\# ==  宏基因组流程的参数配置檔案 ==

\# @@ input @@

\#== Project information ==

name: DonaldTrump 

client: 美格生物研究院

item_number: MGBJ20180504A2196C-2N

total_samples: 6

year: 2018

month: 10

day: 10

\# == alert mail address ==

mail_address: no_reply@none.com

\# ==Disk_threshold(int G) Move?(T/F) ==

Disk_threshold: 0

Is_move2StorePath: T


\# == current & fastq & mapping file location ==

current_location: /sysdata/Meta/pipeline

Fastq_location: /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/raw_fq/

mapping_file: /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/mapping.txt

\# == The name for fastq & mapping file== (\#ID 開頭不要數字)

Sample_id: CB0 CB10 CB1 M1 M2 M3

Sample_id_2: CB0 CB10 CB1 M1 M2 M3

is_complete: True

\# == the common name for R1&R2 fastq ==

R1R2_common: .R1.fq.gz .R2.fq.gz


\# == the name of mapping file == (Category 開頭不要數字, 請都在mappingfile最後一欄加上SampleID, 如沒分組請在mapping_category_id: SampleID，並於N_conditions:後加上樣本個數)

mapping_category_id: Condition1 Condition2

N_conditions: 3 2

\#mapping_category_id: Condition1 Condition2 SampleID

\#N_conditions: 3 2 6

\# == output location ==

Output: /sysdata/Meta/pipeline/metagenome_work_out

Clean_Output: /sysdata/Meta/pipeline/分析结果

do_P2W_ios: do_P2W_ios.sh

do_P2W_windows: do_P2W_windows.sh

Project_store_path: /run/mgjy-metagenome-project-store/test_space/metagenome_work_out

\# bin enviroment

\#Meta_shotgun: /home/chihminchang/miniconda2/envs/Meta-shotgun_test

\#Meta_R: /home/chihminchang/miniconda2/envs/Meta-R2

Meta_py3: /sysdata/Meta/conda_envs/py374

\# bin of clean and preduce the report!

**metagenome_clean: /sysdata/Meta/script/metagenome_clean.py**

metagenome_clean_sig: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/metagenome_clean_sig_20181109.py

\# == bin ==

All_bin: /sdd/pipeline/metaGenome_v3/bin/

readsQC4metaGenome: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/readsQC4metaGenome.py

assemble4metaGenome: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/assemble4metaGenome.py

genePredict4metaGenome: /sysdata/Meta/script/predict/genePredict4metaGenome.py

geneAnnotate4metaGenome: /sysdata/Meta/script/annotation/geneAnnotate4metaGenome.py

gene_nr_taxonomies: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/gene_nr_taxonomies.py

split_sample_group: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/split_sample_group.py

**metaphlan2_taxonomies:/sysdata/Meta/script/annotation/metaphlan/metaphlan2_taxonomies.py**

beta_format: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/beta_format.r

beta_nofactors_format: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/beta_nofactors_format.r

merge_metaphlan_tables: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_env/metaphlan2/utils/merge_metaphlan_tables.py 

**metaphlan_hclust_heatmap: /sysdata/Meta/script/annotation/metaphlan/metaphlan_hclust_heatmap.py**

ktImportRDP: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_env/Krona/KronaTools/bin/ktImportRDP

\# == script ==

All_script: /sdd/pipeline/metaGenome_v3/script/

monitor: /sysdata/Meta/script/monitor.py

sampleUtility: /sysdata/Meta/script/sampleUtility.py
**sum_nr_abundance: /sysdata/Meta/script/annotation/NR/sum_nr_abundance.py**
**sum_metaphlan_abundance: /sysdata/Meta/script/annotation/metaphlan/sum_metaphlan_abundance.py**

multiTask_to_run: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/multiTask_to_run.py

summarize_taxa_x: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/summarize_taxa_x.py

diff_level_taxa_abundance_summary: 

/home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/diff_level_taxa_abundance_summary.py

multi_taxa_barplot: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/multi_taxa_barplot.pl

taxa_heatmap_plot: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/taxa_heatmap_plot.pl

taxa_heatmap_plot_means: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/taxa_heatmap_plot_means.pl

extract_topNum_table: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/extract_topNum_table.py

bubble_plot: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/bubble_plot.R

deleteTaxonColumn: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/deleteTaxonColumn.py

spearman_correlation: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/spearman_correlation.R

ternary_list: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/ternary_list.R

ternaryplot: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/ternaryplot.pl

UPGMA_tree_plot_L2: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_L2.sh

UPGMA_tree_plot_L3: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_L3.sh

UPGMA_tree_plot_L4: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_L4.sh

UPGMA_tree_plot_L5: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_L5.sh

UPGMA_tree_plot_L6: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_L6.sh

UPGMA_tree_plot_L7: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_L7.sh

species_env_corr_heatmap: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/species_env_corr_heatmap.pl

draw_VPA_L2: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_L2.py

draw_VPA_L3: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_L3.py

draw_VPA_L4: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_L4.py

draw_VPA_L5: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_L5.py

draw_VPA_L6: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_L6.py

draw_VPA_L7: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_L7.py

sum_keggFunc_abundance: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/sum_keggFunc_abundance.py

sum_eggNOGFunc_abundance: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/sum_eggNOGFunc_abundance.py

sum_cazyFunc_abundance: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/sum_cazyFunc_abundance.py

PCA_format: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/PCA_format.r

Venn_format: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/Venn_format.r

sig_wilcoxon_format: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/sig_wilcoxon_format.r

sig_ttest_format: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/sig_ttest_format.r

format_input: /sdd/userLogin/xiezh/biosoft/LEfSE/format_input.py

run_lefse: /sdd/userLogin/xiezh/biosoft/LEfSE/run_lefse.py

plot_res: /sdd/userLogin/xiezh/biosoft/LEfSE/plot_res.py

plot_cladogram: /sdd/userLogin/xiezh/biosoft/LEfSE/plot_cladogram.py

plot_features: /sdd/userLogin/xiezh/biosoft/LEfSE/plot_features.py

jar_location: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/jar/

java_location: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/java/

\# 新增待驗證

draw_fuctionClass_barplot: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/draw_fuctionClass_barplot.pl

mean_sd: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/mean_sd.pl

uniq_group_list: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/uniq_group_list.sh

draw_heatmap: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/draw_heatmap.pl

UPGMA_tree_plot_kegg_ko: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_kegg_ko.sh

UPGMA_tree_plot_kegg_L1: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_kegg_L1.sh

UPGMA_tree_plot_kegg_L2: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_kegg_L2.sh

UPGMA_tree_plot_kegg_L3: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_kegg_L3.sh

draw_VPA_kegg_ko: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_kegg_ko.py

draw_VPA_kegg_L1: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_kegg_L1.py

draw_VPA_kegg_L2: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_kegg_L2.py

draw_VPA_kegg_L3: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_kegg_L3.py

\#nog

UPGMA_tree_plot_nog_L1: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_nog_L1.sh

UPGMA_tree_plot_nog_L2: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_nog_L2.sh

draw_VPA_nog_L1: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_nog_L1.py

draw_VPA_nog_L2: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_nog_L2.py

\#cazy

UPGMA_tree_plot_cazy_L1: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_cazy_L1.sh

UPGMA_tree_plot_cazy_family: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/UPGMA_tree_plot_cazy_family.sh

draw_VPA_cazy_L1: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_cazy_L1.py

draw_VPA_cazy_family: /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin_add/draw_VPA_cazy_family.py

\# 結題報告模板與輸出
**template_dir: /sysdata/Meta/template**
**template_oo: /sysdata/Meta/template/【美格基因】宏基因组结题报告模板-V3_oo.docx**
**template_oo_id: 【美格基因】宏基因组结题报告模板-V3_oo.docx**
**template_xo: /sysdata/Meta/template/【美格基因】宏基因组结题报告模板-V3_xo.docx**
**template_xo_id: 【美格基因】宏基因组结题报告模板-V3_xo.docx**
**template_ox: /sysdata/Meta/template/【美格基因】宏基因组结题报告模板-V3_ox.docx**
**template_ox_id: 【美格基因】宏基因组结题报告模板-V3_ox.docx**
**template_xx: /sysdata/Meta/template/【美格基因】宏基因组结题报告模板-V3_xx.docx**
**template_xx_id: 【美格基因】宏基因组结题报告模板-V3_xx.docx**
**template_s1: /sysdata/Meta/template/【美格基因】宏基因组结题报告模板-V3_s1.docx**
**template_s1_id: 【美格基因】宏基因组结题报告模板-V3_s1.docx**
**template_s2: /sysdata/Meta/template/【美格基因】宏基因组结题报告模板-V3_s2.docx**
**template_s2_id: 【美格基因】宏基因组结题报告模板-V3_s2.docx**
**Report_id: 【美格基因】宏基因组结题报告.docx**

/
\#\# [ 1. trimming 參數 ]

\# -m; 使用何种trim工具，默认是trimmomatic，可支持fastp

\# -t; params of Trimmomatic, default is "LEADING:3 TRAILING:3 SLIDINGWINDOW:5:20 MINLEN:50"

trim_method: trimmomatic

trim_param: LEADING:3 TRAILING:3 SLIDINGWINDOW:5:20 MINLEN:50 -phred33

\#trim_method: fastp

\#trim_param: -5 -W -q 15 -u 40 --thread 1 -l 50

\# 并行数(int)

trim_parallel: 3

\# -l; 长度过滤的阈值，单位为bp，默认是50

length_cutoff: 50

\# -u; 对clean data是否做uniq。[T/F]

uniq: T

\# -g; 是否去除宿主序列. 如果需要去除宿主序列，则提供宿主基因组的mapping文件(SampleID	host_path),如果沒有請標註"None"

host_genome: None

\#\# [ 2. assembly 參數 ]/
\# -m; 拼接策略，分为个体拼接(Single)和混合拼接(Mix)和按组拼接(By:Condition1) By:为固定写法后接组名，此时需要mapping文件

model: Singl

\#model: Mix

\#model: By:Condition1

\# -t; 使用何种拼接工具，默认是megahit，可支持idba spades meta_platanus megahit/
assembly_parallel: 1

assembly_method: megahit

assembly_param: --k-min 35 --k-max 95 --k-step 20 -t 25 -m 0.8

\#assembly_method: metaspades

\#assembly_param: --meta -k 35,55,75,95 -t 8 -m 100

\# --length; contigs length threshold

contig_length: 500

/
\#\# [ 3. gene_predict 參數 ]

**predict_core: 12**

\#\# [ 4. annotation 參數 ]

\# -n; 基因注释的内容，默认是"nr,kegg,nog,cazy,ar,vf,pfam,tcdb,secretion"

\# 因为后续需要到NCBI-NR比对结果，所以content必须保留nr

content: nr,kegg,vf,ar,tcdb,phi,cazy,nog

\#content: nr,phi,kegg,nog,cazy,ar,vf,pfam,tcdb,secretion

\# organism type (gram+, gram-) for secretion predict

cell_type: gram+

\# -e; e-value about blast alignments

evalue: 1e-10

\# -t; number of threads to use in the BLAST search

**threads_per_task: 20**

\# parallel task number

**task_number: 3**

/
\#\# [ 6. taxa_statistics 參數 ]

[cca&rda]

\# path to the environment/other factors file. (The sample number must more than environment factor number!) ; 如果沒有請標註"None, 且檔名請固定"factors.txt"/
factors_file: None

\#factors_file: /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/factors.txt/

