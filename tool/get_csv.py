import csv
import time
import json
import time
import os

from online_util.http_get import http_get
from online_util.parse_html import parsehtml
from tool.save_file import save_to_file
from tool.write_list_to_json import write_list_to_json


def get_csv_file(path):
    """

    :param path: this is the csv file path
    :return:
    """
    with open(path, 'r') as f:
        all_vul_num = 0
        reader = csv.reader(f)
        s = set()
        column = [row[1] for row in reader]
        for i in column:
            s.add(i)
        print(len(s))
        for i in s:
             print(i)

