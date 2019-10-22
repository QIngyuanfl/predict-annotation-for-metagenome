#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author:    Zhihao Xie  \(#^o^)/
# Date:      2017.06.01
# Version:   v1.0.0
# CopyRight: Copyright ©Zhihao Xie, All rights reserved.

__author__ = "Zhihao Xie"
__version__ = "v1.0.0"

import sys
import os
import re
import gzip
import magic
from collections import OrderedDict

_names = sys.builtin_module_names

def _exists(name):
    return name in globals()


# some functions
def fileType(fpath):
    """
    determine whether the file is a compressed file and return the file type.
    return file type: gzip, bzip2, zip, rar, text or unknown.    
    """
    if os.path.exists(fpath):
        file_type = magic.from_file(fpath)
        if re.search(r"gzip compressed", file_type):
            put_str = "gzip"
        elif re.search(r"bzip2 compressed", file_type):
            put_str = "bzip2"
        elif re.search(r"Zip archive", file_type, re.I):
            put_str = "zip"
        elif re.search(r"RAR ?(archive)?", file_type, re.I):
            put_str = "rar"
        elif re.search(r"tar archive", file_type):
            put_str = 'tar'
        elif re.search(r"text", file_type):
            put_str = "text"
        else:
            put_str = "unknown"
    else:
        raise Exception("Error! The file don't exists.\n")
    return put_str

def is_CompressFile(fpath):
    """
    determine whether the file is a compressed file and return True or False.
    """
    status = False
    models = re.compile(r"gzip compressed|bzip2 compressed|Zip archive|RAR ?(archive)?|tar archive", re.I)
    if os.path.exists(fpath):
        file_type = magic.from_file(fpath)
        if models.search(file_type):
            status = True
    else:
        raise Exception("Error! The file don't exists.\n")

    return status

def read_Param(yourFile, sep="\s*=\s*"):
    """ get the params from a file and return a hash. default separation(sep) is " = ". """

    yourFile = os.path.abspath(yourFile)
    myHash = {}
    if not os.path.exists(yourFile):
        sys.stderr.write("Error! The file of %s don't exit.\n" % yourFile)
        sys.exit(1)
    else:
        compile_mo = re.compile(sep)
        handle = open(yourFile, "rU")
        for line in handle:
            if re.search(r"^#|^\s*$", line):
                continue
            else:
                param_name, param_value = compile_mo.split(line.strip(), 1)
                param_value = param_value.strip("\"")
                param_value = param_value.strip("\'")
                myHash[param_name] = param_value
    return myHash

def read_SeqList(table_file):
    """ read the sequence list and return a hash include sample name and file path. default separation(sep) is "\t". """

    table_file = os.path.abspath(table_file)
    seq_hash = OrderedDict()
    if not os.path.exists(table_file):
        sys.stderr.write("Error: The file of %s don't exists.\n" % table_file)
        sys.stderr.flush()
        sys.exit()
    else:
        fh = open(table_file, 'rU')
        for line in fh:
            if len(line)>0:
                if re.search(r'^#|^\s*$', line):
                    continue
                else:
                    sample_name, seq_v = line.strip().split("\t", 1)
                    if re.search(r',', seq_v):
                        seq_1, seq_2 = seq_v.strip().split(',', 1)
                        seq_hash.setdefault(sample_name, {})
                        seq_hash[sample_name]['r1'] = os.path.abspath(seq_1)
                        seq_hash[sample_name]['r2'] = os.path.abspath(seq_2)
                    else:
                        seq_hash[sample_name] = os.path.abspath(seq_v)
        fh.close()
        return seq_hash

def mergeTxtFile(fileListStr, outFile):
    """
    merge text files to a large file. 
    usage:
        mergeTxtFile("file1 file2 file3 ...", outFile)
    note:
        fileListStr is string, and separated by space.
    """
    outFile = os.path.join(outFile)
    fileList = re.split(r"\s+", fileListStr)
    with open(outFile, "w") as outFH:
        for item in fileList:
            if os.path.exists(item):
                inputFH = open(item, "rU")  # read input file
                for line in inputFH:
                    if len(line)==0:
                        break
                    outFH.write(line)
                inputFH.close()
            else:
                print("Error! The file of %s don't exist." % item, file=sys.stderr)
                sys.exit(1)

def find_file(path, ext=None):
    # find all files or .ext files
    path = os.path.abspath(path)
    file_lists = []
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            base, file_ext = os.path.splitext(filename)
            if ext:
                if file_ext.lower() == ext.lower():
                    file_lists.append(os.path.join(parent, filename))
            else:
                file_lists.append(os.path.join(parent, filename))
        for dirname in dirnames:
            if os.path.isfile(os.path.join(parent, dirname)):
                abspath = os.path.join(parent, dirname)
                base, file_ext = os.path.splitext(abspath)
                if ext:
                    if file_ext.lower() == ext.lower():
                        file_lists.append(abspath)
                else:
                    file_lists.append(abspath)
    return file_lists

def make_completeLog(outfile, signal):
    """
    make log file
    :param outfile: log file to write
    :param signal: 0 or 1
    """
    outlog = outfile
    with open(outlog, 'w') as fh:
        if signal == 0:
            fh.write("All completed.\n")
        else:
            fh.write("failed.\n")

def split_file(src, chunk, sep = '\n', out = '.'):
    for i in range(1, chunk+1):
        exec(f'src{i} = open("{src}.{i}", "w")')
    with open(src) as f:
        lines = f.read()
        lines = lines.split(sep)
        NR = 1
        for line in lines:
            exec(f'src{NR}.write(sep + line)')
            if NR % chunk == 0:
                NR = 0
            NR += 1
    for i in range(1,chunk+1):
        exec(f'src{NR}.close()')

def split_input_multi_run_insh(src_param, chunk, tool, out = '.', sep = '\n', 
sh = None, **kwargs):
    src = kwargs[src_param]
    split_file(src, chunk, sep , out)
    for i in range(1, chunk+1):
        f.write(tool+'\t')
        if src == kwargs[src_param]:
            kwargs[src_param] = f'{kwargs[src_param]}.{i}'
        if src != kwargs[src_param]:
            kwargs[src_param] = kwargs[src_param].repalce(str(i), str(i-1))
        for arg in kwargs:
           f.write(args+' '+kwargs[arg]+' '+'& PID{i}=$!\n')
    for i in range(1, chunk+1):
        f.write(f'wait $PID{i}\n')
    
if __name__ == "__main__":
    func_lists = ["fileType", "is_CompressFile", "read_Param", "read_SeqList", "mergeTxtFile", "find_file", "make_completeLog", "split_file"]
    print("You can use functions inclused:", " ".join(func_lists))
