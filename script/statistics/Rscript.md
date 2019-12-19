# R脚本优化
- 减少内存使用与重复变量的计算
- 减少循环内冗余计算
- 同一个R脚本出不同的Condition 的结果
- 统一输入文件
- tibble替代dataframe， 提速20%
## 单独使用方法
基本上使用方法相同
```sh 
$ Rscript /sysdata/Meta/script/statistics/任意.R <丰度表> <分组信息> <输出文件夹> 
```
## beta多样性带环境因子的使用方法
```sh
$ Rscript /sysdata/Meta/script/statistics/betadiv.R <丰度表> <分组信息> <输出文件夹> <环境因子>
```
