#!/usr/bin/env python
# author: Qingyuan Zhang
# date: Fri Nov 22 2019
# version: v1.0
import os
import argparse
from multiprocessing import Pool
from itertools import combinations
import pandas as pd

def top10_selected_species(OTU, comb, condition, outdir):
    str_len  = max([len(i) for i in comb])
    if str_len >= 6 and str_len <= 12:
        axis_title_size = 14
        scale = 1.5
    if str_len > 12:
        axis_title_size = 12
        scale = 1.8
    if str_len < 6:
        axis_title_size = 15
        scale = 1
    part = OTU[[i for i in comb]]
    part['Sum'] = part.sum(axis = 1)
    part.sort_values(by = ['Sum'], ascending = False, inplace = True)
    part = part.drop(['Unclassified'])
    part = part.head(10)
    part['Grade'] = [i for i in range(len(part),0,-1)]
    part = part.drop(columns = 'Sum')
    directory = os.path.join(outdir, condition, '-VS-'.join([i for i in comb]))
    if not os.path.exists(directory):
        os.makedirs(directory)
    Rscript = os.path.join(directory, f'{OTU.index.name}_Rscript.R')
    part.to_csv(os.path.join(directory, f'{OTU.index.name}_ternaryplot.txt'), sep = '\t')
    with open(Rscript, 'w') as f:
        f.write(f'''
library(ggtern)
library(grid)
library(scales)
df <- read.table("{directory}/{OTU.index.name}_ternaryplot.txt",header=T,check.name=F,sep="\t")
manu_color <- c(52,619,453,71,134,448,548,655,574,36,544,89,120,131,596,147,576,58,429,386,122,87,404,466,124,463,552,147,45,30,54,84,256,100,652,31,610,477,150,50,588,621,99,81,503,562,76,96,495)
manu_color <- colors()[manu_color]
p <- ggtern(df,aes({comb[0]},{comb[1]},{comb[2]})) + geom_point(aes(size=Grade,color={OTU.index.name})) + theme_rgbw() + scale_color_manual(values=manu_color)
p <- p + theme(axis.text=element_text(face="bold",size=12,color="black"),
            axis.title=element_text(size={axis_title_size},color="black",face="bold"),
            axis.line=element_line(size=1.0,color="black"),
            axis.ticks=element_line(size=1.0,color="black"),
            legend.title=element_text(size=14,face="bold"),
            legend.text=element_text(size=10,face="bold"),
            legend.justification=c(0,1),
            legend.position=c(0,1),
            legend.box.just='left') +
    guides(colour=guide_legend(override.aes=list(size=2),order=1),size=guide_legend(order=2))
ggsave("{directory}/{OTU.index.name}_ternaryplot.pdf",p,width=9,height=8,scale={scale})
ggsave("{directory}/{OTU.index.name}_ternaryplot.png",p,width=9,height=8,scale={scale})
unlink('Rplots.pdf')
''')
    
    os.system(f'Rscript {Rscript}')


def concat_otu(OTU, group_dict:dict):
    OTU = pd.read_table(OTU, index_col = 0)
    for x in group_dict:
        if x not in OTU:
            OTU[x] = 0*OTU.shape[0]
        for y in group_dict[x]:
            OTU[x] += OTU[y]
        OTU[x] = OTU[x]/len(group_dict[x])
    return OTU
    
def main():
# params
    group_info = pd.read_table(arg.mapping, index_col = 0)
# samples in each group
    group = {}    
    for col in group_info:
        if 'Condition' in col:
            condition = group_info[col]
            for sample in pd.unique(condition):
                if sample in group:
                    group[sample] += condition[condition.values == sample].index.tolist()
                if sample not in group:
                    group[sample] = condition[condition.values == sample].index.tolist()
# ternary plot combination
    comb = {}
    group_list = []
    if arg.combination == ['All']:
        for i in group_info:
            id_set = pd.unique(group_info[i])
            if len(id_set) < 3:
                continue
            subgroup_dir = os.path.join(arg.outdir, i)
            if not os.path.exists(subgroup_dir):
                os.makedirs(subgroup_dir)
            if 'Condition' in i:
                group_list += id_set.tolist()
            comb_set = list(combinations(id_set, 3))
            for x in comb_set:
                comb.update({x:i})
    else:
        subgroup_dir = os.path.join(arg.outdir, 'Selected')
         
        for i in arg.combination:
            id_set = tuple(i.split(','))
            for j in id_set:
                if j in group:
                    group_list.append(j)
            assert len(id_set) == 3, \
            print('The combination to draw ternary plot has to be 3')
            comb.update({id_set:'Selected'})

    for i in set(group):
        if i not in group_list:
            del(group[i])
# cores setting
    if arg.cores <= len(comb):
        process = arg.cores
    if arg.cores > len(comb):
        process = len(comb)

# group abundance calculated by average
    with Pool(process) as p:
        result = p.starmap(concat_otu, list(zip(arg.infile, [group]*len(arg.infile))))
        top10_args = []
        for i in result:
            for j in comb:
                top10_args.append((i, j, comb[j], arg.outdir))
        p.starmap(top10_selected_species, top10_args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw ternary plot with OTU table and grouping information')
    parser.add_argument('-i', '--input', dest='infile', nargs='+',
help='A tabular matrix , columns: ID, S1, S2...')
    parser.add_argument('-o', '--output', dest='outdir', default='.',
help='path to output directory')
    parser.add_argument('-c', '--combination', dest='combination', default=['All'],
nargs='*', help='combinations among different groups or samples')
    parser.add_argument('-m', '--mapping', dest='mapping',
help='The mapping file for metagenome, a tabular form, columns : #SampleID   Condition1  SampleID')
    parser.add_argument('-p', '--cores', dest = 'cores', type=int, default=1,
help='Numbers of CPUs to use')
    arg = parser.parse_args()
    assert arg.infile and arg.mapping, parser.print_help()
    if not os.path.exists(arg.outdir):
        os.makedirs(arg.outdir)
    main()

