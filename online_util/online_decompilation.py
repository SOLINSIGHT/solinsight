import json
import time
import os
import csv
from online_util.http_get import http_get
from online_util.parse_html import parsehtml
from tool.save_file import save_to_file
from tool.write_list_to_json import write_list_to_json



def online_decompilation_main3(online_decompiler_result_save_file,solidity_code_result,opcode_result,html_path,path):
    """
    :param online_decompiler_result_save_file: Store all the contract information in the name result.json, and then save it in this folder
    :param solidity_code_result: The address of the folder where the source code of the contract obtained by parsing the file is stored
    :param opcode_result: The operation code of the contract obtained by parsing the address of the folder that should be stored
    :param html_path: Store the html file in this folder, read the html file in the html folder for analysis
    :param path: All address information is stored in this path
    :return:
    """
    list = []
    list2 = []
    all_num = 0
    time_out = 0
    s = set()

    with open("", 'r') as f:# read vul csv file
        all_vul_num = 0
        reader = csv.reader(f)
        column = [row[1] for row in reader]
        for i in column:
            s.add(i)

    for j in s:
        all_num  =all_num +1
        print(all_num)
        url = j
        dict = {"address": url}
        dict["parse_lose"] = False
        dict["parse_timeout_information"] = ""
        start = time.time()
        try:
            http_get(url,
                     html_path)  # Get the address of the contract, crawl the content of the contract at that address, and then store the web page in the address of a folder in html_path
        except Exception as e:
            time_out = time_out + 1
            list2.append(url)
            print(e)
            pass
            continue
        # dict["parsetime"] = 0
        # dict["size"]
        str1, str2 = parsehtml(url, html_path)  # Parse the html file corresponding to the contract
        if (str1 == ""):
            dict["parse_lose"] = True
            dict["parse_information"] = "parse html fail~!"
        end = time.time()
        dict["parsetime"] = end - start
        dict["size"] = len(str1)
        # print("url",url)
        # print(end-start)
        save_to_file(solidity_code_result + url + ".sol", str1)
        save_to_file(opcode_result + url + ".txt", str2)
        list.append(dict)  # Save the acquired contract information in the list, and then save the list in a file

    write_list_to_json(list, result_json_name, online_decompiler_result_save_file)
    return all_num, time_out, list2
    # Write the list into a file, the list contains all the information obtained by the parsed contract, and then save it in a folder named result.json


def online_decompilation_main(result_path,path):
    """
    :param online_decompiler_result_save_file: Store all the contract information in the name result.json, and then save it in this folder
    :param solidity_code_result: The address of the folder where the source code of the contract obtained by parsing the file is stored
    :param opcode_result: The operation code of the contract obtained by parsing the address of the folder that should be stored
    :param html_path: Store the html file in this folder, read the html file in the html folder for analysis
    :param path: All address information is stored in this path
    :return:
    """
    # url = input("please input the contract tx:")
    # url = sys.argv[0]
    online_decompiler_result_save_file = result_path +"result/"
    solidity_code_result = result_path + "source_code_path/"
    opcode_result = result_path + "opcode_path/"
    html_path = result_path + "html_path/"


    f = open(path, )
    data = json.load(f)  # data is a list, and each list is a dictionary, which forms the json format
    all_num = 0
    time_out = 0
    list = []

    l1 = path.split("/")
    list2 = []
    result_json_name = l1[-1]

    for i in data:
        print(all_num,end=' ')
        all_num = all_num+1

        url = i.get("address")
        dict = {"address":url}
        dict["tx_count"] = i.get("tx_count")
        dict["parse_lose"] = False
        dict["parse_timeout_information"] = ""
        start = time.time()
        try:
            http_get(url,html_path) # Get the address of the contract, crawl the content of the contract at that address, and then store the web page in the address of a folder in html_path
        except Exception as e:
            time_out = time_out + 1
            list2.append(url)
            print(e)
            pass
            continue
        # dict["parsetime"] = 0
        # dict["size"]
        str1, str2 = parsehtml(url,html_path) # Parse the html file corresponding to the contract
        if(str1==""):
            dict["parse_lose"] = True
            dict["parse_information"] = "parse html fail~!"
        end = time.time()
        dict["parsetime"] = end - start
        dict["size"] = len(str1)
        # print("url",url)
        # print(end-start)
        save_to_file(solidity_code_result + url + ".sol", str1)
        save_to_file(opcode_result + url + ".txt", str2)
        list.append(dict) # Save the acquired contract information in the list, and then save the list in a file


    write_list_to_json(list,result_json_name ,online_decompiler_result_save_file)
    return all_num,time_out,list2
    # Write the list into a file, the list contains all the information obtained by the parsed contract, and then save it in a folder named result.json





def online_decompilation_main1(online_decompiler_result_save_file,solidity_code_result,opcode_result,html_path,path):
    """
    :param online_decompiler_result_save_file: Store all the contract information in the name result.json, and then save it in this folder
    :param solidity_code_result: The address of the folder where the source code of the contract obtained by parsing the file is stored
    :param opcode_result: The operation code of the contract obtained by parsing the address of the folder that should be stored
    :param html_path: Store the html file in this folder, read the html file in the html folder for analysis
    :param path: All address information is stored in this path
    :return:
    """
    # url = input("please input the contract tx:")
    # url = sys.argv[0]

    f = open(path, )
    data = json.load(f)  # data is a list, and each list is a dictionary, which forms the json format
    all_num = 0
    time_out = 0
    list = []

    l1 = path.split("/")
    list2 = []
    result_json_name = l1[-1]

    for i in data:
        list3 = i.get("list")
        for j in list3:
            print(all_num, end=' ')
            all_num = all_num + 1
            print(j)
            url = j
            dict = {"num": all_num}
            dict["url"] = url
            dict["parse_lose"] = False
            dict["parse_timeout_information"] = ""
            start = time.time()
            try:
                http_get(url,
                         html_path)  # Get the address of the contract, crawl the content of the contract at that address, and then store the web page in the address of a folder in html_path
            except Exception as e:
                time_out = time_out + 1
                list2.append(url)
                print(e)
                print("get html fail!")
                pass
                continue

            str1, str2 = parsehtml(url, html_path)  # Parse the html file corresponding to the contract
            if (str1 == ""):
                dict["parse_lose"] = True
                dict["parse_information"] = "parse html fail~!"
            end = time.time()
            dict["parsetime"] = end - start
            dict["size"] = len(str1)
            print("url",url)
            # print(end-start)
            save_to_file(solidity_code_result + url + ".sol", str1)
            save_to_file(opcode_result + url + ".txt", str2)
            list.append(dict)  # Save the acquired contract information in the list, and then save the list in a file

    write_list_to_json(list,result_json_name ,online_decompiler_result_save_file)
    return all_num,time_out,list2
    # Write the list into a file, the list contains all the information obtained by the parsed contract, and then save it in a folder named result.json