#!/usr/bin/env Rscript
rgs <- commandArgs(T)
library(plyr)
library(tidyverse)
library(phyloseq)
library(ellipse)
library(ggrepel)
library(vegan)

theme_set(theme_bw())
rank <- str_match(basename(rgs[1]), "abundance_table_(.*).biom")[,2]
print(rank)
otutable <- import_biom(BIOMfilename = rgs[1], parseFunction = parse_taxonomy_greengenes)
mapping <- import_qiime_sample_data(mapfilename = rgs[2])[, -1]
outdir <- rgs[3]
if (!dir.exists(outdir)){
  dir.create(outdir)
}
physeq <- merge_phyloseq(otutable, mapping)
physeq <- prune_taxa(taxa_sums(physeq) > 0, physeq) %>%
  transform_sample_counts(function(x) x/sum(x)) %>%
  subset_samples()
dist_methods <- c("bray", "jaccard")
for (col in colnames(mapping)) {
  if (any(table(unlist(mapping$col)) == "1")) {
    next
  }
  if (col != "SampleID") {
  cat("dist,method,test,sub-condition1 vs sub-condition2,Df,SumsOfSqs,MeanSqs,F.Model,R2,Pr(>F)", "\n", file = str_c(outdir, "/", "statistics_adonis_", col, "_", rank, ".txt"), append = TRUE)
  cat("dist,method,test,sub-condition1 vs sub-condition2,R-value,P-value", "\n", file= str_c(outdir, "/", "statistics_anosim_", col, "_", rank, ".txt"), append = TRUE)
  cat("dist,method,test,sub-condition1 vs sub-condition2,A,observed-delta,expected-delta,Significant", "\n", file= str_c(outdir, "/", "statistics_mrpp_", col, "_", rank, ".txt"), append = TRUE)
  }
  Condition = mapping[[col]]
  for (dist in dist_methods) {
    ord_meths = c("DCA", "CCA", "RDA", "NMDS", "MDS", "PCoA")
    plist = llply(as.list(ord_meths), function(i, physeq, dist){
      ordi = ordinate(physeq, method = i, distance = dist)
      plot_ordination(physeq, ordi, "samples", color = col)
    }, physeq, dist)
    names(plist) <- ord_meths
    # Write distance matrix
    matrix.distance <- as.data.frame(as.matrix(distance(physeq,dist)))
    write.table(matrix.distance, file = paste(outdir, "/distance_matrix_",dist,".txt",sep = ""), quote = F,row.names = T, col.names = T,sep = "\t")
    # significant difference test
    if (col != 'SampleID') {
      condition.uniq <- levels(mapping[[col]])
      condition.comb <- combn(condition.uniq, 2)
      
      
      j <- 1
      while (j <= length(condition.comb[1,])) {
        design.sub = subset(mapping, get(col) %in% condition.comb[,j])
        dis.sub = matrix.distance[rownames(design.sub), rownames(design.sub)] %>%
          as.dist(diag = FALSE, upper = FALSE)
        # for adonis
        adonis.table = adonis(dis.sub~get(col), data = data.frame(design.sub), permutations = 10000)
        adonis.pvalue = adonis.table$aov.tab$`Pr(>F)`[1]    
        cat(paste(dist, "All", "adonis",paste(condition.comb[1,j],"vs",condition.comb[2,j],sep = " "),adonis.table$aov.tab$Df[1],format(adonis.table$aov.tab$SumsOfSqs[1], digits = 3),format(adonis.table$aov.tab$MeanSqs[1], digits = 3),format(adonis.table$aov.tab$F.Model[1], digits = 3),format(adonis.table$aov.tab$R2[1], digits = 3),format(adonis.table$aov.tab$`Pr(>F)`[1], digits = 3, scientific = TRUE),sep = ","), "\n", file = str_c(outdir, "/", "statistics_adonis_", col, "_", rank, ".txt"), append = TRUE)
        # for anosim
        anosim.table = anosim(dis.sub, design.sub[[col]], permutations = 10000)
        anosim.pvalue = anosim.table$signif
        cat(paste(dist,"All","anosim", paste(condition.comb[1,j],"vs",condition.comb[2,j],sep = " "),format(anosim.table$statistic, digits = 3),format(anosim.pvalue, digits = 3, scientific = TRUE),sep = ","), "\n", file = str_c(outdir, "/", "statistics_anosim_", col, "_", rank, ".txt"), append = TRUE)
        # for mrpp
        mrpp.table = mrpp(dis.sub, design.sub[[col]], permutations = 10000)
        mrpp.pvalue = mrpp.table$Pvalue
        cat(paste(dist,"All","mrpp",paste(condition.comb[1,j],"vs", condition.comb[2,j],sep = " "),format(mrpp.table$A, digits = 3),format(mrpp.table$delta, digits = 3),format(mrpp.table$E.delta, digits = 3),format(mrpp.table$Pvalue, digits = 3, scientific = TRUE),sep = ","), "\n", file = str_c(outdir, "/", "statistics_anosim_", col, "_", rank, ".txt"), append = TRUE)
        j <- j + 1
      }
        
    }
    # DCA
    ## Neither ellipses nor labels
    DCA.dir <- file.path(outdir, "DCA")
    if (!dir.exists(DCA.dir)) {
      dir.create(DCA.dir)
    }
    p <- plist[[1]] + geom_point(size = 4, alpha = 0.5)  + scale_fill_brewer(type = "qual", palette = "Set1") +
      scale_colour_brewer(type = "qual", palette = "Set1") + theme(panel.grid = element_blank()) +
      ggtitle(paste("DCA (method=",dist,") - ", rank, "\n",sep = ""))
    ggsave(p, filename = paste(DCA.dir, '/', dist, "_DCA_", col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## with labels
    p.labels <- p + geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.labels, filename = paste(DCA.dir, '/', dist, "_DCA_", col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    
    ## with ellipse
    if (col != 'SampleID') {
    
    test_selected <- plist$DCA$data
    coordinate.file <- str_c(DCA.dir, "/", "coordinates", "_DCA_", dist, ".txt")
    if (!file.exists(coordinate.file)) {
      write.table(test_selected[,1:2], coordinate.file, quote = F,row.names = T, col.names = T,sep = "\t")
    }
    centroids <- aggregate(cbind(DCA1,DCA2)~Condition,test_selected,mean)
    colnames(centroids)[1] <- col
    conf.rgn  <- do.call(rbind,lapply(unique(test_selected[[col]]),function(t)
      df <- data.frame(Condition = as.character(t),
                 ellipse(cov(test_selected[test_selected[[col]] == t,1:2]), 
                         centre = as.matrix(centroids[t,2:3]), level = 0.95), stringsAsFactors = FALSE)
      ))
    colnames(conf.rgn)[1] <- col
    test_selected <- merge(test_selected,centroids,by = col,suffixes = c("",".centroid"))
    p.ellipse <- p + geom_path(data = conf.rgn) + geom_point(data = centroids, size = 2) +
    geom_point(data = centroids, size = 2) +
    geom_segment(data = test_selected, aes(x = DCA1.centroid, y = DCA2.centroid, xend = DCA1, yend = DCA2))
    ggsave(p.ellipse, filename = paste(DCA.dir, '/', dist, "_DCA_", 'ellipse_', col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## Both ellipse and labels
    p.ellipse.labels <- p.ellipse + 
      geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.ellipse, filename = paste(DCA.dir, '/', dist, "_DCA_", 'ellipse_', col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    }
    # CCA
    ## Neither ellipses nor labels
    CCA.dir <- file.path(outdir, "CCA")
    if (!dir.exists(CCA.dir)) {
      dir.create(CCA.dir)
    }
    p <- plist[[2]] + geom_point(size = 4, alpha = 0.5)  + scale_fill_brewer(type = "qual", palette = "Set1") +
      scale_colour_brewer(type = "qual", palette = "Set1") + theme(panel.grid = element_blank()) +
      ggtitle(paste("CCA (method=",dist,") - ", rank, "\n",sep = ""))
    ggsave(p, filename = paste(CCA.dir, '/', dist, "_CCA_", col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## with labels
    p.labels <- p + geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.labels, filename = paste(CCA.dir, '/', dist, "_CCA_", col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    
    ## with ellipse
    if (col != 'SampleID') {
    test_selected <- plist$CCA$data
    coordinate.file <- str_c(CCA.dir, "/", "coordinates", "_CCA_", dist, ".txt")
    if (!file.exists(coordinate.file)) {
      write.table(test_selected[,1:2], coordinate.file, quote = F,row.names = T, col.names = T,sep = "\t")
    }
    centroids <- aggregate(cbind(CA1,CA2)~Condition,test_selected,mean)
    colnames(centroids)[1] <- col
    conf.rgn  <- do.call(rbind,lapply(unique(test_selected[[col]]),function(t)
      df <- data.frame(Condition = as.character(t),
                       ellipse(cov(test_selected[test_selected[[col]] == t,1:2]), 
                               centre = as.matrix(centroids[t,2:3]), level = 0.95), stringsAsFactors = FALSE)
    ))
    colnames(conf.rgn)[1] <- col
    test_selected <- merge(test_selected,centroids,by = col,suffixes = c("",".centroid"))
    p.ellipse <- p + geom_path(data = conf.rgn) + geom_point(data = centroids, size = 2) +
      geom_point(data = centroids, size = 2) +
      geom_segment(data = test_selected, aes(x = CA1.centroid, y = CA2.centroid, xend = CA1, yend = CA2))
    ggsave(p.ellipse, filename = paste(CCA.dir, '/', dist, "_CCA_", 'ellipse_', col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## Both ellipse and labels
    p.ellipse.labels <- p.ellipse + 
      geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.ellipse, filename = paste(CCA.dir, '/', dist, "_CCA_", 'ellipse_', col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    }
    # RDA
    RDA.dir <- file.path(outdir, "RDA")
    if (!dir.exists(RDA.dir)) {
      dir.create(RDA.dir)
    }
    ## Neither ellipses nor labels
    p <- plist[[3]] + geom_point(size = 4, alpha = 0.5)  + scale_fill_brewer(type = "qual", palette = "Set1") +
      scale_colour_brewer(type = "qual", palette = "Set1") + theme(panel.grid = element_blank()) +
      ggtitle(paste("RDA (method=",dist,") - ", rank, "\n",sep = ""))
    ggsave(p, filename = paste(RDA.dir, '/', dist, "_RDA_", col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## with labels
    p.labels <- p + geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.labels, filename = paste(RDA.dir, '/', dist, "_RDA_", col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    
    ## with ellipse
    if (col != 'SampleID') {
    test_selected <- plist$RDA$data
    coordinate.file <- str_c(RDA.dir, "/", "coordinates", "_RDA_", dist, ".txt")
    if (!file.exists(coordinate.file)) {
      write.table(test_selected[,1:2], coordinate.file, quote = F,row.names = T, col.names = T,sep = "\t")
    }
    
    centroids <- aggregate(cbind(PC1,PC2)~Condition,test_selected,mean)
    colnames(centroids)[1] <- col
    conf.rgn  <- do.call(rbind,lapply(unique(test_selected[[col]]),function(t)
      df <- data.frame(Condition = as.character(t),
                       ellipse(cov(test_selected[test_selected[[col]] == t,1:2]), 
                               centre = as.matrix(centroids[t,2:3]), level = 0.95), stringsAsFactors = FALSE)
    ))
    colnames(conf.rgn)[1] <- col
    test_selected <- merge(test_selected,centroids,by = col,suffixes = c("",".centroid"))
    p.ellipse <- p + geom_path(data = conf.rgn) + geom_point(data = centroids, size = 2) +
      geom_point(data = centroids, size = 2) +
      geom_segment(data = test_selected, aes(x = PC1.centroid, y = PC2.centroid, xend = PC1, yend = PC2))
    ggsave(p.ellipse, filename = paste(RDA.dir, '/', dist, "_RDA_", 'ellipse_', col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    
    ## Both ellipse and labels
    p.ellipse.labels <- p.ellipse + 
      geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.ellipse, filename = paste(RDA.dir, '/', dist, "_RDA_", 'ellipse_', col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    }
    # NMDS
    NMDS.dir <- file.path(outdir, "NMDS")
    if (!dir.exists(NMDS.dir)) {
      dir.create(NMDS.dir)
    }
    ## Neither ellipses nor labels
    p <- plist[[4]] + geom_point(size = 4, alpha = 0.5)  + scale_fill_brewer(type = "qual", palette = "Set1") +
      scale_colour_brewer(type = "qual", palette = "Set1") + theme(panel.grid = element_blank()) +
      ggtitle(paste("NMDS (method=",dist,") - ", rank, "\n",sep = ""))
    ggsave(p, filename = paste(NMDS.dir, '/', dist, "_NMDS_", col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## with labels
    p.labels <- p + geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.labels, filename = paste(NMDS.dir, '/', dist, "_NMDS_", col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    
    ## with ellipse
    if (col != 'SampleID') {
    test_selected <- plist$NMDS$data
    coordinate.file <- str_c(NMDS.dir, "/", "coordinates", "_NMDS_", dist, ".txt")
    if (!file.exists(coordinate.file)) {
      write.table(test_selected[,1:2], coordinate.file, quote = F,row.names = T, col.names = T,sep = "\t")
    }
    centroids <- aggregate(cbind(NMDS1,NMDS2)~Condition,test_selected,mean)
    colnames(centroids)[1] <- col
    conf.rgn  <- do.call(rbind,lapply(unique(test_selected[[col]]),function(t)
      df <- data.frame(Condition = as.character(t),
                       ellipse(cov(test_selected[test_selected[[col]] == t,1:2]), 
                               centre = as.matrix(centroids[t,2:3]), level = 0.95), stringsAsFactors = FALSE)
    ))
    colnames(conf.rgn)[1] <- col
    test_selected <- merge(test_selected,centroids,by = col,suffixes = c("",".centroid"))
    p.ellipse <- p + geom_path(data = conf.rgn) + geom_point(data = centroids, size = 2) +
      geom_point(data = centroids, size = 2) +
      geom_segment(data = test_selected, aes(x = NMDS1.centroid, y = NMDS2.centroid, xend = NMDS1, yend = NMDS2))
    ggsave(p.ellipse, filename = paste(NMDS.dir, '/', dist, "_NMDS_", 'ellipse_', col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## Both ellipse and labels
    p.ellipse.labels <- p.ellipse + 
      geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.ellipse, filename = paste(NMDS.dir, '/', dist, "_NMDS_", 'ellipse_', col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    }
    # MDS
    MDS.dir <- file.path(outdir, "MDS")
    if (!dir.exists(MDS.dir)) {
      dir.create(MDS.dir)
    }
    ## Neither ellipses nor labels
    p <- plist[[5]] + geom_point(size = 4, alpha = 0.5)  + scale_fill_brewer(type = "qual", palette = "Set1") +
      scale_colour_brewer(type = "qual", palette = "Set1") + theme(panel.grid = element_blank()) +
      ggtitle(paste("MDS (method=",dist,") - ", rank, "\n",sep = ""))
    ggsave(p, filename = paste(MDS.dir, '/', dist, "_MDS_", col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## with labels
    p.labels <- p + geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.labels, filename = paste(MDS.dir, '/', dist, "_MDS_", col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    
    ## with ellipse
    if (col != 'SampleID') {
    test_selected <- plist$MDS$data
    coordinate.file <- str_c(MDS.dir, "/", "coordinates", "_MDS_", dist, ".txt")
    if (!file.exists(coordinate.file)) {
      write.table(test_selected[,1:2], coordinate.file, quote = F,row.names = T, col.names = T,sep = "\t")
    }
    centroids <- aggregate(cbind(Axis.1,Axis.2)~Condition,test_selected,mean)
    colnames(centroids)[1] <- col
    conf.rgn  <- do.call(rbind,lapply(unique(test_selected[[col]]),function(t)
      df <- data.frame(Condition = as.character(t),
                       ellipse(cov(test_selected[test_selected[[col]] == t,1:2]), 
                               centre = as.matrix(centroids[t,2:3]), level = 0.95), stringsAsFactors = FALSE)
    ))
    colnames(conf.rgn)[1] <- col
    test_selected <- merge(test_selected,centroids,by = col,suffixes = c("",".centroid"))
    p.ellipse <- p + geom_path(data = conf.rgn) + geom_point(data = centroids, size = 2) +
      geom_point(data = centroids, size = 2) +
      geom_segment(data = test_selected, aes(x = Axis.1.centroid, y = Axis.2.centroid, xend = Axis.1, yend = Axis.2))
    ggsave(p.ellipse, filename = paste(MDS.dir, '/', dist, "_MDS_", 'ellipse_', col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## Both ellipse and labels
    p.ellipse.labels <- p.ellipse + 
      geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.ellipse, filename = paste(MDS.dir, '/', dist, "_MDS_", 'ellipse_', col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    }
    # PCoA
    PCoA.dir <- file.path(outdir, "PCoA")
    if (!dir.exists(PCoA.dir)) {
      dir.create(PCoA.dir)
    }
    ## Neither ellipses nor labels
    p <- plist[[6]] + geom_point(size = 4, alpha = 0.5)  + scale_fill_brewer(type = "qual", palette = "Set1") +
      scale_colour_brewer(type = "qual", palette = "Set1") + theme(panel.grid = element_blank()) +
      ggtitle(paste("PCoA (method=",dist,") - ", rank, "\n",sep = ""))
    ggsave(p, filename = paste(PCoA.dir, '/', dist, "_PCoA_", col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## with labels
    p.labels <- p + geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.labels, filename = paste(PCoA.dir, '/', dist, "_PCoA_", col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    
    ## with ellipse
    if (col != 'SampleID') {
    test_selected <- plist$PCoA$data
    coordinate.file <- str_c(PCoA.dir, "/", "coordinates", "_RDA_", dist, ".txt")
    if (!file.exists(coordinate.file)) {
      write.table(test_selected[,1:2], coordinate.file, quote = F,row.names = T, col.names = T,sep = "\t")
    }
    centroids <- aggregate(cbind(Axis.1,Axis.2)~Condition,test_selected,mean)
    colnames(centroids)[1] <- col
    conf.rgn  <- do.call(rbind,lapply(unique(test_selected[[col]]),function(t)
      df <- data.frame(Condition = as.character(t),
                       ellipse(cov(test_selected[test_selected[[col]] == t,1:2]), 
                               centre = as.matrix(centroids[t,2:3]), level = 0.95), stringsAsFactors = FALSE)
    ))
    colnames(conf.rgn)[1] <- col
    test_selected <- merge(test_selected,centroids,by = col,suffixes = c("",".centroid"))
    p.ellipse <- p + geom_path(data = conf.rgn) + geom_point(data = centroids, size = 2) +
      geom_point(data = centroids, size = 2) +
      geom_segment(data = test_selected, aes(x = Axis.1.centroid, y = Axis.2.centroid, xend = Axis.1, yend = Axis.2))
    ggsave(p.ellipse, filename = paste(PCoA.dir, '/', dist, "_PCoA_", 'ellipse_', col, "_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    ## Both ellipse and labels
    p.ellipse.labels <- p.ellipse + 
      geom_text_repel(aes(label = SampleID),hjust = -0.25, vjust = 0, size = 2.5)
    ggsave(p.ellipse, filename = paste(PCoA.dir, '/', dist, "_PCoA_", 'ellipse_', col, "_label_", rank, ".pdf",sep = ""), dpi = 600, width = 16,
           height = 12, units = c("cm"),colormodel = "srgb")
    }
  }
}





