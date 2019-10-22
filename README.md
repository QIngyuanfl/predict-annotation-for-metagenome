# 宏基因组预测与注释

适用于已经质控并组装的宏基因项目

## 环境准备
### miniconda2 或miniconda3
```sh
# 安装miniconda| linux
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sh Miniconda3-latest-Linux-x86_64.sh
# miniconda 2
$ source activate /sysdata/Meta/conda_envs/py374
# miniconda 3
$ conda activate /sysdata/Meta/conda_envs/py374
```
### python3.7.4 第三方库
- pandas
- matplotlib
- Bio
- aiohttp
- BeautifulSoup
- pyecharts
- FileUtilx(本地库)

### 配置档设置
* [metagenome_config_2taxa.txt](./pipeline/metagenome_config_2taxa.txt)

## 流程执行
```sh
# 在当前文件夹生成流程脚本 predict.sh和annotation.sh
$ python metagenome_pipeline_2taxa.py metagenome_config_2taxa.txt
# 宏基因组基因预测
$ nohup sh predict.sh > predict.log &
# 待预测完成后， 注释
$ nohup sh annotation.sh > annotation.log &
```
## 流程图

## 结果文件

## 新特性
- [邮箱通知](./mailx.md)
- 注释效率提高8倍
- 预测效率提高1.2倍
- 预测与注释在配置档增设CPU配置
- [keggMapper.py]()-异步爬取kegg数据库
- [vfdb_classsum_and_plot.py]()-修正文字遮挡的问题
- [分序列并行化]()

## FAQs
问：如何设置CPU和并行数量？\
答：在oss的系统配置下，为了避免内存使用超额 ，样品数超过10个的项目，每台服务器只能同时运行单个项目，cpu设置为60个。样品数少于10个的项目，每台服务器可以同时运行为两个项目，cpu设置为30个。\
剩余的资源留给售后及个性化分析。

问：如何断点运行？\
答： 样品维度的分析产出结果后，将会通过发进度表给分析人员。倘若与上次的进度表相同或进度表迟迟不发，代表运行错误，可以追踪相应的样品，跑报错的样品。其余的错误可以通过追踪log文件， python 报错关键词为raise, perl 为 at line $. 
