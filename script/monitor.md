# 监测进程运行时间和内存峰值
此脚本用于统计运行时间和内存峰值，方便后续项目的调参。目前是每隔1秒获取PID的运行时间和真实内存。

## 使用方法
```sh
$ python monitor.py <pid>
# 例：在脚本中监测本脚本的运行时间和内存使用值
$ echo 'python monitor.py $$ &' > test.sh
$ echo 'sleep 10' >> test.sh
$ sh test.sh
```
## 结果输出
|Queue|RunTime(s)|MaxMemory(b)|

|---|---|---|

|sleep 10|10.271119117736816|368640.0|

|sh test.sh|10.291218996047974|1421312.0|

|python monitor.py 45201|10.270901679992676|70008832.0|
