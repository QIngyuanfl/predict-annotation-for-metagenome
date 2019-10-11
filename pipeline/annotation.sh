echo 4.annotation processing start
echo 2018V3-物种及功能注释
date


source activate /home/chihminchang/miniconda2/envs/py365v2
mkdir /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation
mkdir /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/3.gene_predict/Gene/gene_catalogue.faa /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/3.gene_predict/Gene/gene_depth/gene_abundance_table.txt /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt


export MPLBACKEND="Agg"
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n nr -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd_nr.sh
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n phi -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n kegg -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n nog -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n cazy -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n ar -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n vf -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh
echo python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/geneAnnotate4metaGenome.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_catalogue.faa -g Unigenes -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes -n tcdb -t 20 -e 1e-10 -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/gene_abundance_table.txt >> /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh


nohup python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/multiTask_to_run.py /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd_nr.sh 1 &
nohup python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/script/multiTask_to_run.py /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/annotate_task_cmd.sh 3 &


echo 4.annotation processing end !!


while true
do
if [ -f "/home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes/NR/Unigenes_abundance_nrFunc.tsv" ] && [ -f "/home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes/NR/Unigenes.annotations.nr.txt" ] && [ -f "/home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes/NR/Unigenes_gene_nr.txt" ] && [ -f "/home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes/NR/Unigenes_vs_nr_fortaxa.txt" ];then
echo "NR annotation completed !"
break
else
sleep 10
echo "NR annotation processing"
fi
echo 5.taxa processing start
echo 2018V3-后续分析
date


mkdir /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa
mkdir /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/common_taxonomic
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/3.gene_predict/Gene/gene_catalogue.faa /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/gene_catalogue.faa
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/3.gene_predict/Gene/gene_depth/gene_abundance_table.txt /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/gene_abundance_table.txt
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/4.annotation/Unigenes/NR/Unigenes_vs_nr_fortaxa.txt /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/Unigenes_vs_nr_fortaxa.txt
/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time -a -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/../source_results.txt -f 'taxa-nr %e %M' python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/gene_nr_taxonomies.py -p /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/gene_catalogue.faa -n /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/Unigenes_vs_nr_fortaxa.txt -a /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/gene_abundance_table.txt -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/common_taxonomic


mkdir /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/metaphlan2_taxonomic
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/1.clean_data/clean_reads_file.list /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/clean_reads_file.list
mkdir /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition1
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/sample_Condition1.tsv /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition1/.
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/sample_ids.tsv /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition1/.
/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time -a -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/../source_results.txt -f 'taxa-metaphlan2-Condition1 %e %M' python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/metaphlan2_taxonomies.py -q /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/clean_reads_file.list -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/metaphlan2_taxonomic -g /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition1
mkdir /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition2
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/sample_Condition2.tsv /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition2/.
cp /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/sample_ids.tsv /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition2/.
/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time -a -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/../source_results.txt -f 'taxa-metaphlan2-Condition2 %e %M' python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/metaphlan2_taxonomies.py -q /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/clean_reads_file.list -o /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/5.taxa/metaphlan2_taxonomic -g /home/chihminchang/Metagenomics/Meta_shotgun/workspace/V3_pipeline/metagenome_work_out/sample_groups_info/Condition2


