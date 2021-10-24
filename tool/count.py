import os
import json
import numpy as np
import matplotlib.pyplot as plt


class item:
    def __init__(self, parsetime, size):
        self.parsetime = parsetime
        self.size = size

def count(path):
    all_num = 0
    parse_success = 0
    parse_fail = 0
    timeout_num = 0
    g = os.walk(path)
    item_list = []
    # Traverse the results of the analysis and make statistics
    for path, dir_list, file_list in g:
        for file_name in file_list:
            f = open(path + file_name, "r")
            all_num = all_num + 1
            content = f.read()
            # try:
            a = json.loads(content)
            # print(a[0]["address"])
            # First read the file and record the total data
            ParseFlag = a[0]["ParseFlag"]  # Parse each data, parseflag indicates success or failure of interpretation
            size = a[0]["size"]
            parsetime = a[0]["parsetime"]

            i1 = item(size,parsetime)
            item_list.append(i1)

            if size!=0 :
                k = size / parsetime
            else:
                k = 0
            # print(a[0]["address"],k)
            if ParseFlag == True:
                parse_success = parse_success + 1
            else:
                # print("address :" + a[0]["address"])
                # print("bytecode :  " + a[0]["bytecode"])
                parse_fail = parse_fail + 1
            #
            if a[0]["parse_information"].find("Timeout") != -1:  # Judging whether there is a Timeout timeout from whether there is Timeout in the parsed information
                print("address :" + a[0]["address"])
                print("parse_information" + a[0]["parse_information"])
                print(a[0]["address"] +"-------------------------timeout!")
                timeout_num = timeout_num + 1
            # if not(a[0]["parsetime"] < float(29.9)) :
            #     print(a[0]["address"] + "-------------------------timeout!")
            #     timeout_num = timeout_num + 1

    # digram(item_list)
    print("success    :", parse_success)
    print("fali       :", parse_fail)
    print("timeout_num:", timeout_num)
    print("all_num    :", all_num)
