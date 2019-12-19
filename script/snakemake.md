# Snakemake 宏基因组统计流程
## snakemake 流程的优势
- 可将流程中不同任务进行自动化并行计算，32核运行流程理论上能提高3000% 速度，目前的限速步骤为lefse。
- 支持通配符，主流程代码量减少87%
- 自动生成时间与内存使用报告与流程图
- 断点运行
- 单模块运行
- 指定输出文件运行
- 在成功和失败执行任务的时候发送邮箱通知

## 使用方法

1. 在项目文件夹创建snakemake配置文件[config.yaml](/pipeline/config.yaml)
2. 将Snakefile 拷贝至项目文件夹
```sh
cp /sysdata/Meta/pipeline/Snakefile workdir
```
3. 在项目文件夹运行Snakemake
```sh
snakemake --cores 32
```

## FAQs
* 如何单模块运行？

    依据rules， 如重新运行物种Venn图
    
    ```sh
    snakemake -R taxa_Venn --cores 32
    ```
* 如何指定输出文件(夹)运行？
    依据output关键词， 如重新生成基因韦恩图

    ```sh
    snakemake -R metagenome_work_out/3.gene_predict/Gene/gene_Venn --cores 32
    ```
* snakemake rule的关键词解释？
    - input 输入文件
    - output 输出文件
    - params 命令行参数
    - log 运行日志
    - shell 执行命令
    - run 执行python 代码
    - threads 单条rules执行线程数
    - priority 任务执行优先级
    - wildcards_constrain 通配符来限制输出文件
