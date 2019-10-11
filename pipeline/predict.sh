source activate /sysdata/Meta/conda_envs/py374
echo 2018V3-基因预测
date

echo "$$"

mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict
cp /sysdata/Meta/pipeline/metagenome_work_out/1.clean_data/clean_reads_file.list /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/clean_reads_file.list
cp /sysdata/Meta/pipeline/metagenome_work_out/2.assembly/assemble_seq.list /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/assemble_seq.list




echo 3.1 orf prediciton processing start !!
/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time -a -o /sysdata/Meta/pipeline/metagenome_work_out/../source_results.txt -f 'Gene_prediciton %e %M' python /home/chihminchang/Metagenomics/Meta_shotgun/bin/metaGenome_v3/bin/genePredict4metaGenome.py -q /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/clean_reads_file.list -f /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/assemble_seq.list -d /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict -step 1
echo 3.1 orf prediciton processing end!!
