# Venn 图与花瓣图绘制
## 第三方库
* VennDiagram 
## 单独使用方法
``` sh
python Venn.py -i abundance_table.txt -o Venn -c All -m mapping.txt -p 30
usage: Venn.py [-h] [-i INFILE] [-o OUTFILE]
               [-c [COMBINATION [COMBINATION ...]]] [-m MAPPING] [-p CORES]

Draw Venn plot or petal plot with OTU table and grouping information

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --input INFILE
                        A tabular matrix , columns: ID, S1, S2...
  -o OUTFILE, --output OUTFILE
                        path to output directory
  -c [COMBINATION [COMBINATION ...]], --combination [COMBINATION [COMBINATION ...]]
                        combinations among different groups or samples, default All
  -m MAPPING, --mapping MAPPING
                        The mapping file for metagenome, a tabular form,
                        columns : #SampleID Condition1 SampleID
  -p CORES, --cores CORES
                        Numbers of CPUs to use
```

## 结合snakemake
```python
run:
    shell("python {script_path}/Venn.py -i {input.OTU_table} -o {output} -c {params.interact} -m {input.mapped} -p {threads} 2> {log}")
    shell('rm {output}/*.r')
    shell('rm {output}/*.list')
```
