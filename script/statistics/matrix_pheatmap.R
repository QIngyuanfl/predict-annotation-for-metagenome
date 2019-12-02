# Author: Qingyuan Zhang
# Date
# Version: 0.1

library(tidyverse)
library(pheatmap)
rgs <- commandArgs(T)

if (!dir.exists(rgs[3])) {
  dir.create(rgs[3])
}
# setting
theme_set(theme_classic())
# input 
df <- read_tsv(rgs[1])
mapping <- read_tsv(rgs[2])[, -1] 
# select top 35 taxonomy

for (col in colnames(mapping)) {
  store.name <- file.path(rgs[3], col)
  if (!dir.exists(store.name)) {
    dir.create(store.name)
  }
  if (col == "SampleID") {
    df.sample <- mutate(df, sum = rowSums(df[, 2:dim(df)[2]])) %>%
      arrange(desc(sum)) %>%
      head(35) 
    df.sample$sum <- NULL
    write_tsv(df.sample, str_c(store.name, '/', colnames(df)[1], '_top35.txt'))
    df.sample <- as.data.frame(df.sample, row.names = 1, col.names = 1)
    rownames(df.sample) <- df.sample[[1]]
    df.sample <- df.sample[, -1]
    pheatmap(df.sample, cellheight = 14, scale = 'row', color=colorRampPalette(c("navy", "white", "firebrick3"))(100),
             filename = str_c(store.name, '/', colnames(df)[1], '_top35.pdf'))
    pheatmap(df.sample, cellheight = 14, scale = 'row', color=colorRampPalette(c("navy", "white", "firebrick3"))(100),
             filename = str_c(store.name, '/', colnames(df)[1], '_top35.png'))
  } else {
    
    group.list <- list()
    for (i in seq_along(mapping[[col]])) {
      condition <- mapping[[col]][i]
      if (condition %in% names(group.list)) {
        group.list[[condition]] <- append(group.list[[condition]], mapping$SampleID[i])
      } else  {
        group.list[[condition]] <- mapping$SampleID[i]
      }
    }
    df.group <- list()
    for (group in names(group.list)) {
      df.group[[group]] <- apply(select(df, group.list[[group]]), 1, mean)
    }
    df.group <- as_tibble(df.group) %>%
      mutate(Taxo = df[[colnames(df)[1]]])
    colnames(df.group)[length(colnames(df.group))] <- colnames(df)[1]
    df.group <- mutate(df.group, sum = rowSums(df[, 2:dim(df)[2]])) %>%
      arrange(desc(sum)) %>%
      head(35) 
    df.group$sum = NULL
    df.group <- df.group[, c(colnames(df)[1], names(group.list))] 
    write_tsv(df.group, str_c(store.name, '/', colnames(df)[1], '_top35.txt'))
    df.group <-  as.data.frame(df.group, row.names = 1, col.names = 1)
    rownames(df.group) <- df.group[[1]]
    df.group <- df.group[, -1]

    pheatmap(df.group, cellheight = 14, scale = 'column', color=colorRampPalette(c("navy", "white", "firebrick3"))(100),
             filename = str_c(store.name, '/', colnames(df)[1], '_top35.pdf'))
    p <- pheatmap(df.group, cellheight = 14, scale = 'column', color=colorRampPalette(c("navy", "white", "firebrick3"))(100),
             filename = str_c(store.name, '/', colnames(df)[1], '_top35.png'))
  }
}
