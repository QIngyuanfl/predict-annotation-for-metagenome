# Author: Qingyuan Zhang
# Date: Fri Nov 29 14:09:00 CST 2019
# version: 0.1
from io import StringIO
import sys
import pandas as pd

def sort_descend(df):
    df['sum'] = df.sum(axis = 1)
    df = df.sort_values('sum', ascending = False)
    df = df.drop('sum', axis = 1)
    output = StringIO()
    df.to_csv(output, sep = '\t')
    output.seek(0)
    print(output.read())

def main():
    df = pd.read_table(tsv, index_col = 0)
    if method == '--sort_descend':
        sort_descend(df)


if __name__ == "__main__":
    tsv = sys.argv[1]
    method = sys.argv[-1]
    main()
