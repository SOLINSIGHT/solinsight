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
>git clone https://github.com/SOLINSIGHT/solinsight.git
>
>cd solinsight
>
>python main.py source_json_name offline_result_path online_result_path

## Example

python main.py "./dataset/normal_dataset/results-20190801.json" "./result/offline_decompiler_paronomix" "./result/online_decompiler_result/result"

## Code structure
.
├── LICENSE
├── README.md
├── dataset
│   ├── normal_dataset
│   ├── result.csv
│   └── vul_dataset
├── insturction
│   ├── panoramix_large_empirical.py
│   └── vul_bin_run.py
├── main.py
├── online_util
│   ├── http_get.py
│   ├── online_decompilation.py
│   └── parse_html.py
├── panoramix
│   ├── paronomix.py
│   ├── paronomix_double.py
│   ├── paronomix_sigle.py
│   ├── paronomix_str.py
│   └── paronomix_str_double.py
├── result
│   ├── offline_decompiler_paronomix
│   └── online_decompiler_result
└── tool
    ├── count.py
    ├── delete_bytecode_0x.py
    ├── get_bin.py
    ├── get_csv.py
    ├── picture.py
    ├── save_file.py
    ├── save_json.py
    ├── timeout_decorator.py
    └── write_list_to_json.py