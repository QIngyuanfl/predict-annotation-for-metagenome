#-*- coding: utf-8 -*-
import sys
import os

#config = raw_input('please give you config file:')
#config_file = open(config,'r')
config_file = open(sys.argv[1],'r')
#line = config_file.readline()

for line in config_file :
    list = line.strip().split(' ')
    if list[0] == 'current_location:':
        current_location = list[1];
    elif list[0] == 'Sample_id:':
        N_sample = len(list)-1
        #print N_sample
        sample_list = list[1:]
        #print sample_list;
    elif list[0] == "is_complete:":
        is_complete = list[1]
    elif list[0] == 'mail_address':
        mail_address = list[1]
    elif list[0] == 'R1R2_common:':
        R1R2_common = list[1:]
    elif list[0] == 'Output:':
         Output = list[1];
    elif list[0] == 'Fastq_location:': 
        Fastq_location = list[1];
    elif list[0] == 'method:':
        method = list[1];
    elif list[0] == 'phred_type:':
        phred_type = int(list[1]);
        #print phred_type;
    elif list[0] == 'tparam:':
        tparam = list[1:];
        #print tparam
        N_tparam = len(list)-1
        #print N_tparam
    elif list[0] == 'quality:':
         quality = int(list[1]);
    elif list[0] == 'length_cutoff:':
         length_cutoff = int(list[1]);
    elif list[0] == 'uniq:':
         uniq = list[1];
    elif list[0] == 'adapter:':
        adapter = list[1];
    elif list[0] == 'host_genome:':
        host_genome = list[1];
    elif list[0] == 'readsQC4metaGenome:':
        readsQC4metaGenome = list[1];
    elif list[0] == 'assemble4metaGenome:':
        assemble4metaGenome = list[1];
    elif list[0] == 'model:':
        model = list[1];
    elif list[0] == 'toolkit:':
        toolkit = list[1];
    elif list[0] == 'mink:':
        mink = list[1];
    elif list[0] == 'maxk:':
        maxk = list[1];
    elif list[0] == 'step:':
        step = list[1];
    elif list[0] == 'threads:':
        threads = list[1];
    elif list[0] == 'memory:':
        memory = list[1];
    elif list[0] == 'contig_length:':
        contig_length = list[1];
    elif list[0] == 'genePredict4metaGenome:':
         genePredict4metaGenome = list[1];
    elif list[0] == 'content:':
        content = list[1];
    elif list[0] == 'cell_type:':
        cell_type = list[1];
    elif list[0] == 'evalue:':
        evalue = list[1];
    elif list[0] == 'threads_per_task:':
        threads_per_task = list[1];
    elif list[0] == 'task_number:':
        task_number = list[1];
    elif list[0] == 'geneAnnotate4metaGenome:':
        geneAnnotate4metaGenome = list[1];
    elif list[0] == 'monitor:':
        monitor = list[1];
    elif list[0] == 'multiTask_to_run:':
        multiTask_to_run = list[1];
    elif list[0] == 'sampleUtility:':
        sampleUtility = list[1];
    elif list[0] == 'predict_core:':
        predict_core = list[1];
    elif list[0] == 'gene_nr_taxonomies:':
        gene_nr_taxonomies = list[1];
    elif list[0] == 'mapping_file:':
        mapping_file = list[1];
    elif list[0] == 'split_sample_group:':
        split_sample_group = list[1];
    elif list[0] == 'metaphlan2_taxonomies:':
        metaphlan2_taxonomies = list[1];
    elif list[0] == 'summarize_taxa_x:':
        summarize_taxa_x = list[1];
    elif list[0] == 'diff_level_taxa_abundance_summary:':
        diff_level_taxa_abundance_summary = list[1];
    elif list[0] == 'factors_file:':
        factors_file = list[1];
    elif list[0] == 'mapping_category_id:':
        #N_category = len(list)-2
        #category_list = list[1:len(list)-1]
        N_category = len(list)-1
        category_list = list[1:]
    elif list[0] == 'beta_format:':
        beta_format = list[1];
    elif list[0] == 'beta_nofactors_format:':
        beta_nofactors_format = list[1];
    elif list[0] == 'multi_taxa_barplot:':
        multi_taxa_barplot = list[1];
    elif list[0] == 'taxa_heatmap_plot:':
        taxa_heatmap_plot = list[1];
    elif list[0] == 'taxa_heatmap_plot_means:':
        taxa_heatmap_plot_means = list[1];
    elif list[0] == 'extract_topNum_table:':
        extract_topNum_table = list[1];
    elif list[0] == 'bubble_plot:':
        bubble_plot = list[1];
    elif list[0] == 'deleteTaxonColumn:':
        deleteTaxonColumn = list[1];
    elif list[0] == 'spearman_correlation:':
        spearman_correlation = list[1];
    elif list[0] == 'ternary_list:':
        ternary_list = list[1];
    elif list[0] == 'ternaryplot:':
        ternaryplot = list[1];
    elif list[0] == 'UPGMA_tree_plot_L2:':
         UPGMA_tree_plot_L2 = list[1];
    elif list[0] == 'UPGMA_tree_plot_L3:':
        UPGMA_tree_plot_L3 = list[1];
    elif list[0] == 'UPGMA_tree_plot_L4:':
        UPGMA_tree_plot_L4 = list[1];
    elif list[0] == 'UPGMA_tree_plot_L5:':
        UPGMA_tree_plot_L5 = list[1];
    elif list[0] == 'UPGMA_tree_plot_L6:':
        UPGMA_tree_plot_L6 = list[1];
    elif list[0] == 'UPGMA_tree_plot_L7:':
        UPGMA_tree_plot_L7 = list[1];
    elif list[0] == 'species_env_corr_heatmap:':
        species_env_corr_heatmap = list[1];
    elif list[0] == 'draw_VPA_L2:':
        draw_VPA_L2 = list[1];
    elif list[0] == 'draw_VPA_L3:':
        draw_VPA_L3 = list[1];
    elif list[0] == 'draw_VPA_L4:':
        draw_VPA_L4 = list[1];
    elif list[0] == 'draw_VPA_L5:':
        draw_VPA_L5 = list[1];
    elif list[0] == 'draw_VPA_L6:':
        draw_VPA_L6 = list[1];
    elif list[0] == 'draw_VPA_L7:':
        draw_VPA_L7 = list[1];
    elif list[0] == 'sum_keggFunc_abundance:':
        sum_keggFunc_abundance = list[1];
    elif list[0] == 'sum_eggNOGFunc_abundance:':
        sum_eggNOGFunc_abundance = list[1];
    elif list[0] == 'sum_cazyFunc_abundance:':
        sum_cazyFunc_abundance = list[1];
    elif list[0] == 'Clean_Output:':
        Clean_Output = list[1];
    elif list[0] == 'PCA_format:':
        PCA_format = list[1];
    elif list[0] == 'N_conditions:':
        #N_conditions = len(list)-2
        #list_N_conditions = list[1:len(list)-1]
        N_conditions = len(list)-1
        list_N_conditions = list[1:]
    elif list[0] == 'Venn_format:':
        Venn_format = list[1];
    elif list[0] == 'sig_wilcoxon_format:':
        sig_wilcoxon_format = list[1];
    elif list[0] == 'sig_ttest_format:':
        sig_ttest_format = list[1];
    elif list[0] == 'format_input:':
        format_input = list[1];
    elif list[0] == 'run_lefse:':
        run_lefse = list[1];
    elif list[0] == 'plot_res:':
        plot_res = list[1];
    elif list[0] == 'plot_cladogram:':
        plot_cladogram = list[1];
    elif list[0] == 'plot_features:':
        plot_features = list[1];
    elif list[0] == 'jar_location:':
        jar_location = list[1];
    elif list[0] == 'java_location:':
        java_location = list[1];
    elif list[0] == 'Picture2Word2:':
        Picture2Word2 = list[1];
    elif list[0] == 'template_oo:':
        template_oo = list[1];
    elif list[0] == 'template_ox:':
        template_ox = list[1];
    elif list[0] == 'template_xo:':
        template_xo = list[1];
    elif list[0] == 'template_xx:':
        template_xx = list[1];
    elif list[0] == 'template_s1:':
        template_s1 = list[1];
    elif list[0] == 'template_s2:':
        template_s2 = list[1];
    elif list[0] == 'name:':
        name = list[1];
    elif list[0] == 'client:':
        client = list[1];
    elif list[0] == 'item_number:':
        item_number = list[1];
    elif list[0] == 'total_samples:':
        total_samples = list[1];
    elif list[0] == 'year:':
        year = list[1];
    elif list[0] == 'month:':
        month = list[1];
    elif list[0] == 'day:':
        day = list[1];
    elif list[0] == 'template_oo_id:':
        template_oo_id = list[1];
    elif list[0] == 'template_xo_id:':
        template_xo_id = list[1];
    elif list[0] == 'template_ox_id:':
        template_ox_id = list[1];
    elif list[0] == 'template_xx_id:':
        template_xx_id = list[1];
    elif list[0] == 'template_s1_id:':
        template_s1_id = list[1];
    elif list[0] == 'template_s2_id:':
        template_s2_id = list[1];
    elif list[0] == 'Report_id:':
        Report_id = list[1];
    elif list[0] == 'Meta_shotgun:':
        Meta_shotgun = list[1];
    elif list[0] == 'Meta_R:':
        Meta_R = list[1];
    elif list[0] == 'merge_metaphlan_tables:':
        merge_metaphlan_tables = list[1];
    elif list[0] == 'metaphlan_hclust_heatmap:':
        metaphlan_hclust_heatmap = list[1];
    elif list[0] == 'ktImportRDP:':
        ktImportRDP = list[1];
    elif list[0] == 'metagenome_clean:':
        metagenome_clean = list[1];
    elif list[0] == 'Meta_py3:':
        Meta_py3 = list[1];

#新增待驗證
    elif list[0] == 'draw_fuctionClass_barplot:':
        draw_fuctionClass_barplot = list[1];
    elif list[0] == 'mean_sd:':
        mean_sd = list[1];
    elif list[0] == 'uniq_group_list:':
        uniq_group_list = list[1];
    elif list[0] == 'draw_heatmap:':
        draw_heatmap = list[1];
    elif list[0] == 'UPGMA_tree_plot_kegg_ko:':
        UPGMA_tree_plot_kegg_ko = list[1];
    elif list[0] == 'UPGMA_tree_plot_kegg_L1:':
        UPGMA_tree_plot_kegg_L1 = list[1];
    elif list[0] == 'UPGMA_tree_plot_kegg_L2:':
        UPGMA_tree_plot_kegg_L2 = list[1];
    elif list[0] == 'UPGMA_tree_plot_kegg_L3:':
        UPGMA_tree_plot_kegg_L3 = list[1];
    elif list[0] == 'draw_VPA_kegg_ko:':
        draw_VPA_kegg_ko = list[1];
    elif list[0] == 'draw_VPA_kegg_L1:':
        draw_VPA_kegg_L1 = list[1];
    elif list[0] == 'draw_VPA_kegg_L2:':
        draw_VPA_kegg_L2 = list[1];
    elif list[0] == 'draw_VPA_kegg_L3:':
        draw_VPA_kegg_L3 = list[1];

    elif list[0] == 'UPGMA_tree_plot_nog_L1:':
        UPGMA_tree_plot_nog_L1 = list[1];
    elif list[0] == 'UPGMA_tree_plot_nog_L2:':
        UPGMA_tree_plot_nog_L2 = list[1];
    elif list[0] == 'draw_VPA_nog_L1:':
        draw_VPA_nog_L1 = list[1];
    elif list[0] == 'draw_VPA_nog_L2:':
        draw_VPA_nog_L2 = list[1];

    elif list[0] == 'UPGMA_tree_plot_cazy_L1:':
        UPGMA_tree_plot_cazy_L1 = list[1];
    elif list[0] == 'UPGMA_tree_plot_cazy_family:':
        UPGMA_tree_plot_cazy_family = list[1];
    elif list[0] == 'draw_VPA_cazy_L1:':
        draw_VPA_cazy_L1 = list[1];
    elif list[0] == 'draw_VPA_cazy_family:':
        draw_VPA_cazy_family = list[1];

# source enviromant !!
#print "source activate", Meta_shotgun 
'''
# mkdir -p dictories
print("## mkdir -p dictories ##")
print("mkdir -p", Output)
print('\n')

print("source activate", Meta_py3)

print("rm", Output + "../source_results.txt")
print("echo Process Time Memory >", Output + "../source_results.txt")

# 0.samples groups infor processing
print("echo 0.samples groups infor processing start")
#print "source activate", Meta_py3
print("mkdir -p", Output + "sample_groups_info")
print("python", split_sample_group, mapping_file, Output + "sample_groups_info")

#print "source deactivate"
#print "source activate", Meta_shotgun
print('\n')

#print "mkdir -p", Output + "5.taxa"

# 1. trimming processing
print("echo 1.trimming processing start")
print("echo 2018V3-质控")
print("date")
print("mkdir -p", Output + "1.clean_data")
tparam_list = ""

j=1
while j <= N_sample:
    if j == 1:
        print("echo -e", sample_list[j-1] + "\\\\t" + Fastq_location + sample_list[j-1] + R1R2_common[0] + "," + Fastq_location + sample_list[j-1] + R1R2_common[1], ">", Output + "1.clean_data" + "/" + "raw_fq_list.txt") 
    elif j > 1:
        print("echo -e", sample_list[j-1] + "\\\\t" + Fastq_location + sample_list[j-1] + R1R2_common[0] + "," + Fastq_location + sample_list[j-1] + R1R2_common[1], ">>", Output + "1.clean_data" + "/" + "raw_fq_list.txt") 
    j +=1;
print('\n')

i=1
while i <= N_tparam:
    if i < N_tparam:
        tparam_list = tparam_list + tparam[i-1] + " "
    if i == N_tparam:        
        tparam_list = tparam_list + tparam[i-1]
    i += 1;
#print tparam_list
if adapter == "None" and host_genome == "None":
    #print "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq
    print("/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time", "-a -o", Output + "../source_results.txt -f", "\'" + "QC","%e","%M\'", "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq)
if adapter != "None" and host_genome == "None":
        #print "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq, "-a", adapter
        print("/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time", "-a -o", Output + "../source_results.txt -f", "\'" + "QC","%e","%M\'", "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq, "-a", adapter)
if adapter == "None" and host_genome != "None":
        #print "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq, "-g", host_genome
        print("/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time", "-a -o", Output + "../source_results.txt -f", "\'" + "QC","%e","%M\'", "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq, "-g", host_genome)
if adapter != "None" and host_genome != "None":
        #print "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq, "-a", adapter, "-g", host_genome
        print("/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time", "-a -o", Output + "../source_results.txt -f", "\'" + "QC","%e","%M\'", "python", readsQC4metaGenome, "-f", Output + "1.clean_data" + "/" + "raw_fq_list.txt", "-d", Output + "1.clean_data", "-p", phred_type, "-t", "\"" + tparam_list + "\"", "-c", quality, "-l", length_cutoff, "-m", method, "-u", uniq, "-a", adapter, "-g", host_genome)
print('\n')
print("echo 1.trimming processing end !!")
print('\n')
# 2. assembly processing
print("echo 2.assembly processing start")
print("echo 2018V3-序列组装")
print("date")
print('\n')
print("mkdir -p", Output + "2.assembly") 
print("cp", Output + "1.clean_data" + "/" + "clean_reads_file.list", Output + "2.assembly" + "/" + "clean_reads_file.list")

print('\n')
print("export MPLBACKEND=\"Agg\"")
#print "python", assemble4metaGenome, "-f", Output + "2.assembly" + "/" + "clean_reads_file.list", "-d", Output + "2.assembly", "-m", model, "-t", toolkit, "--mink", mink, "--maxk", maxk, "---step", step, "--threads", threads, "--memory", memory, "--length", contig_length 
print("/home/chihminchang/Metagenomics/Meta_shotgun/bin/time-1.9/time", "-a -o", Output + "../source_results.txt -f", "\'" + "Assembly","%e","%M\'", "python", assemble4metaGenome, "-f", Output + "2.assembly" + "/" + "clean_reads_file.list", "-d", Output + "2.assembly", "-m", model, "-t", toolkit, "--mink", mink, "--maxk", maxk, "---step", step, "--threads", threads, "--memory", memory, "--length", contig_length) 

print('\n')
print("echo 2.assembly processing end !!")
print('\n')
'''
# 3.gene prediciton processing
f = open('predict.sh','w')
print("source activate", Meta_py3, file = f)
print("echo 2018V3-基因预测" , file = f)
print("date" , file = f)
print('\n' , file = f)
print(f'nohup python {monitor} $$ &', file = f)


print("mkdir -p", Output + "3.gene_predict" , file = f)
print("cp", Output + "1.clean_data" + "/" + "clean_reads_file.list", Output + "3.gene_predict" + "/" + "clean_reads_file.list" , file = f)
print("cp", Output + "2.assembly" + "/" + "assemble_seq.list", Output + "3.gene_predict" + "/" + "assemble_seq.list" , file = f)

print('\n' , file = f)

print('\n', file = f)
#print "python", genePredict4metaGenome, "-q", Output + "3.gene_predict" + "/" + "clean_reads_file.list", "-f", Output + "3.gene_predict" + "/" + "assemble_seq.list", "-d", Output + "3.gene_predict", "-n", "T"

print("echo 3.1 orf prediciton processing start !!" , file = f)
print("python", genePredict4metaGenome, "-q", Output + "3.gene_predict" + "/" + "clean_reads_file.list", "-f", Output + "3.gene_predict" + "/" + "assemble_seq.list", "-d", Output + "3.gene_predict", "--step", "1", "-t", predict_core, file = f)
print("echo 3.1 orf prediciton processing end!!" , file = f)

if is_complete == "True":
    print("echo 3.2 gene catalogue processing start!!" , file = f)
    print("python", genePredict4metaGenome, "-q", Output + "3.gene_predict" + "/" + "clean_reads_file.list", "-f", Output + "3.gene_predict" + "/" + "assemble_seq.list", "-d", Output + "3.gene_predict", "--step", "2", "-t", predict_core, file = f)
    print("echo 3.2 gene catalogue processing end!!" , file = f)

    print("echo 3.3 gene depth processing start!!" , file = f)
    print("python", genePredict4metaGenome, "-q", Output + "3.gene_predict" + "/" + "clean_reads_file.list", "-f", Output + "3.gene_predict" + "/" + "assemble_seq.list", "-d", Output + "3.gene_predict", "--step", "3", "-t", predict_core, file = f)

    print("echo 3.3 gene depth processing end!!" , file = f)
    print('\n' , file = f)



    print('\n' , file = f)
    print("echo 3.gene prediciton processing end !!" , file = f)
    print('\n' , file = f)
    print("python", sampleUtility, 'Check_utility_for_sample.txt', sys.argv[1], file = f)
    print('\n' , file = f)
    print("chmod -R 777*", file = f)
    f.close()

    # 4.annotation processing
    f = open('annotation.sh','w')
    print("echo 4.annotation processing start", file = f)
    print("echo 2018V3-物种及功能注释", file = f)
    print("date", file = f)
    print('\n', file = f)
    print("source activate", Meta_py3, file = f)

    print(f'nohup python {monitor} $$ &', file = f)
    print("mkdir -p", Output + "4.annotation", file = f)
    print("mkdir -p", Output + "4.annotation" + "/" + "Unigenes", file = f)
    print("cp", Output + "3.gene_predict" + "/" + "Gene" + "/" + "gene_catalogue.faa", Output + "4.annotation" + "/" + "gene_catalogue.faa", file = f)
    print("cp", Output + "3.gene_predict" + "/" + "Gene" + "/" + "gene_depth" + "/" + "gene_abundance_table.txt", Output + "4.annotation" + "/" + "gene_abundance_table.txt", file = f)
    print('\n', file = f)

    print("export MPLBACKEND=\"Agg\"", file = f)

    #201909
    print("echo", "python", geneAnnotate4metaGenome, "-p", Output + "4.annotation" + "/" + "gene_catalogue.faa", "-g", "Unigenes", "-o", Output + "4.annotation" + "/" + "Unigenes", "-n", content, "-t", threads_per_task, "-m", task_number, "-e", evalue, "-a", Output + "4.annotation" + "/" + "gene_abundance_table.txt", ">", Output + "4.annotation" + "/" + "annotate_task_cmd.sh", file = f)
    
    print('\n', file = f)
    print('sh ', Output + "4.annotation" + "/" + "annotate_task_cmd.sh", file =f)
    print('\n', file = f)
    print("echo 4.annotation processing end !!", file = f)
    print('\n', file = f)
    print('\n', file = f)
    # 5.taxa processing
    print("echo 5.taxa processing start", file = f)
    print("echo 2018V3-后续分析", file = f)
    print("date", file = f)
    print('\n', file = f)

    print("mkdir -p", Output + "5.taxa", file = f)
    print("mkdir -p", Output + "5.taxa" + "/" + "common_taxonomic", file = f)
    print("ln -s", Output + "3.gene_predict" + "/" + "Gene" + "/" + "gene_catalogue.faa", Output + "5.taxa" + "/" + "gene_catalogue.faa", file = f)
    print("ln -s", Output + "3.gene_predict" + "/" + "Gene" + "/" + "gene_depth" + "/" + "gene_abundance_table.txt", Output + "5.taxa" + "/" + "gene_abundance_table.txt", file = f)
    print("ln -s", Output + "4.annotation" + "/" + "Unigenes" + "/" + "NR" + "/" + "Unigenes_vs_nr_fortaxa.txt", Output + "5.taxa" + "/" + "Unigenes_vs_nr_fortaxa.txt", file = f)


    print("python", gene_nr_taxonomies, "-p", Output + "5.taxa" + "/" + "gene_catalogue.faa", "-n", Output + "5.taxa" + "/" + "Unigenes_vs_nr_fortaxa.txt", "-a", Output + "5.taxa" + "/" + "gene_abundance_table.txt", "-o", Output + "5.taxa" + "/" + "common_taxonomic", file = f)

    print('\n', file = f)

    print("mkdir -p", Output + "5.taxa" + "/" + "metaphlan2_taxonomic", file = f)
    print("cp", Output + "1.clean_data" + "/" + "clean_reads_file.list", Output + "5.taxa" + "/" + "clean_reads_file.list", file = f)

    g=1;
    while g <= N_category:

        print("mkdir -p", Output + "sample_groups_info" + "/" + category_list[g-1], file = f)
        print("cp", Output + "sample_groups_info" + "/" + "sample_" + category_list[g-1] + ".tsv", Output + "sample_groups_info" + "/" + category_list[g-1] + "/.", file = f)
        print("cp", Output + "sample_groups_info" + "/" + "sample_ids.tsv", Output + "sample_groups_info" + "/" + category_list[g-1] + "/.", file = f)

        print("python", metaphlan2_taxonomies, "-q", Output + "5.taxa" + "/" + "clean_reads_file.list", "-o", Output + "5.taxa" + "/" + "metaphlan2_taxonomic", "-g", Output + "sample_groups_info" + "/" + category_list[g-1], "-t", int(threads_per_task)*int(task_number), file = f)

        g += 1;
    print('\n', file = f)


    if N_sample == 1:
        print("cd", Output + "5.taxa" + "/" + "metaphlan2_taxonomic", file = f)
        print("python", merge_metaphlan_tables, "*taxa_profile.txt > merged_abundance_table.txt", file = f)
        print("sed -i 's/.taxa_profile//g' merged_abundance_table.txt", file = f)
        print("python", metaphlan_hclust_heatmap, "--in merged_abundance_table.txt --out merged.heatmap.pdf -m average -d braycurtis -f correlation --tax_lev s", file = f)
        print("python", metaphlan_hclust_heatmap, "--in merged_abundance_table.txt --out merged.heatmap.png -m average -d braycurtis -f correlation --tax_lev s")
        print("perl", ktImportRDP, sample_list[0] + ".krona.txt," + sample_list[0], file = f)
    print("python", sampleUtility, 'Check_utility_for_sample.txt', sys.argv[1], file = f)
    print("chmod -R 777 *", file =f) 
    f.close()



#########################################################
    os.system("python", metagenome_clean, sys.argv[1], ">", "do_clean.sh") 

    print("echo 分析解析完毕，进入运行环节 !!")

    print('\n')
    config_file.close()



