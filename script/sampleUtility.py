#!/usr/bin/env python
import os,re,sys
import pandas as pd
import numpy as np
def convert(value):
    new_value = str(value).replace('s', '').replace('G', '')
    return np.float(new_value)
def main():
    # sample information
    with open(config) as f:
        for line in f:
            if line.startswith('Sample_id:'):
                sample_list = line.strip().split(':')[-1].split()
            if line.startswith('current_location:'):
                project_space = line.strip().split(':')[-1].strip()
    
    # load existing table
    time_file = os.path.join(project_space, 'Check_source_for_Sample.txt')
    rss_file = os.path.join(project_space, 'Check_time_for_Sample.txt')
    if_table = os.path.exists(time_file) and os.path.exists(time_file)
    if if_table:
        df_t = pd.read_table(time_file, index_col = "SampleID")
        df_s = pd.read_table(rss_file, index_col = "SampleID")
        if 'All' in df_s.index:
            df_s = df_s.drop('All')
        df_s = df_s.applymap(lambda x: convert(x))
    else:
        df_s = pd.DataFrame(np.zeros((len(sample_list), 7)), 
        columns = ['raw base(G)', 'QC', 'Assemble', 'OrfPrediction', 'GeneCatalogue',
        'GeneDepth', 'Annotation'], index = [i for i in sample_list])
        df_t = pd.DataFrame(np.zeros((len(sample_list)+1, 7)),
        columns = ['bases(G)', 'QC', 'Assemble', 'OrfPrediction', 'GeneCatalogue',
        'GeneDepth', 'Annotation'], index = [i for i in sample_list]+['All'])
    # screen run time and maximum rss usage in samples level
    all_utility = pd.read_table(Check_utility_for_sample, sep = '\t')
    cmd = all_utility['Queue']
    # gene catalogue
    catalogue = all_utility[cmd.str.contains('predict_2.sh')]
    catalogue_run_time = str(round(max(catalogue['RunTime(s)'])))+'s'
    df_t['GeneCatalogue'] = catalogue_run_time
    catalogue_MaxMemory = float(max(catalogue['MaxMemory(b)']))/(1024**3)
    df_s['GeneCatalogue'] = catalogue_MaxMemory
    # annotation
    annotation = all_utility[cmd.str.contains('annotation')]
    annotation_runtime = str(round(max(annotation['RunTime(s)']))) + 's'
    df_t['Annotation'] = catalogue_run_time
    annotation_MaxMemory = float(max(annotation['MaxMemory(b)']))/(1024**3)
    df_s['Annotation'] = catalogue_run_time 
    for i in sample_list:
        sample_cmd = all_utility[cmd.str.contains(i)]
        # orf prediction
        orf_time = str(round(max(sample_cmd[sample_cmd['Queue'].str.contains(pat = f'{i}_orf_predict.sh')]['RunTime(s)'])))+'s'
        df_t.loc[i, 'OrfPrediction'] = orf_time
        orf_rss = float(max(sample_cmd[sample_cmd['Queue'].str.contains('prodigal|antifam', regex = True)]['MaxMemory(b)']))/(1024**3)
        df_s.loc[i, 'OrfPrediction'] = orf_rss
        # gene depth
        depth_time = str(round(max(sample_cmd[sample_cmd['Queue'].str.contains('bbmap')]['RunTime(s)'])))+'s'
        df_t.loc[i, 'geneDepth'] = depth_time
        depth_rss = float(max(sample_cmd[sample_cmd['Queue'].str.contains('bbmap')]['MaxMemory(b)']))/(1024**3)
        df_s.loc[i, 'geneDepth'] = depth_rss
    # All
        df_t.loc['All', 'OrfPrediction'] = round(max(all_utility[cmd.str.contains(pat = 'predict_1.sh')]['RunTime(s)']))
        df_t.loc['All', 'Gene_depth'] = round(max(all_utility[cmd.str.contains(pat = 'predict_3.sh')]['RunTime(s)']))
    df_t.to_csv(time_file, sep = '\t', index_label = "SampleID")
    df_s.to_csv(rss_file, sep = '\t', index_label = "SampleID")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python sampleUtility.py <Check_utility_for_sample.txt> \
<config>')
    else:
        Check_utility_for_sample = sys.argv[1]
        config = sys.argv[2]
        main()
