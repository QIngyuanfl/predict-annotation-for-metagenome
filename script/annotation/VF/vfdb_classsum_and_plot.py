#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FileName:  vfdb_classsum_and_plot.py
# Author:    Zhihao Xie  \(#^o^)/
# Date:      2018/1/26 14:07
# Version:   v1.0.0
# CopyRight: Copyright ©Zhihao Xie, All rights reserved.

# Note: summary of vfs blastout and pie plot

import sys, re, os
from collections import OrderedDict
import pandas as pd
from matplotlib import pyplot as plt
import pyecharts.options as opts
from pyecharts.charts import Pie

def draw_barh(profix_file, out_prefix):
    
    df = pd.read_table(profix_file)
    df = df[~df['Level1'].str.contains('Others')]
    df = df.sort_values('Number')
    level1 = df.groupby('Level1')
    mean = df['Number'].mean()
    plt.figure(figsize=(16,9))
    ax = plt.subplot()
    for i, j in level1:
        _x = j['Number'].astype(int).tolist()
        _y = j['Level2']
        rects = ax.barh(_y,_x, label = i)
        n = 0
        for rect in rects:
            width = int(rect.get_width())
            height = int(rect.get_height())
            Str = _x[n]
            n += 1 
            if width < mean:
                xloc = 5
                clr = 'black'
                align = 'left'
            else:
                # Shift the text to the left side of the right edge
                xloc = -5
                # White on magenta
                clr = 'white'
                align = 'right'
            # Center the text vertically in the bar
            yloc = rect.get_y() + rect.get_height() / 2
            label = ax.annotate(Str, xy=(width, yloc), xytext=(xloc, 0),
                            textcoords="offset points",
                            ha=align, va='center',
                            color=clr, weight='bold', clip_on=True)
    plt.xlabel('Number')
    plt.legend(loc = 'best')
    plt.savefig(out_prefix+'.vf_barhplot.pdf', bbox_inches = 'tight')
    plt.savefig(out_prefix+'.vf_barhplot.png', bbox_inches = 'tight')

def draw_pie(profix_file, out_prefix):

    df = pd.read_table(profix_file)
    df = df[~df['Level1'].str.contains('Others')]

    level1 = df.groupby('Level1').agg(sum)
    inner_x_data = level1.index
    inner_y_data = level1['Number']
    inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

    outer_x_data = df['Level2'].tolist()
    outer_y_data = df['Number'].tolist()
    outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]
    (
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="Level1",
        data_pair=inner_data_pair,
        radius=["0%", "30%"],
        label_opts=opts.LabelOpts(position="inner"),
    )
    .add(
        series_name="Level2",
        radius=["40%", "70%"],
        data_pair=outer_data_pair,
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2
                },
            },
        ),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
    .render(out_prefix+'.vf.pieplot.html')
)

def main():
    if len(sys.argv) < 3:
        print("python %s <vf_bsp_out> <out_prefix>" % sys.argv[0])
        sys.exit(1)

    #VFDB_level_table = "/sdd/database/VFDB/VFDB_level_gene_link.txt"
    selfscript_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    #VFDB_level_table = os.path.join(selfscript_path, "../../database/VFDB/VFDB_level_gene_link.txt")
    VFDB_level_table = os.path.join("/run/mgjy-oss-metagenome/metaGenome_v3/database/VFDB/VFDB_level_gene_link.txt")
    if not os.path.isfile(VFDB_level_table):
        print("Error: %s don't exist.")
        sys.exit(1)

    symbol2level = {}
    gene2symbol = {}
    with open(VFDB_level_table) as fh:
        for line in fh:
            if re.match(r'Level1', line):
                continue
            fields = line.strip().split("\t")
            if fields[3] == '-' or fields[3] == "":
                continue
            symbol2level.setdefault(fields[3], set()).add("\t".join(fields[:2]))
            gene_list = re.split(r',\s*', fields[4])
            for gene in gene_list:
                if gene != "" or gene != '-':
                    gene2symbol[gene] = fields[3]

    level_sum_dict = OrderedDict()
    with open(sys.argv[1]) as fh:
        for line in fh:
            if re.search(r'^Query|No hit|^\s*$', line):
                continue
            fields = line.strip().split("\t")
            vfid = fields[2]
            vf_symbol = fields[11]
            if vf_symbol in symbol2level:
                for level in sorted(list(symbol2level[vf_symbol])):
                    level_sum_dict.setdefault(level, 0)
                    level_sum_dict[level] += 1
            elif vfid in gene2symbol:
                tmp_symbol = gene2symbol[vfid]
                if tmp_symbol in symbol2level:
                    for level in sorted(list(symbol2level[vf_symbol])):
                        level_sum_dict.setdefault(level, 0)
                        level_sum_dict[level] += 1
            else:
                level_sum_dict.setdefault('Others\tOthers', 0)
                level_sum_dict['Others\tOthers'] += 1

    out_prefix = sys.argv[2]
    with open(out_prefix+".vf_sum.txt", 'w') as outfh:
        outfh.write("Level1\tLevel2\tNumber\n")
        for level in sorted(level_sum_dict.keys()):
            if not re.search(r'^Others', level):
                outfh.write("%s\t%s\n" % (level, level_sum_dict[level]))
        if 'Others\tOthers' in level_sum_dict:
            outfh.write("Others\tOthers\t" + str(level_sum_dict['Others\tOthers']) + "\n")

    # barh plot
    sum_file = out_prefix+".vf_sum.txt"
    draw_barh(sum_file, out_prefix)
    draw_pie(sum_file, out_prefix)
if __name__ == '__main__':
    main()

