#!/usr/bin/env python
# Author: Qingyuan Zhang
# Date: Wed Nov 20 17:03:20 CST 2019
# version: 1.0
import os
import argparse
from itertools import combinations
from functools import reduce
from multiprocessing import Pool
import pandas as pd

def add_group(df, mapping):
    group = {}
    for col in mapping:
        if 'Condition' not in col:
            continue
        group = tuple(zip(mapping[col].tolist(), mapping[col].index.tolist()))
        for j in group:
            if j[0] in df:
                df[j[0]] += df[j[1]]
            if j[0] not in df:
                df[j[0]] = df[j[1]]
    return df

def abundance_split_greater0(Sample) -> dict:
    counter = {}
    uniq = Sample[Sample > 0].index.to_list()
    with open(f'{arg.outfile}/{Sample.name}_uniq.list', 'w') as f:
        f.write('\n'.join(uniq))
    counter[Sample.name] = len(uniq)
    
    return counter

def draw_venn(combination:dict):
    samples = list((list(combination.keys())[0]))
    condition = list(combination.values())[0]
    Venn_Rscript = os.path.join(arg.outfile, f'Venn_{condition}_{"_".join(samples)}.r')
    outdir = os.path.abspath(os.path.join(arg.outfile, condition))
    with open(Venn_Rscript, 'w') as f:
        f.write(r'''library(VennDiagram)
library(ggplot2)
color_v <- c("dodgerblue", "goldenrod1", "darkorange1", "seagreen3", "orchid3", "cornsilk3", "dodgerblue4","gray45", "lemonchiffon2", "skyblue1", "palegreen4", "orange1", "nava", "navajowhite","tan1")
''')
        for i in samples:
            f.write(f'list{i} <- read.csv("{os.path.abspath(arg.outfile)}/{i}_uniq.list", header = F)[,1]\n')
            f.write(f'list{i} <- as.vector(list{i})\n')
        all_list = ','.join([f'list{i}' for i in samples])
        c = ','.join([f'"{i}"' for i in samples])
        f.write(f'\np <- venn.diagram( x = list({all_list}), filename=NULL,fill = color_v[1:{len(samples)}], include = "both",category.names = c({c}))\n')
        f.write('grid.draw(p)\n')
        f.write(f'ggsave ("{outdir}/Venn_{condition}_{"-".join(samples)}_{len(samples)}.pdf",grid.draw(p),width = 8 , height = 8, useDingbats=F)\n')
        f.write('dev.off()\n')
    os.system(f'Rscript {Venn_Rscript}')

def intersection(id_set):
    gene = []
    for i in id_set:
        with open(f'{arg.outfile}/{i}_uniq.list') as f:
             gene.append([line.strip() for line in f])
    intercept =  reduce(lambda x,y : set(x) & set(y), gene)
    return len(intercept)  

def draw_petal(condition, counter:dict, cross):
    Petal_Rscript = os.path.join(arg.outfile, f'Petal_{condition.name}_All.r')
    with open(Petal_Rscript, 'w') as f:
        f.write(r'''
library(ggplot2)
library(plotrix)
flower_plot2 <- function(sample, value, start, a, b,
                         ellipse_col = rgb(135, 206, 235, 150, max = 255),
                         circle_col = rgb(0, 162, 214, max = 255),
                         circle_text_cex = 1, labels=labels) {
  par( bty = "n", ann = F, xaxt = "n", yaxt = "n", mar = c(1,1,1,1))
  plot(c(0,10),c(0,10),type="n")
  n   <- length(sample)
  deg <- 360 / n
  res <- lapply(1:n, function(t){
    ellipse_col <- ellipse_col[t]
    plotrix::draw.ellipse(x = 5 + cos((start + deg * (t - 1)) * pi / 180),
                          y = 5 + sin((start + deg * (t - 1)) * pi / 180),
                          col = ellipse_col,
                          border = ellipse_col,
                          a = a, b = b, angle = deg * (t - 1))
    text(x = 5 + 2.5 * cos((start + deg * (t - 1)) * pi / 180),
         y = 5 + 2.5 * sin((start + deg * (t - 1)) * pi / 180),         
         value[t]
    )

    if (deg * (t - 1) < 180 && deg * (t - 1) > 0 ) {
      text(x = 5 + 3.3 * cos((start + deg * (t - 1)) * pi / 180),
           y = 5 + 3.3 * sin((start + deg * (t - 1)) * pi / 180),
           sample[t],
           srt = deg * (t - 1) - start,
           adj = 1,
           cex = circle_text_cex
      )

    } else {
      text(x = 5 + 3.3 * cos((start + deg * (t - 1)) * pi / 180),
           y = 5 + 3.3 * sin((start + deg * (t - 1)) * pi / 180),
           sample[t],
           srt = deg * (t - 1) + start,
           adj = 0,
           cex = circle_text_cex
      )
    }
  })
  plotrix::draw.circle(x = 5, y = 5, r = 1.5, col = circle_col, border = circle_col )
  text(x = 4.7, y = 5, labels=labels)
}
''')
        sample = pd.unique(condition)
        N = len(sample)
        N_uniq_list =  [str(counter[i]) for i in sample]
        sample = ','.join([f'"{i}"' for i in sample])
        N_uniq_list = ','.join(N_uniq_list)
        f.write(f'''
ggsave(flower_plot2 (c({sample}), 
c({N_uniq_list}), 90, 0.5, 2, labels=paste("     ",{cross},sep=""),
ellipse_col = topo.colors({N}, alpha = 0.5),
circle_col = topo.colors(1, alpha = 0.7) ), 
filename=paste("{os.path.join(arg.outfile, condition.name)}/Petal_{condition.name}_",{N},".pdf", sep=""), dpi=600, width=16,
height=12, units=c("cm"),colormodel="srgb")
''')
    os.system(f'Rscript {Petal_Rscript}')

   

    
def main():
# params
    outdir = arg.outfile
    OTU = arg.infile
    combination = arg.combination
    cores = arg.cores
    mapping = pd.read_table(arg.mapping, index_col = 0)
    for i in mapping:
        if not os.path.exists(os.path.join(outdir, mapping[i].name)):
            os.makedirs(os.path.join(outdir, mapping[i].name))
    OTU = pd.read_table(arg.infile, index_col = 0)
    OTU = add_group(OTU, mapping)
# uniq list
    if cores <= OTU.shape[1]:
        process = OTU.shape[1]
    if cores > OTU.shape[1]:
        process = cores
    with Pool(process) as p:   
        gene_number = p.map(abundance_split_greater0, [OTU[i] for i in OTU.columns])
    gene_number_dict = {}
    for i in gene_number:
        gene_number_dict.update(i)
    
    comb_all = []
    if combination == ['All']:
        for i in mapping:
            id_set = pd.unique(mapping[i])
            for j in range(2,6):
                if len(id_set) < j:
                    continue
                comb = list(combinations(id_set, j))
                comb = [ {x:i} for x in comb]
                comb_all += comb
    else:
        selected = os.path.join(outdir, 'Selected')
        if not os.path.exists(selected):
            os.makedirs(selected)
        for i in combination:
            comb = i.split(',')
            assert len(comb) <= 5, print('The numbers of selected groups or samples to depict Venn plot should not exceed 5')
            comb = [{tuple(comb):'Selected'}]
            comb_all += comb
    if cores <= len(comb_all):
        process = len(comb_all)
    if cores > len(comb_all):
        process = cores
    with Pool(process) as p:
        p.map(draw_venn, comb_all)

# petal plot
    for i in mapping:
        id_set = pd.unique(mapping[i])
        if len(id_set) > 5:
            inner = intersection(id_set)
            draw_petal(mapping[i], gene_number_dict, inner)
                
                       
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw Venn plot or petal plot with OTU table and grouping information')
    parser.add_argument('-i', '--input', dest='infile', 
help='A tabular matrix , columns: ID, S1, S2...')
    parser.add_argument('-o', '--output', dest='outfile', default='.',
help='path to output directory')
    parser.add_argument('-c', '--combination', dest='combination', default='All', 
nargs='*', help='combinations among different groups or samples')
    parser.add_argument('-m', '--mapping', dest='mapping', 
help='The mapping file for metagenome, a tabular form, columns : #SampleID   Condition1  SampleID')
    parser.add_argument('-p', '--cores', dest = 'cores', type=int, default=1,
help='Numbers of CPUs to use')
    arg = parser.parse_args()
    assert arg.infile and arg.mapping, parser.print_help()
    if not os.path.exists(arg.outfile):
        os.makedirs(arg.outfile)
    main()
