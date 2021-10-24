# SOLINSIGHT

## Introduction

**SOLINSIGHT** is a prototype tool to help analyze  the effectiveness and limitations of the existing  smart contract decompilation tools. It has been used on a common contract data set.

## Enviroments

Python3.8

[ethervm.io](https://ethervm.io/decompile) : the online decompiler

[panoramix](https://github.com/eveem-org/panoramix) : the offline decompiler 

## Install and Run
```
$ pip install panoramix-decompiler
$ git clone https://github.com/SOLINSIGHT/solinsight.git
$ cd solinsight
$ python main.py source_json_name offline_result_path online_result_path
```
## Example
```
$ python main.py "./dataset/normal_dataset/results-20190801.json" "./result/offline_decompiler_paronomix" "./result/online_decompiler_result/result"
```