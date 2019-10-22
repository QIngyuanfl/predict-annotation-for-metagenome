source activate /sysdata/Meta/conda_envs/py374
echo 2018V3-基因预测
date


nohup python /sysdata/Meta/script/monitor.py $$ &
mkdir -p /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict
cp /sysdata/Meta/pipeline/metagenome_work_out/1.clean_data/clean_reads_file.list /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/clean_reads_file.list
cp /sysdata/Meta/pipeline/metagenome_work_out/2.assembly/assemble_seq.list /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/assemble_seq.list




echo 3.1 orf prediciton processing start !!
python /sysdata/Meta/script/predict/genePredict4metaGenome.py -q /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/clean_reads_file.list -f /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/assemble_seq.list -d /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict --step 1 -t 12
echo 3.1 orf prediciton processing end!!
echo 3.2 gene catalogue processing start!!
python /sysdata/Meta/script/predict/genePredict4metaGenome.py -q /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/clean_reads_file.list -f /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/assemble_seq.list -d /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict --step 2 -t 12
echo 3.2 gene catalogue processing end!!
echo 3.3 gene depth processing start!!
python /sysdata/Meta/script/predict/genePredict4metaGenome.py -q /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/clean_reads_file.list -f /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict/assemble_seq.list -d /sysdata/Meta/pipeline/metagenome_work_out/3.gene_predict --step 3 -t 12
echo 3.3 gene depth processing end!!




echo 3.gene prediciton processing end !!


python /sysdata/Meta/script/sampleUtility.py Check_utility_for_sample.txt metagenome_config_2taxa.txt


chmod -R 777*
