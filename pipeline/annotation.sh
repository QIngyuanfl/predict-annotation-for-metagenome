echo 4.annotation processing start
echo 2018V3-物种及功能注释
date


source activate /sysdata/Meta/conda_envs/py374
nohup python /sysdata/Meta/script/monitor.py $$ &
mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/4.annotation
mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/Unigenes
cp /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/Gene/gene_catalogue.faa /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa
cp /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/Gene/gene_depth/gene_abundance_table.txt /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt


export MPLBACKEND="Agg"
echo python /sysdata/Meta/script/annotation/geneAnnotate4metaGenome.py -p /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/Unigenes -n nr,vf,ar,tcdb,phi,cazy,nog,kegg -t 20 -m 3 -e 1e-10 -a /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt > /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh


sh  /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh


echo 4.annotation processing end !!




echo 5.taxa processing start
echo 2018V3-后续分析
date


mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/5.taxa
mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/common_taxonomic
ln -s /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/Gene/gene_catalogue.faa /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/gene_catalogue.faa
ln -s /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/Gene/gene_depth/gene_abundance_table.txt /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/gene_abundance_table.txt
ln -s /sysdata/Meta/pipeline/metagenome_work_out/4.annotation/Unigenes/NR/Unigenes_vs_nr_fortaxa.txt /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/Unigenes_vs_nr_fortaxa.txt
python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/gene_nr_taxonomies.py -p /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/gene_catalogue.faa -n /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/Unigenes_vs_nr_fortaxa.txt -a /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/gene_abundance_table.txt -o /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/common_taxonomic


mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/metaphlan2_taxonomic
cp /sysdata/Meta/pipeline/metagenome_work_out/1.clean_data/clean_reads_file.list /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/clean_reads_file.list
mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition1
cp /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/sample_Condition1.tsv /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition1/.
cp /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/sample_ids.tsv /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition1/.
python /sysdata/Meta/script/annotation/metaphlan/metaphlan2_taxonomies.py -q /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/clean_reads_file.list -o /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/metaphlan2_taxonomic -g /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition1 -t 60
mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition2
cp /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/sample_Condition2.tsv /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition2/.
cp /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/sample_ids.tsv /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition2/.
python /sysdata/Meta/script/annotation/metaphlan/metaphlan2_taxonomies.py -q /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/clean_reads_file.list -o /sysdata/Meta/pipeline/metagenome_work_out/5.taxa/metaphlan2_taxonomic -g /sysdata/Meta/pipeline/metagenome_work_out/sample_groups_info/Condition2 -t 60


python /sysdata/Meta/script/sampleUtility.py Check_utility_for_sample.txt metagenome_config_2taxa.txt
chmod -R 777 *
