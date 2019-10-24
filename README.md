# 宏基因组预测与注释

适用于已经质控并组装的宏基因项目

## 环境准备
### miniconda2 或miniconda3
```sh
# 安装miniconda| linux
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sh Miniconda3-latest-Linux-x86_64.sh
# miniconda 2
$ source activate /sysdata/Meta/conda_envs/py374
# miniconda 3
$ conda activate /sysdata/Meta/conda_envs/py374
```
### python3.7.4 第三方库
- pandas
- matplotlib
- Bio
- aiohttp
- BeautifulSoup
- pyecharts
- psutil
- FileUtilx(本地库)

### 配置档设置
* [metagenome_config_2taxa.txt](/pipeline/metagenome_config_2taxa.txt)

## 新特性
- [邮箱通知](./mailx.md)
- 注释效率提高8倍
- 预测效率提高1.2倍
- 预测与注释在配置档增设CPU配置
- [keggMapper.py](/script/annotation/KEGG/keggMapper.md)-异步爬取kegg数据库
- [vfdb_classsum_and_plot.py](/script/annotation/VF/vfdb_classsum_and_plot.md)-修正文字遮挡的问题
- [分序列并行化](/Lib/FileUtilx.md)

## 流程执行
```sh
# 在当前文件夹生成流程脚本 predict.sh和annotation.sh
$ python metagenome_pipeline_2taxa.py metagenome_config_2taxa.txt
# 宏基因组基因预测
$ nohup sh predict.sh > predict.log &
# 待预测完成后， 注释
$ nohup sh annotation.sh > annotation.log &
```
## 流程图
![流程图](/bpmn-with-drawio.png)

## FAQs
问：如何设置CPU和并行数量？\
答：在oss的系统配置下，为了避免内存使用超额 ，样品数超过10个的项目，每台服务器只能同时运行单个项目，cpu设置为60个。样品数少于10个的项目，每台服务器可以同时运行为两个项目，cpu设置为30个。\
剩余的资源留给售后及个性化分析。

问：如何断点运行？\
答： 样品维度的分析产出结果后，将会通过发进度表给分析人员。倘若与上次的进度表相同或进度表迟迟不发，代表运行错误，可以追踪相应的样品，跑报错的样品。其余的错误可以通过追踪log文件， python 报错关键词为raise, perl 为 at line $. 
## 结果文件
```
.
├── 1.clean_data
│   ├── CB0
│   │   ├── fastqc.out
│   │   │   ├── clean_R1_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R1_fastqc.html
│   │   │   ├── clean_R1_fastqc.zip
│   │   │   ├── clean_R2_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R2_fastqc.html
│   │   │   └── clean_R2_fastqc.zip
│   │   ├── infile
│   │   └── status.json
│   ├── CB1
│   │   ├── fastqc.out
│   │   │   ├── clean_R1_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R1_fastqc.html
│   │   │   ├── clean_R1_fastqc.zip
│   │   │   ├── clean_R2_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R2_fastqc.html
│   │   │   └── clean_R2_fastqc.zip
│   │   ├── infile
│   │   └── status.json
│   ├── CB10
│   │   ├── fastqc.out
│   │   │   ├── clean_R1_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R1_fastqc.html
│   │   │   ├── clean_R1_fastqc.zip
│   │   │   ├── clean_R2_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R2_fastqc.html
│   │   │   └── clean_R2_fastqc.zip
│   │   ├── infile
│   │   └── status.json
│   ├── Check_Process_for_Sample.txt
│   ├── Check_source_for_Sample.txt
│   ├── Check_time_for_Sample.txt
│   ├── clean_reads_file.list
│   ├── M1
│   │   ├── fastqc.out
│   │   │   ├── clean_R1_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R1_fastqc.html
│   │   │   ├── clean_R1_fastqc.zip
│   │   │   ├── clean_R2_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R2_fastqc.html
│   │   │   └── clean_R2_fastqc.zip
│   │   ├── infile
│   │   └── status.json
│   ├── M2
│   │   ├── fastqc.out
│   │   │   ├── clean_R1_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R1_fastqc.html
│   │   │   ├── clean_R1_fastqc.zip
│   │   │   ├── clean_R2_fastqc
│   │   │   │   ├── fastqc_data.txt
│   │   │   │   ├── fastqc.fo
│   │   │   │   ├── fastqc_report.html
│   │   │   │   ├── Icons
│   │   │   │   │   ├── error.png
│   │   │   │   │   ├── fastqc_icon.png
│   │   │   │   │   ├── tick.png
│   │   │   │   │   └── warning.png
│   │   │   │   ├── Images
│   │   │   │   │   ├── adapter_content.png
│   │   │   │   │   ├── duplication_levels.png
│   │   │   │   │   ├── per_base_n_content.png
│   │   │   │   │   ├── per_base_quality.png
│   │   │   │   │   ├── per_base_sequence_content.png
│   │   │   │   │   ├── per_sequence_gc_content.png
│   │   │   │   │   ├── per_sequence_quality.png
│   │   │   │   │   └── sequence_length_distribution.png
│   │   │   │   └── summary.txt
│   │   │   ├── clean_R2_fastqc.html
│   │   │   └── clean_R2_fastqc.zip
│   │   ├── infile
│   │   └── status.json
│   └── M3
│       ├── fastqc.out
│       │   ├── clean_R1_fastqc
│       │   │   ├── fastqc_data.txt
│       │   │   ├── fastqc.fo
│       │   │   ├── fastqc_report.html
│       │   │   ├── Icons
│       │   │   │   ├── error.png
│       │   │   │   ├── fastqc_icon.png
│       │   │   │   ├── tick.png
│       │   │   │   └── warning.png
│       │   │   ├── Images
│       │   │   │   ├── adapter_content.png
│       │   │   │   ├── duplication_levels.png
│       │   │   │   ├── per_base_n_content.png
│       │   │   │   ├── per_base_quality.png
│       │   │   │   ├── per_base_sequence_content.png
│       │   │   │   ├── per_sequence_gc_content.png
│       │   │   │   ├── per_sequence_quality.png
│       │   │   │   └── sequence_length_distribution.png
│       │   │   └── summary.txt
│       │   ├── clean_R1_fastqc.html
│       │   ├── clean_R1_fastqc.zip
│       │   ├── clean_R2_fastqc
│       │   │   ├── fastqc_data.txt
│       │   │   ├── fastqc.fo
│       │   │   ├── fastqc_report.html
│       │   │   ├── Icons
│       │   │   │   ├── error.png
│       │   │   │   ├── fastqc_icon.png
│       │   │   │   ├── tick.png
│       │   │   │   └── warning.png
│       │   │   ├── Images
│       │   │   │   ├── adapter_content.png
│       │   │   │   ├── duplication_levels.png
│       │   │   │   ├── per_base_n_content.png
│       │   │   │   ├── per_base_quality.png
│       │   │   │   ├── per_base_sequence_content.png
│       │   │   │   ├── per_sequence_gc_content.png
│       │   │   │   ├── per_sequence_quality.png
│       │   │   │   └── sequence_length_distribution.png
│       │   │   └── summary.txt
│       │   ├── clean_R2_fastqc.html
│       │   └── clean_R2_fastqc.zip
│       ├── infile
│       └── status.json
├── 2.assembly
│   ├── assemble_seq.list
│   ├── CB0_assemble_out
│   │   ├── covstats.txt
│   │   ├── status.json
│   │   ├── unmap_reads1.fastq.gz
│   │   └── unmap_reads2.fastq.gz
│   ├── CB10_assemble_out
│   │   ├── covstats.txt
│   │   ├── status.json
│   │   ├── unmap_reads1.fastq.gz
│   │   └── unmap_reads2.fastq.gz
│   ├── CB1_assemble_out
│   │   ├── covstats.txt
│   │   ├── status.json
│   │   ├── unmap_reads1.fastq.gz
│   │   └── unmap_reads2.fastq.gz
│   ├── M1_assemble_out
│   │   ├── covstats.txt
│   │   ├── status.json
│   │   ├── unmap_reads1.fastq.gz
│   │   └── unmap_reads2.fastq.gz
│   ├── M2_assemble_out
│   │   ├── covstats.txt
│   │   ├── status.json
│   │   ├── unmap_reads1.fastq.gz
│   │   └── unmap_reads2.fastq.gz
│   ├── M3_assemble_out
│   │   ├── covstats.txt
│   │   ├── status.json
│   │   ├── unmap_reads1.fastq.gz
│   │   └── unmap_reads2.fastq.gz
│   └── unmap_assemble_out
│       └── status.json
├── 3.gene_predict
│   ├── assemble_seq.list
│   ├── clean_reads_file.list
│   ├── Gene
│   │   ├── back_filter.log
│   │   ├── back_filter.sh
│   │   ├── CB0
│   │   │   ├── CB0.gene.ffn
│   │   │   ├── CB0.gene.gff
│   │   │   ├── CB0.length_distribution.pdf
│   │   │   ├── CB0.length_distribution.png
│   │   │   ├── CB0.length.txt
│   │   │   ├── CB0_orf_predict.log
│   │   │   ├── CB0_orf_predict.sh
│   │   │   ├── CB0.protein.faa
│   │   │   └── CB0_vs_antifam.out
│   │   ├── CB1
│   │   │   ├── CB1.gene.ffn
│   │   │   ├── CB1.gene.gff
│   │   │   ├── CB1.length_distribution.pdf
│   │   │   ├── CB1.length_distribution.png
│   │   │   ├── CB1.length.txt
│   │   │   ├── CB1_orf_predict.log
│   │   │   ├── CB1_orf_predict.sh
│   │   │   ├── CB1.protein.faa
│   │   │   └── CB1_vs_antifam.out
│   │   ├── CB10
│   │   │   ├── CB10.gene.ffn
│   │   │   ├── CB10.gene.gff
│   │   │   ├── CB10.length_distribution.pdf
│   │   │   ├── CB10.length_distribution.png
│   │   │   ├── CB10.length.txt
│   │   │   ├── CB10_orf_predict.log
│   │   │   ├── CB10_orf_predict.sh
│   │   │   ├── CB10.protein.faa
│   │   │   └── CB10_vs_antifam.out
│   │   ├── cluster_gene_count.tsv
│   │   ├── gene_catalogue.faa
│   │   ├── gene_catalogue.ffn
│   │   ├── gene_catalogue_geneFile.list
│   │   ├── gene_catalogue.length_distribution.pdf
│   │   ├── gene_catalogue.length_distribution.png
│   │   ├── gene_catalogue.length.txt
│   │   ├── gene_catalogue_proteinFile.list
│   │   ├── gene_catalogue.summary.txt
│   │   ├── gene_depth
│   │   │   ├── CB0.covstats.txt
│   │   │   ├── CB10.covstats.txt
│   │   │   ├── CB1.covstats.txt
│   │   │   ├── gene_abundance_table.txt
│   │   │   ├── gene_depth_table.txt
│   │   │   ├── M1.covstats.txt
│   │   │   ├── M2.covstats.txt
│   │   │   ├── M3.covstats.txt
│   │   │   └── ref
│   │   │       ├── genome
│   │   │       │   └── 1
│   │   │       │       ├── chr1.chrom.gz
│   │   │       │       ├── info.txt
│   │   │       │       ├── scaffolds.txt.gz
│   │   │       │       └── summary.txt
│   │   │       └── index
│   │   │           └── 1
│   │   │               ├── chr1_index_k13_c13_b1.block
│   │   │               └── chr1_index_k13_c13_b1.block2.gz
│   │   ├── M1
│   │   │   ├── M1.gene.ffn
│   │   │   ├── M1.gene.gff
│   │   │   ├── M1.length_distribution.pdf
│   │   │   ├── M1.length_distribution.png
│   │   │   ├── M1.length.txt
│   │   │   ├── M1_orf_predict.log
│   │   │   ├── M1_orf_predict.sh
│   │   │   ├── M1.protein.faa
│   │   │   └── M1_vs_antifam.out
│   │   ├── M2
│   │   │   ├── M2.gene.ffn
│   │   │   ├── M2.gene.gff
│   │   │   ├── M2.length_distribution.pdf
│   │   │   ├── M2.length_distribution.png
│   │   │   ├── M2.length.txt
│   │   │   ├── M2_orf_predict.log
│   │   │   ├── M2_orf_predict.sh
│   │   │   ├── M2.protein.faa
│   │   │   └── M2_vs_antifam.out
│   │   ├── M3
│   │   │   ├── M3.gene.ffn
│   │   │   ├── M3.gene.gff
│   │   │   ├── M3.length_distribution.pdf
│   │   │   ├── M3.length_distribution.png
│   │   │   ├── M3.length.txt
│   │   │   ├── M3_orf_predict.log
│   │   │   ├── M3_orf_predict.sh
│   │   │   ├── M3.protein.faa
│   │   │   └── M3_vs_antifam.out
│   │   ├── predict_1.log
│   │   ├── predict_1.sh
│   │   ├── predict_2.log
│   │   ├── predict_2.sh
│   │   ├── predict_3.log
│   │   ├── predict_3.sh
│   │   ├── predict_gene.list
│   │   ├── predict_gene.summary.txt
│   │   ├── predict_protein.list
│   │   ├── query_linclust_cluster.tsv
│   │   ├── unigenes_cluster.table.txt
│   │   └── unmap_samples
│   │       ├── unmap_samples.gene.ffn
│   │       ├── unmap_samples.gene.gff
│   │       ├── unmap_samples.length_distribution.pdf
│   │       ├── unmap_samples.length_distribution.png
│   │       ├── unmap_samples.length.txt
│   │       ├── unmap_samples_orf_predict.log
│   │       ├── unmap_samples_orf_predict.sh
│   │       ├── unmap_samples.protein.faa
│   │       └── unmap_samples_vs_antifam.out
│   ├── ncRNA
│   │   ├── all_samples_ncRNA_summary.txt
│   │   ├── CB0
│   │   │   ├── CB0.arc.rRNA.fasta
│   │   │   ├── CB0.arc.rRNA.gff
│   │   │   ├── CB0.bac.rRNA.fasta
│   │   │   ├── CB0.bac.rRNA.gff
│   │   │   ├── CB0.euk.rRNA.fasta
│   │   │   ├── CB0.euk.rRNA.gff
│   │   │   ├── CB0.ncRNA_summary.txt
│   │   │   ├── CB0.rRNA.fasta
│   │   │   ├── CB0.tmRNA.fasta
│   │   │   ├── rna_cmd.log
│   │   │   └── rna_cmd.sh
│   │   ├── CB1
│   │   │   ├── CB1.arc.rRNA.fasta
│   │   │   ├── CB1.arc.rRNA.gff
│   │   │   ├── CB1.bac.rRNA.fasta
│   │   │   ├── CB1.bac.rRNA.gff
│   │   │   ├── CB1.euk.rRNA.fasta
│   │   │   ├── CB1.euk.rRNA.gff
│   │   │   ├── CB1.ncRNA_summary.txt
│   │   │   ├── CB1.rRNA.fasta
│   │   │   ├── CB1.tmRNA.fasta
│   │   │   ├── rna_cmd.log
│   │   │   └── rna_cmd.sh
│   │   ├── CB10
│   │   │   ├── CB10.arc.rRNA.fasta
│   │   │   ├── CB10.arc.rRNA.gff
│   │   │   ├── CB10.bac.rRNA.fasta
│   │   │   ├── CB10.bac.rRNA.gff
│   │   │   ├── CB10.euk.rRNA.fasta
│   │   │   ├── CB10.euk.rRNA.gff
│   │   │   ├── CB10.ncRNA_summary.txt
│   │   │   ├── CB10.rRNA.fasta
│   │   │   ├── CB10.tmRNA.fasta
│   │   │   ├── rna_cmd.log
│   │   │   └── rna_cmd.sh
│   │   ├── M1
│   │   │   ├── M1.arc.rRNA.fasta
│   │   │   ├── M1.arc.rRNA.gff
│   │   │   ├── M1.bac.rRNA.fasta
│   │   │   ├── M1.bac.rRNA.gff
│   │   │   ├── M1.euk.rRNA.fasta
│   │   │   ├── M1.euk.rRNA.gff
│   │   │   ├── M1.ncRNA_summary.txt
│   │   │   ├── M1.rRNA.fasta
│   │   │   ├── M1.tmRNA.fasta
│   │   │   ├── rna_cmd.log
│   │   │   └── rna_cmd.sh
│   │   ├── M2
│   │   │   ├── M2.arc.rRNA.fasta
│   │   │   ├── M2.arc.rRNA.gff
│   │   │   ├── M2.bac.rRNA.fasta
│   │   │   ├── M2.bac.rRNA.gff
│   │   │   ├── M2.euk.rRNA.fasta
│   │   │   ├── M2.euk.rRNA.gff
│   │   │   ├── M2.ncRNA_summary.txt
│   │   │   ├── M2.rRNA.fasta
│   │   │   ├── M2.tmRNA.fasta
│   │   │   ├── rna_cmd.log
│   │   │   └── rna_cmd.sh
│   │   ├── M3
│   │   │   ├── M3.arc.rRNA.fasta
│   │   │   ├── M3.arc.rRNA.gff
│   │   │   ├── M3.bac.rRNA.fasta
│   │   │   ├── M3.bac.rRNA.gff
│   │   │   ├── M3.euk.rRNA.fasta
│   │   │   ├── M3.euk.rRNA.gff
│   │   │   ├── M3.ncRNA_summary.txt
│   │   │   ├── M3.rRNA.fasta
│   │   │   ├── M3.tmRNA.fasta
│   │   │   ├── rna_cmd.log
│   │   │   └── rna_cmd.sh
│   │   ├── predict_rna_final.log
│   │   ├── predict_rna_final.sh
│   │   ├── predict_rna.log
│   │   ├── predict_rna.sh
│   │   └── unmap_samples
│   │       ├── rna_cmd.log
│   │       ├── rna_cmd.sh
│   │       ├── unmap_samples.arc.rRNA.fasta
│   │       ├── unmap_samples.arc.rRNA.gff
│   │       ├── unmap_samples.bac.rRNA.fasta
│   │       ├── unmap_samples.bac.rRNA.gff
│   │       ├── unmap_samples.euk.rRNA.fasta
│   │       ├── unmap_samples.euk.rRNA.gff
│   │       ├── unmap_samples.ncRNA_summary.txt
│   │       ├── unmap_samples.rRNA.fasta
│   │       └── unmap_samples.tmRNA.fasta
│   └── predict.log
├── 4.annotation
│   ├── annotate_task_cmd.sh
│   ├── gene_abundance_table.txt
│   ├── gene_catalogue.faa
│   └── Unigenes
│       ├── AR
│       │   ├── ardb_annotation.sh
│       │   ├── ar_high.log
│       │   ├── ar_high.sh
│       │   ├── error.log
│       │   ├── genomeList.tab
│       │   ├── Unigenes.ardb.bltOut.txt
│       │   ├── Unigenes_ardb_class_count.txt
│       │   ├── Unigenes.ardb.output.txt
│       │   ├── Unigenes.bacmet.bacmet.report.temp
│       │   ├── Unigenes.bacmet.counts
│       │   ├── Unigenes.bacmet.daa
│       │   ├── Unigenes.bacmet.matrix
│       │   ├── Unigenes.bacmet.report
│       │   ├── Unigenes.bacmet.table
│       │   ├── Unigenes.bacmet.toplist
│       │   └── Unigenes.blastp
│       ├── CAZy
│       │   ├── cazy_annotation.log
│       │   ├── cazy_annotation.sh
│       │   ├── cazy_high.log
│       │   ├── cazy_high.sh
│       │   ├── CAZyme_out.txt
│       │   ├── cazyme_summary.xls
│       │   ├── gene_catalogue.faa.cut
│       │   │   ├── gene_catalogue.faa.1
│       │   │   ├── gene_catalogue.faa.10
│       │   │   ├── gene_catalogue.faa.11
│       │   │   ├── gene_catalogue.faa.12
│       │   │   ├── gene_catalogue.faa.13
│       │   │   ├── gene_catalogue.faa.14
│       │   │   ├── gene_catalogue.faa.15
│       │   │   ├── gene_catalogue.faa.16
│       │   │   ├── gene_catalogue.faa.17
│       │   │   ├── gene_catalogue.faa.18
│       │   │   ├── gene_catalogue.faa.19
│       │   │   ├── gene_catalogue.faa.2
│       │   │   ├── gene_catalogue.faa.20
│       │   │   ├── gene_catalogue.faa.3
│       │   │   ├── gene_catalogue.faa.4
│       │   │   ├── gene_catalogue.faa.5
│       │   │   ├── gene_catalogue.faa.6
│       │   │   ├── gene_catalogue.faa.7
│       │   │   ├── gene_catalogue.faa.8
│       │   │   └── gene_catalogue.faa.9
│       │   ├── Unigenes_abundance_cazyFunc.tsv
│       │   ├── Unigenes.CAZyme.class.pdf
│       │   ├── Unigenes.CAZyme.class.png
│       │   ├── Unigenes.CAZyme.class.txt
│       │   └── Unigenes.CAZyme.txt
│       ├── eggNOG
│       │   ├── eggNOG_annotation.log
│       │   ├── eggNOG_annotation.sh
│       │   ├── nog_high.log
│       │   ├── nog_high.sh
│       │   ├── Unigenes_abundance_nogFunc.tsv
│       │   ├── Unigenes.all_catalog.xls
│       │   ├── Unigenes.all_class.pdf
│       │   ├── Unigenes.all_class.png
│       │   ├── Unigenes.all_class.xls
│       │   ├── Unigenes.all_func_desc.xls
│       │   ├── Unigenes.all_og_count.xls
│       │   └── Unigenes.nog_blast_out.txt
│       ├── KEGG
│       │   ├── gene2ko.txt
│       │   ├── gene_vs_kegg_annotation.xls
│       │   ├── kegg_annotation.log
│       │   ├── kegg_annotation.sh
│       │   ├── kegg_high.log
│       │   ├── kegg_high.sh
│       │   ├── ko_sum.txt
│       │   ├── ko_sum.xls
│       │   ├── Level1.stats.pdf
│       │   ├── Level1.stats.png
│       │   ├── Level1.xls
│       │   ├── Level2.stats.pdf
│       │   ├── Level2.stats.png
│       │   ├── Level2.xls
│       │   ├── Level3.stats.pdf
│       │   ├── Level3.stats.png
│       │   ├── Level3.xls
│       │   ├── Map
│       │   │   ├── map00051.args
│       │   │   ├── map00051.png
│       │   │   ├── map00190.args
│       │   │   ├── map00190.png
│       │   │   ├── map00220.args
│       │   │   ├── map00220.png
│       │   │   ├── map00330.args
│       │   │   ├── map00330.png
│       │   │   ├── map00400.args
│       │   │   ├── map00400.png
│       │   │   ├── map00473.args
│       │   │   ├── map00473.png
│       │   │   ├── map00480.args
│       │   │   ├── map00480.png
│       │   │   ├── map00500.args
│       │   │   ├── map00500.png
│       │   │   ├── map00520.args
│       │   │   ├── map00520.png
│       │   │   ├── map00620.args
│       │   │   ├── map00620.png
│       │   │   ├── map00780.args
│       │   │   ├── map00780.png
│       │   │   ├── map00790.args
│       │   │   ├── map00790.png
│       │   │   ├── map01100.args
│       │   │   ├── map01100.png
│       │   │   ├── map01110.args
│       │   │   ├── map01110.png
│       │   │   ├── map01120.args
│       │   │   ├── map01120.png
│       │   │   ├── map01130.args
│       │   │   ├── map01130.png
│       │   │   ├── map01230.args
│       │   │   ├── map01230.png
│       │   │   ├── map01502.args
│       │   │   ├── map01502.png
│       │   │   ├── map02010.args
│       │   │   ├── map02010.png
│       │   │   ├── map03010.args
│       │   │   ├── map03010.png
│       │   │   ├── map03018.args
│       │   │   ├── map03018.png
│       │   │   ├── map03020.args
│       │   │   ├── map03020.png
│       │   │   ├── map03070.args
│       │   │   ├── map03070.png
│       │   │   ├── map03430.args
│       │   │   ├── map03430.png
│       │   │   ├── map04112.args
│       │   │   ├── map04112.png
│       │   │   ├── map04212.args
│       │   │   ├── map04212.png
│       │   │   ├── map04918.args
│       │   │   ├── map04918.png
│       │   │   ├── map05146.args
│       │   │   ├── map05146.png
│       │   │   └── requests.html
│       │   ├── Unigenes_abundance_keggFunc.tsv
│       │   └── Unigenes_vs_kegg_blt.txt
│       ├── NR
│       │   ├── nr_annotation.sh
│       │   ├── nr_high.log
│       │   ├── nr_high.sh
│       │   ├── Unigenes_abundance_nrFunc.tsv
│       │   ├── Unigenes.annotations.nr.txt
│       │   ├── Unigenes_gene_nr.txt
│       │   └── Unigenes_vs_nr_fortaxa.txt
│       ├── PHI
│       │   ├── phi_annotation.log
│       │   ├── phi_annotation.sh
│       │   ├── phi_high.log
│       │   ├── phi_high.sh
│       │   ├── Unigenes_abundance_phiFunc.tsv
│       │   ├── Unigenes.phi.annotation.tsv
│       │   └── Unigenes_vs_phi.blt.tsv
│       ├── TCDB
│       │   ├── tcdb_annotation.log
│       │   ├── tcdb_annotation.sh
│       │   ├── tcdb_high.log
│       │   ├── tcdb_high.sh
│       │   ├── Unigenes_abundance_tcdbFunc.tsv
│       │   ├── Unigenes.tcdb.annotation.txt
│       │   └── Unigenes_vs_tcdb.bsp
│       └── VF
│           ├── Unigenes_abundance_vfFunc.tsv
│           ├── Unigenes.vf_barhplot.pdf
│           ├── Unigenes.vf_barhplot.png
│           ├── Unigenes.vf.pieplot.html
│           ├── Unigenes.VFs.tsv
│           ├── Unigenes.vf_sum.txt
│           ├── vf_annotation.log
│           ├── vf_annotation.sh
│           ├── vf_high.log
│           └── vf_high.sh
├── 5.taxa
│   ├── clean_reads_file.list
│   ├── common_taxonomic
│   │   ├── gene_taxa_relative_abundance.txt
│   │   ├── Krona
│   │   │   ├── CB0_Krona_taxa.txt
│   │   │   ├── CB10_Krona_taxa.txt
│   │   │   ├── CB1_Krona_taxa.txt
│   │   │   ├── krona.log
│   │   │   ├── krona.sh
│   │   │   ├── Krona_taxonomy_profile.html
│   │   │   ├── M1_Krona_taxa.txt
│   │   │   ├── M2_Krona_taxa.txt
│   │   │   └── M3_Krona_taxa.txt
│   │   ├── nr_blast_out.m8 -> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/Unigenes_vs_nr_fortaxa.txt
│   │   ├── nr_blast_out.m8.tax
│   │   ├── nr_blast_out.m8.tax.table
│   │   ├── run_nr_taxa.log
│   │   └── run_nr_taxa.sh
│   ├── gene_abundance_table.txt -> /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/Gene/gene_depth/gene_abundance_table.txt
│   ├── gene_catalogue.faa -> /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/Gene/gene_catalogue.faa
│   ├── metaphlan2_taxonomic
│   │   ├── CB0.bowtie2.bz2
│   │   ├── CB0.krona.txt
│   │   ├── CB0.taxa_profile.txt
│   │   ├── CB10.bowtie2.bz2
│   │   ├── CB10.krona.txt
│   │   ├── CB10.taxa_profile.txt
│   │   ├── CB1.bowtie2.bz2
│   │   ├── CB1.krona.txt
│   │   ├── CB1.taxa_profile.txt
│   │   ├── Krona_taxa_profile.html
│   │   ├── lefse
│   │   │   ├── Condition1
│   │   │   │   ├── biomarkers_images
│   │   │   │   ├── merged.lefseInput.txt
│   │   │   │   ├── run_lefse.log
│   │   │   │   └── run_lefse.sh
│   │   │   └── Condition2
│   │   │       ├── biomarkers_images
│   │   │       ├── merged.lefseInput.txt
│   │   │       ├── run_lefse.log
│   │   │       └── run_lefse.sh
│   │   ├── M1.bowtie2.bz2
│   │   ├── M1.krona.txt
│   │   ├── M1.taxa_profile.txt
│   │   ├── M2.bowtie2.bz2
│   │   ├── M2.krona.txt
│   │   ├── M2.taxa_profile.txt
│   │   ├── M3.bowtie2.bz2
│   │   ├── M3.krona.txt
│   │   ├── M3.taxa_profile.txt
│   │   ├── merged_abundance_table.txt
│   │   ├── metaphlan2_taxa.log
│   │   ├── run_metaphlan2_taxa.log
│   │   └── run_metaphlan2_taxa.sh
│   └── Unigenes_vs_nr_fortaxa.txt
└── sample_groups_info
    ├── Condition1
    │   ├── sample_Condition1.tsv
    │   └── sample_ids.tsv
    ├── Condition2
    │   ├── sample_Condition2.tsv
    │   └── sample_ids.tsv
    ├── sample_Condition1.tsv
    ├── sample_Condition2.tsv
    ├── sample_ids.tsv
    └── sample_SampleID.tsv

104 directories, 667 files
```
