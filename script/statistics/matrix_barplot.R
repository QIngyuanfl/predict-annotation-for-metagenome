# Author: Qingyuan Zhang
# Date: Mon Dec  2 14:00:24 CST 2019
# Version: 0.1
library(tidyverse)
library(reshape2)
library(scales)
rgs <- commandArgs(T)
if (!dir.exists(rgs[3])) {
  dir.create(rgs[3])
}
# setting
theme_set(theme_classic())
manu_color <- c(52,619,453,71,134,448,548,655,574,36,544,89,120,131,596,147,576,58,429,386,122,87,404,466,124,463,552,147,45,30,54,84,256,100,652,31,610,477,150,50,588,621,99,81,503,562,76,96,495)
manu_color <- colors()[manu_color]
# input 
df <- read_tsv(rgs[1])
df <- mutate(df, sum = rowSums(df[, 2:dim(df)[2]])) %>%
  arrange(desc(sum)) 
df$sum <- NULL
mapping <- read_tsv(rgs[2])[, -1] 
# draw
for (col in colnames(mapping)) {
  font.length <- length(str_count(max(mapping[[col]])))
  sample.length <- length(mapping[[col]])
  store.name <- file.path(rgs[3], col)
  if (!dir.exists(store.name)) {
    dir.create(store.name)
  }
  # if (font.length > 7 || (sample.length > 10 & sample.length <= 30)) {
  #   x.text.angle <- 75
  #   x.text.hjust <- 1.0
  #   x.text.size <- 22
  # } else {
  #   x.text.size <- 22
  # }
  # if (sample.length == 1) {
  #   x.text.size <- 22
  # }
  # if (font.length > 5 || (sample.length > 5 & sample.length <= 15)) {
  #   x.text.wrap.angle <- 75
  #   x.text.wrapper.hjust <- 1.0
  #   x.text.wrapper.size <- 22
  #   col.n <- 5
  # } else if (sample.length > 15) {
  #   x.text.wrap.angle <- 85
  #   x.text.wrapper.hjust <- 1.0
  #   x.text.wrapper.size <- 14
  #   if (sample.length <= 30) {col.n <- 4}
  #   if (sample.length > 30) {col.n <- 3}
  # } else {
  #   x.text.wrapper.size <- 22
  #   col.n <- 5
  # }
   if (sample.length > 30 || font.length > 7) {
     flip <- T
   } else {
     flip <- F
   }
  if (col == "SampleID") {
    df.sample <- mutate(df, sum = rowSums(df[, 2:dim(df)[2]])) %>%
      arrange(desc(sum)) %>%
      head(10) 
    df.sample$sum <- NULL
    write_tsv(df.sample, str_c(store.name, '/', colnames(df)[1], '.txt'))
    df.sample <- melt(df.sample)
    p <- ggplot(df.sample) +
      geom_bar(aes(x = variable, y = value, fill = get(colnames(df.sample)[1])), stat = "identity", alpha = 0.8)  +
      scale_y_continuous(labels = percent_format(), expand = c(0, 0)) + xlab("") + ylab("Relative abundance") +
      scale_fill_manual(values = manu_color)
    p$labels$fill <- colnames(df)[1]
    P <- if (flip) p + coord_flip() else p
    ggsave(p, filename = str_c(store.name, '/', colnames(df)[1], '.pdf'))
    ggsave(p, filename = str_c(store.name, '/', colnames(df)[1], '.png'))
    p.wrap <- p + facet_wrap(~ get(colnames(df)[1])) +
      theme(axis.text.x = element_text(angle = 45, hjust = 0.5))
    ggsave(p.wrap, filename = str_c(store.name, '/', colnames(df)[1], '_wrap.pdf'), width = 16, height = 9)
    ggsave(p.wrap, filename = str_c(store.name,'/',  colnames(df)[1], '_wrap.png'), width = 16, height = 9)
  }
  if (col != "SampleID") {
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
      head(10) 
    df.group$sum = NULL
    df.group <- df.group[, c(colnames(df)[1], names(group.list))]
    write_tsv(df.group, str_c(store.name, '/', colnames(df)[1], '.txt'))
    df.group <- melt(df.group)
    p <- ggplot(df.group) +
      geom_bar(aes(x = variable, y = value, fill = get(colnames(df.group)[1])), stat = "identity", alpha = 0.8)  +
      scale_y_continuous(labels = percent_format(), expand = c(0, 0)) + xlab("") + ylab("Relative abundance") +
      scale_fill_manual(values = manu_color)
    p$labels$fill <- colnames(df)[1]
    P <- if (flip) p + coord_flip() else p
    ggsave(p, filename = str_c(store.name, '/', colnames(df)[1], '.pdf'))
    ggsave(p, filename = str_c(store.name, '/', colnames(df)[1], '.png'))
    p.wrap <- p + facet_wrap(~ get(colnames(df)[1])) +
      theme(axis.text.x = element_text(angle = 45, hjust = 0.5))
    ggsave(p.wrap, filename = str_c(store.name, '/', colnames(df)[1], '_wrap.pdf'), width = 16, height = 9)
    ggsave(p.wrap, filename = str_c(store.name, '/', colnames(df)[1], '_wrap.png'), width = 16, height = 9)
    }
}

