# A Large-Scale Empirical Study of Smart Contract Decompilation

## Introduction

In order to answer the above research questions, this paper proposes a large-scale empirical study of smart contracts
Decompile. We first designed and implemented a new software tool prototype to conduct this research.

There are two types of data sets stored in the dataset, one is a common contract data set, and the other is a contract data set containing vulnerable code.

## Enviroments

Python3.8

[ethervm.io](https://ethervm.io/decompile) : the online decompiler

[panoramix](https://github.com/eveem-org/panoramix) : the offline decompiler 

## Install and Run
>pip install panoramix-decompiler
>
>git clone https://github.com/SOLINSIGHT/solinsight.git
>
>cd solinsight
>
>python main.py source_json_name offline_result_path online_result_path

## Example

python main.py "./dataset/normal_dataset/results-20190801.json" "./result/offline_decompiler_paronomix" "./result/online_decompiler_result/result"
