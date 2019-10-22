# 分序列并行化
一些软件只支持单线程运行，另一些软件大部分时间都在IO.在这两种情况下，分序列并行化能极大的提高任务运行的速度.
此次更新后, cazy hmmscan不需要转移到master运行，可以直接在oss上运行，并且资源利用率提升很大。

## FileUtilx 分序列并行化
### 低层API： 拆分序列
``` python
lib_path = 'sydata/Meta/Lib'
sys.path.append(lib_path)
import FileUtilx
FileUtilx.split_file(src, chunk, sep = '\n', out = '.')
"""
src: 源文件
chunk: 分割出的个数
sep: 分隔符
out: 输出文件夹
"""
# 例:将1个fasta文件分为10分并保存到当前文件夹
# FileUtilx.split_file('demo.fasta', 10, sep = '>')
# 输出文件为 ./demo.fasta.1 ./demo.fasta.2 ... ./demo.fasta.10
# 不支持压缩文件
```

### 高层API: 分序列并行化写入*shell*
``` python
split_input_multirun_insh(src_in, src_out, chunk, fh, tool, sep = '\n', **kwargs)
"""
src_in: 命令行的输入参数
src_out: 命令行的输出参数
chunk 和 sep 同上
fh : 已经通过python打开的文件
tool: 使用的工具
**kwargs: 命令行传入的参数
# 例: data{'-i': input_file, '-o': output_file, '-g':'11', ...}
# FileUtilx.split_input_multirun_insh('-i', '-o', 10, f, 'prodigal', sep = '>', **data
"""
```
