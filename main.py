import configparser
import os
import sys
import time
import tool.count
import json
import panoramix.paronomix_double
from insturction.panoramix_large_empirical import panoramix_large
from online_util.online_decompilation import online_decompilation_main
from online_util.online_decompilation import online_decompilation_main1
from online_util.online_decompilation import online_decompilation_main3

from online_util.http_get import http_get
from online_util.parse_html import parsehtml
from tool.save_file import save_to_file
from tool.write_list_to_json import write_list_to_json


conf = configparser.ConfigParser()
a = conf.read("conf/config.ini")
main_path = os.path.abspath('.')+"/"
result_path = main_path+"result/offline_decompiler_paronomix/" # decompiler result save address


if __name__ == '__main__':
	source_json_name = sys.argv[1]
	offline_result_dir = sys.argv[2]
	online_result_dir = sys.argv[3]
    a1, t1, list1 = online_decompilation_main(online_result_dir, source_json_name)
    panoramix.paronomix_double.get_json_to_panoramix_double(source_json_name,result_dir)
