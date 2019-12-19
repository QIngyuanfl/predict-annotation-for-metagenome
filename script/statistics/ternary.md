# 三元相图绘制
## 第三方库
* r-ggtern
* pandas
## 单独使用方法
```sh
usage: ternary_plot.py [-h] [-i INFILE [INFILE ...]] [-o OUTDIR]
                       [-c [COMBINATION [COMBINATION ...]]] [-m MAPPING]
                       [-p CORES] [--top TOP]

Draw ternary plot with OTU table and grouping information

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE [INFILE ...], --input INFILE [INFILE ...]
                        A tabular matrix , columns: ID, S1, S2...
  -o OUTDIR, --output OUTDIR
                        path to output directory
  -c [COMBINATION [COMBINATION ...]], --combination [COMBINATION [COMBINATION ...]]
                        combinations among different groups or samples
  -m MAPPING, --mapping MAPPING
                        The mapping file for metagenome, a tabular form,
                        columns : #SampleID Condition1 SampleID
  -p CORES, --cores CORES
                        Numbers of CPUs to use
  --top TOP             top N abundance table to draw ternary plot
  ```
  ## 注意事项
  * 输入文件可以为多个丰度表，因为输出文件命名与丰度表的表头相关，因此丰度表第一行第一列必须有所差别才能不会覆盖输出文件。