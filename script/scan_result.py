#!/usr/bin/env python
import os,sys
import pandas as pd
import numpy as np

class sample:
    def __init__(self, name, size, where):
        self.name = name
        self.size = size
        self.where = where
            
    def OrfScan(self):
        WorkSpace = os.path.abspath(self.where)
        gene_file = os.path.join(WorkSpace, f'3.gene_predict/Gene/{self.name}/{self.name}.gene.ffn')
        if os.path.exists(gene_file):
            if os.path.getsize(gene_file):
                return 1
            if not os.path.getsize(gene_file):
                return 0
        if not os.path.exists(gene_file):
            return 0

    def depthScan(self):
        WorkSpace = os.path.abspath(self.where)
        depth_file = os.path.join(WorkSpace, f'3.gene_predict/Gene/gene_depth/{self.name}.covstats.txt')
        if os.path.exists(depth_file):
            if os.path.getsize(depth_file):
                return 1
            if not os.path.getsize(depth_file):
                return 0
        if not os.path.exists(depth_file):
            return 0


def CatalogueScan(path):
    WorkSpace = os.path.abspath(path)
    gene_catalogue = os.path.join(WorkSpace, '3.gene_predict/Gene/gene_catalogue.summary.txt')
    if os.path.exists(gene_catalogue):
        if os.path.getsize(gene_catalogue):
            return 1
        if not os.path.getsize(gene_catalogue):
            return 0
    if not os.path.exists(gene_catalogue):
        return 0

def AnnotationScan(path):
    WorkSpace = os.path.abspath(path)
    Unigenes = os.path.join(WorkSpace, '4.annotation/Unigenes')
    result_file  = os.path.join(DB,'annotation_result.list')
    exist = 0
    with open(result_file) as f:
        result_list = [line.strip() for line in f]
    for i in os.walk(Unigenes):
        for j in i[2]:
            if j in result_list:
                exist += 1
    finish_percent = exist/len(result_list)
    return finish_percent
        
def main():
    metagenome_work_out = sys.argv[1]
    config = sys.argv[2]    
    with open(config) as f:
        for line in f:
            if line.startswith('mail_address:'):
                mail_address = line.strip().split(':')[-1]
            if line.startswith('Sample_id:'):
                sample_list = line.strip().split(':')[-1].split()
            if line.startswith('current_location:'):
                project_space = line.strip().split(':')[-1].strip()
            if line.startswith('item_number:'):
                item_number = line.strip().split(':')[-1]

    #load existing table
    table_file = os.path.join(project_space, 'Check_Process_for_Sample.txt')
    if_table = os.path.exists(table_file)
    if if_table:
        df = pd.read_table(table_file, index_col = "SampleID")
        df = df.drop('ALL')
        df = df.apply(pd.to_numeric)
    else:
        df = pd.DataFrame(np.zeros((len(sample_list), 6)), columns = ['QC', 'Assemble', 'OrfPrediction', 'GeneCatalogue', 'GeneDepth', 'Annotation'], index = [i for i in sample_list])
    # read sample id and mail_address from configure file

    Catalogue_status = CatalogueScan(metagenome_work_out)
    Annotation_status = AnnotationScan(metagenome_work_out)
    
    for i in sample_list:
        SampleID = i
        size = None
        S1 = sample(SampleID, size, metagenome_work_out)

        orf_status = S1.OrfScan()
        depth_status = S1.depthScan()

        df.loc[i,'OrfPrediction'] = orf_status
        df.loc[i,'GeneCatalogue'] = Catalogue_status
        df.loc[i,'GeneDepth'] = depth_status
        df.loc[i,'Annotation'] = Annotation_status
    df.loc['ALL'] = df.mean().apply(lambda x: '%.2f%%' % (x*100))
    df.to_csv(table_file, sep = '\t', index_label = "SampleID")
    os.system(f'mailx -v -s "{item_number}进度表"  {mail_address} < {table_file}')
if __name__ == "__main__":
    DB = '/sysdata/Meta/DB'
    try:
        main()
    except IndexError:
        print (f"Usage: python3 {sys.argv[0]} <metagenome_work_out directory> <metagenome_config_2taxa.txt>")
