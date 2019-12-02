library(ggbiplot)
library(tidyverse)
rgs=commandArgs(T)
# 读入实验设计
design <- read_tsv(rgs[1])
#design <- read_tsv('mapping.txt')
# 读取OTU表
otu_table <- read_tsv(rgs[2])
#otu_table <- read_tsv("Table_taxa_NR_Class.txt")
# 过滤数据并排序
idx <- design$SampleID %in% colnames(otu_table)
sub_design <- design[idx, ][, -1]
count <- otu_table[, sub_design$SampleID]

# PCA 分析
otu.pca <- prcomp(t(count)[ , apply(t(count), 2, var) != 0], scale. = TRUE, center= TRUE)

# PCA绘图
for ( i in colnames(sub_design)){
  p <- ggbiplot(otu.pca, obs.scale = 1, var.scale = 1, varname.size = 2, 
    groups = sub_design[[i]], ellipse = F,var.axes = F) + ggtitle("PCA - Class") + theme_bw() + theme(panel.grid=element_blank())

  p.label <- p + geom_text(aes(label=design$SampleID),hjust=-0.25, vjust=0, size = 2.5)
i
  if(all(table(unlist(design[[i]])) > "2" )) {
    p.ellipse <- ggbiplot(otu.pca, obs.scale = 1, var.scale = 1, varname.size = 2, groups = sub_design[[i]], ellipse = TRUE,var.axes = F) +ggtitle("PCA - Class level") + theme_bw()+ theme(panel.grid=element_blank())
    p.ellipse.label <- p.ellipse + geom_text(aes(label=design$SampleID),hjust=-0.25, vjust=0, size = 2.5)
    ggsave(p.ellipse, filename=str_c(rgs[4], "/PCA_ellipse_", i, "_", rgs[3], ".pdf"), dpi=600, width=16, height=12, units=c("cm"))
    ggsave(p.ellipse.label, filename=str_c(rgs[4], "/PCA_ellipse_", i, "_label_", rgs[3], ".pdf"), dpi=600, width=16, height=12, units=c("cm"))
}
  ggsave(p, filename = str_c(rgs[4], "/PCA_", i, "_", rgs[3], ".pdf"), dpi=600, width=16, height=12, units=c("cm"))
  ggsave(p.label, filename=str_c(rgs[4], "/PCA_", i, "_label_", rgs[3], ".pdf"), dpi=600, width=16, height=12, units=c("cm"))
}
