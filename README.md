# 宏基因组预测、注释与统计

适用于已经质控并组装的宏基因项目

## 环境准备
### miniconda2 或miniconda3
```sh
# 安装miniconda| linux, 已装请忽略
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sh Miniconda3-latest-Linux-x86_64.sh
# conda环境
## 预测与注释环境
$ source activate /sysdata/Meta/conda_envs/py374
## 统计环境
$ source activate /sysdata/Meta/conda_envs/MetaSnakemake
## lefse
$ source activate /sysdata/Meta/conda_envs/lefse
```
### 第三方库
见下方conda环境

- 预测与注释环境-[py374.yml](/conda_envs/py374.yml)
- 统计环境-[snakemake.yml](/conda_envs/snakemake.yml)
- lefse环境-[lefse.yml](/conda_envs/lefse.yml)

### 配置档设置
* [metagenome_config_2taxa.txt](/pipeline/metagenome_config_2taxa.md)
* [config.yaml](/pipeline/config.yaml)-snakemake配置文件
## 新特性
- [snakemake并行化](/script/snakemake.md)
- [Venn图可选感兴趣的分组进行绘图](/script/statistics/Venn.md)
- [三元相图可选感兴趣的分组进行绘图](/script/statistics/ternary.md)
- Beta多样性减少重复计算
    1. Anosim, Adonis, Mrpp 减少计算6倍的次数
    2. 距离矩阵 减少计算30倍的次数
    3. 减少作图次数，基于图层绘图，无需每一幅图不管有无labels或有无椭圆都运行一次绘图函数。
- UPGMA增加Condition绘图
- [消除vim进行替换脚本(R脚本优化)](/script/statistics/Rscript.md)
- 预测模块命令行更新
- 解决云端metaphlan2 lefse无法运行的问题
- 更新metaphlan2 的heatmap 并与matplotlib版本相兼容

## 流程执行
```sh
# 在当前文件夹生成流程脚本 predict.sh和annotation.sh
$ source activate /sysdata/Meta/conda_envs/py374
$ python metagenome_pipeline_2taxa.py metagenome_config_2taxa.txt
# 宏基因组基因预测
$ nohup sh predict.sh > predict.log &
# 待预测完成后， 注释
$ nohup sh annotation.sh > annotation.log &
# 待注释完成后, 统计
$ wget https://github.com/QIngyuanfl/predict-annotation-for-metagenome/edit/master/pipeline/Snakefile
$ conda deactivate
$ source activate /sydata/Meta/conda_envs/MetaSnakemake
$ nohup snakemake --cores 32 > stat.log &
# 统计完成后
$ sh do_clean.sh
```
## 流程图
![流程图](/bpmn-with-drawio.png)
* [统计流程图](/pipeline/dag.pdf)

## FAQs
问：如何设置CPU和并行数量？

答：在oss的系统配置下，为了避免内存使用超额 ，样品数超过10个的项目，每台服务器只能同时运行单个项目，cpu设置为64个。样品数少于10个的项目，每台服务器可以同时运行为两个项目，cpu设置为32个。剩余的资源留给售后及个性化分析。

问：如何断点运行？

答： 样品维度的分析产出结果后，将会通过发进度表给分析人员。倘若与上次的进度表相同或进度表迟迟不发，代表运行错误，可以追踪相应的样品，跑报错的样品。其余的错误可以通过追踪log文件， python 报错关键词为raise, perl 为 at line $. 
## 结果文件
![文件架构](/template/文件架构.png)
