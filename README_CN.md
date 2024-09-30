# pandora：收集了一些日常使用频率较高的简单功能。

[中文](./README_CN.md) | [English](./README.md)

## 1. 简介
在日常使用电脑时，通常我们只需要点击鼠标即可安装目标软件、运行软件、并实现一些功能。例如撰写一个说明文档，我们只需要双击Word，即可打开一个空白文档，写入内容后，点击鼠标保存即可完成文档撰写。

而在日常的测序数据分析过程当中，通常我们需要大量的内存和CPU来进行计算，例如宏基因组`15Gb`左右数据的组装，`megahit`需要大概`50~80G`的内存和10个CPU核。普通的电脑肯定是无法满足这样的计算资源需求的，所以大部分情况下需要使用HPC系统来完成这些计算。

目前常见的HPC分两种：基于云端的和基于终端命令行的。基于云端的，即云计算，将数据分析的流程部署在HPC系统，并给这些流程包装一个操作页面，让用户可以通过鼠标点击实现想要进行的分析内容。这样的方式使得用户操作起来非常的方便。但目前基于云端的云计算依然存在很多限制，例如针对不同的样本，需要采取不同的分析流程，这就使得分析流程很难统一部署，极大的增加了云计算流程开发和部署的工作量。而基于终端命令行的方式，相比之下就显得更加的灵活，用户可以自由的根据需要改变分析流程，串联流程等。只需要用户掌握一些`bash`命令。

在HPC上分析数据时，经常会遇到各种各样的问题，例如需要改变数据格式等。因为这样的功能不是很复杂，所以并没有集成的工具。而`pandora`的目标就是帮助用户在数据分析的过程中更快速的查看分析结果并串接到流程的下一步。`pandora`中收录了很多小功能的代码，方便用户调用。用户在安装了这个工具包之后，即可直接使用包里包含的功能，例如将`fastq`文件转换为`fasta`文件，用户只需要调用`fq2fa`命令即可。

希望这个小工具可以帮助到你。

`pandora`目前包含的命令有：

- `fq2fa`: 将`fastq`格式转换为`fasta`格式，`fasta`格式序列是`stdout`实时输出到屏幕。如果想要将`fasta`文件写入文件，只需用`>`重定向到一个文件即可。

- `check_phred`: 检查输入序列的平均`Phred`值。这个功能将提取文件中指定数量的序列，读取每一条序列的所有`ASCII`值及最小`ASCII`值，最后`stdout`所有读取的`ASCII`值的平均值、所有最小`ASCII`值的平均值和标准差。

- `extract_seq`: 输入序列`id`(用空格键隔开)或一个包含序列`id`的文件（一行一个序列`id`），提取对应的匹配/不匹配的序列。当提供`--unmatch`参数时，将打印除提供的`id`之外的所有序列。

- `fxlength`: 打印输出所有输入序列的长度。输出的格式为<序列`id`>TAB<序列长度>。

- `avglength`: 打印输出所有输入序列的平均长度。读入一个序列文件，打印输出这些序列的平均长度。

- `summary_mag`: 读入`CheckM/CheckM2`的结果，统计高质量MAG的数量情况。读入参数`-i`提供的一个或多个`CheckM/CheckM2`输出的MAG的质量统计文件之后，统计每一个文件里基因组完整度高于`--completeness`且污染度低于`--contamination`的基因组数量，这些MAG定义为目标MAG。整合了所有的目标MAG之后，以`5`为步长，统计完整度和污染度分别从`100`递减和`20`递增时的MAG数量。例如当定义`--completeness 90 --contamination 10`时，将统计输出完整度`100`且污染度为`0`时MAG的数量情况，完整度高于`95`且污染度低于`5`时MAG的数量情况，以及完整度高于`90`且污染度低于`10`时MAG的数量情况。

- `abs2rel`: 在绝对丰度的表格中对每一列（样本）计算相对值并插入该表格中。

## 2. 安装
pandora已经打包上传到PyPI，可使用`pip`直接进行安装
```
$ pip install pandora-microbiome
```

## 3. 使用
`pandora`中包含的所有命令都可以直接调用，满足不同的场景需求。查看`pandora`中的命令：
```
$ pandora -h
```
```
usage: pandora [-h] [-v] {fq2fa,fxlength,avglength,check_phred,extract_seq,summary_mag,abs2rel} ...

positional arguments:
  {fq2fa,fxlength,avglength,check_phred,extract_seq,summary_mag}
    fq2fa               convert fastq to fasta.
    fxlength            count sequence length.
    avglength           average length of input sequences.
    check_phred         check fastq Phred vaule.
    extract_seq         extract sequences using id.
    summary_mag         summary high quality mag.
    abs2rel             insert relative abundance for each sample.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         print version information
```

### 3.1 `fq2fa`
将`fastq`转换为`fasta`格式。可以通过使用`pandora fq2fa -h`查看详细信息 。
```
$ pandora fq2fa -h
```
```
usage: pandora fq2fa [-h] [-v] -i FQ

optional arguments:
  -h, --help      show this help message and exit
  -v, --version   print version information
  -i FASTQ, --fastq FASTQ  input fastq file (.gz).
```

#### 3.1.1 实例
```
$ pandora fq2fa -i test.fastq.gz > test.fasta
$ pandora fq2fa -i test.fastq.gz | gzip > test.fasta.gz
```

### 3.2 `check_phred`
检查输入文件中序列的`Phred`值。通过使用`pandora check_phred -h`查看详细信息。
```
$ pandora check_phred -h
```
```
usage: pandora check_phred [-h] [-v] -i FASTQ [-n NUM]

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      print version information
  -i FASTQ, --fastq FASTQ     input fastq file.
  -n NUM, --num NUM  number of sequences for Phred check (1000).
```

#### 3.2.1 实例
```
$ pandora check_phred -i test.fastq.gz -n 10000
```

### 3.3 `extract_seq`
根据输入的序列`id`提取序列。通过使用`pandora extract_seq -h`查看详细信息。
```
$ pandora extract_seq -h
```
```
usage: pandora extract_seq [-h] [-v] [-i SEQID | -l IDLIST] -s SEQ [-q]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         print version information
  -i SEQID, --seqid SEQID
                        sequence id to extract, seperate by " ".
  -l IDLIST, --idlist IDLIST
                        id list file to extract.
  -s SEQUENCE, --sequence SEQUENCE     input sequence file.
  -q, --fastq           set if input is fastq.
```

#### 3.3.1 实例
提取匹配输入`id`的序列:
```
$ pandora extract_seq -i Filt9 -s test.fa > extracted_Filt9.fa
$ pandora extract_seq -l seq_list -s test.fa > extracted_all.fa
```

提取不匹配输入`id`的序列:
```
$ pandora extract_seq -i Filt9 -s test.fa -u
```


### 3.4 `fxlength`
统计输入的序列文件中每一条序列的长度。通过使用`pandora fxlength -h`查看详细信息
```
$ pandora fxlength -h
```
```
usage: pandora fxlength [-h] [-v] -s SEQ [-p]

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      print version information
  -s SEQUENCE, --sequence SEQUENCE  input sequence file.
  -p, --plot         Set to plot a histogram for length.
```

#### 3.4.1 实例
```
$ pandora fxlength -s test.fa --plot
$ pandora fxlength -s test_1.fa.gz --plot
```

### 3.5 `avglength`
计算输入的序列文件中所有序列的平均长度。通过使用`pandora avglength -h`查看详细信息。
```
$ pandora avglength -h
```
```
usage: pandora avglength [-h] [-v] -s SEQUENCE [-p]

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      print version information
  -s SEQUENCE, --sequence SEQUENCE  input sequence file.
  -p, --plot         set to plot a histogram for length
```

#### 3.5.1 实例
```
$ pandora avglength -s test.fa --plot
$ pandora avglength -s test_1.fq.gz --plot
```

### 3.6 `summary_mag`
根据`CheckM/CheckM2`的结果，统计高质量MAG的数量情况。通过使用`pandora summary_mag -h`查看详细信息。
```
$ pandora summary_mag -h
```
```
usage: pandora summary_mag [-h] [-v] -i INPUT [INPUT ...] [-cp COMPLETENESS] [-ct COMTAMINATION]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Print version information
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        input stats file from CheckM, seperate by " ".
  -cp COMPLETENESS, --completeness COMPLETENESS
                        stat genomes with completeness above this value (80).
  -ct COMTAMINATION, --comtamination COMTAMINATION
                        stat genomes with comtamination below this value (20).
```

#### 3.6.1 实例
```
$ pandora summary_mag -i checkm_result.txt -cp 80 -ct 20
```

### 3.7 `abs2rel`
在绝对丰度的表格中对每一列（样本）计算相对丰度并插入该表格中。通过使用`pandora abs2rel -h`查看详细信息。
```
$ pandora abs2rel -h
```
```
usage: pandora abs2rel [-h] [-v] -i TABLE [-o OUT_TABLE]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         print version information
  -i TABLE, --table TABLE
                        input table, column represents sample, row represents OTU, species, MAG etc.
  -o OUT_TABLE, --out_table OUT_TABLE
                        output table, print if not set.
```

#### 3.7.1 实例
```
$ pandora abs2rel -i abundance.table.xls -o abundance.table.relative.xls
```

## 4. 贡献
欢迎为这个项目做出贡献。你可以开启一个问题（[issue](https://github.com/lijierr/pandora/issues)）或提交一个拉取请求（pull request）。

## 5. 联系
这个仓库由Jie Li(https://github.com/lijierr)开发和维护。
