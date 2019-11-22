#!/usr/bin/env python
# Author: Qingyuan Zhang
# Date: Fri Nov 22 2019
# Version: v2.0
import re
import sys
import pandas as pd

def extract_rank(rank:str) ->str:
    rank_dict = {'k':'Kingdom', 'p': 'Phylum', 'o':'Order', 'p': 'Phylum', 
    'f':'Family', 'g':'Genus', 's':'Species'}
    
    if re.search(r'(.)__unclassified', rank):
        match = re.search(r'(.)__unclassified', rank).group(1)
        return 'Unclassified'
    if re.search(r'[a-z]__$', rank):
        return 'Unclassified'
    if re.search(r'(.)__(\S+)', rank):
        match = re.search(r'(.)__(.+)', rank)
        return match.group(2)

def split_table(dataframe, col):
    OTU = dataframe.groupby([col]).sum()
    for i in OTU.iterrows():
        tax = i[0]
        if tax == 'Unclassified':
            continue
        else:
            tax = extract_rank(tax)
            if tax == 'Unclassified':
                OTU.loc['Unclassified'] += OTU.loc[i[0]]
                OTU = OTU.drop(i[0])
            else:
                OTU = OTU.rename(index = {i[0]:tax})    
    OTU.to_csv(f'Table_taxa_NR_{col}.txt', sep = '\t')

def main():
    df = pd.read_table(taxonomy_otu)
    ranks = df['taxonomy'].str.split(';', expand = True)
    ranks.columns = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
    ranks.fillna('Unclassified', inplace = True)
    df = df.join(ranks)
    for i in ranks.columns:
        split_table(df, i)            
                
if __name__ == "__main__":
    taxonomy_otu = sys.argv[1]
    main()

