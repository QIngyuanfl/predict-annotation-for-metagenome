#!/usr/bin/env python3
import sys,os,time
import psutil
import pandas as pd 
def proc_tree(pid, include_parent):
    # assert parent pid is not sys.argv[0]
    proc_info = {} 
    assert pid != os.getpid()
    parent = psutil.Process(pid)
    children = parent.children(recursive = True)
         
    if include_parent:
        children.append(parent)
    # process tree information at moment
    for p in children:
        with p.oneshot():
            try:
                start_time=p.create_time()
                now = time.time()
                run_time = now - start_time
                memory = p.memory_info().rss
                cmdline = ' '.join(p.cmdline())
                proc_info[cmdline] = [run_time, memory]
            except Exception as e:
                print(f'PID {p.pid} has been gone')
     
    return proc_info

def main():
    table_file =  'Check_utility_for_Sample.txt'
    pid = int(sys.argv[1])
    if_table = os.path.exists(table_file)
    if if_table:
        df = pd.read_table(table_file, index_col = 'Queue')
    else:
        df = pd.DataFrame(columns = ['RunTime(s)', 'MaxMemory(b)'])
        df.index.name = 'Queue'
    while psutil.pid_exists(pid):
        proc_info = proc_tree(pid, include_parent = True)
        for cmd in proc_info:
            run_time = proc_info[cmd][0] 
            memory = proc_info[cmd][1]
            try:
                if memory <= temp_proc_info[cmd][1]:
                    df.loc[cmd] = [run_time, temp_proc_info[cmd][1]]
                if memory > temp_proc_info[cmd][1]:
                    df.loc[cmd] = [run_time, memory]
                    temp_proc_info = proc_info
            except Exception as e:
                temp_proc_info = proc_info
        df.to_csv(table_file, sep = '\t')
        time.sleep(1)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python monitor.py <pid>')
    else:
        main()
