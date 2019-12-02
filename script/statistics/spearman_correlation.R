Args <- commandArgs(T)
depthFile = Args[1]
prefix = Args[2]
library(tidyverse)
library(pheatmap)
df <- read.table(depthFile, header = T, row.names = 1, check.names = TRUE, quote = "", fill = T, sep="\t") %>%
head(500000)
otu_cor <- cor(df, method = "spearman")
write.csv(otu_cor, file = paste(prefix,"spearman_cor_table.csv",sep = "."), quote = F, row.names = TRUE)
otu_cor_p <- apply(df, 2, function(x)apply(df,2,function(y) cor.test(x,y,method = "spearman")$p.value))
write.csv(otu_cor_p, file = paste(prefix,"spearman_cor_pvalue.csv",sep="."), quote = F, row.names = TRUE)
pheatmap(otu_cor, display_numbers = TRUE, cellheight = 12, cellwidth = 15, 
border_color = NA,  
cluster_rows = TRUE, cluster_cols = TRUE, legend = TRUE, fontsize = 7, 
fontsize_col = 7, fontsize_row = 7, annotation_legend = FALSE, 
filename = paste(prefix,"spearman_cor_heatmap.pdf",sep="."))
#pheatmap(otu_cor, display_numbers = TRUE, cellheight = 12, cellwidth = 15,
#border_color = NA,
#cluster_rows = TRUE, cluster_cols = TRUE, legend = TRUE, fontsize = 7,
#fontsize_col = 7, fontsize_row = 7, annotation_legend = FALSE,
#filename = paste(prefix,"spearman_cor_heatmap.png",sep="."))

