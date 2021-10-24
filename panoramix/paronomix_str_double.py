import json
import os
import time

from tool.get_bin import get_bin
from multiprocessing import Pool
from panoramix.paronomix import panoramix
from panoramix.paronomix_str import panoramix_str


def get_str_to_panoramix_double(path, result_path):
    """
    :param path: path is the path where the binary code of the parsed data is stored
                path is the path of the binary code file, the internal storage is the binary code of each contract address, and the data item contains the basic information of each contract
    :param result_path: result_path stores the results in this path, which is a directory. Each parsing result is stored separately in a json file and saved in this path
    :return:
    """
    list = []
    # First iterate through the folders
    g = os.walk(path)
    # Traverse the results of the analysis and count
    for path, dir_list, file_list in g:
        for file_name in file_list:
            filepath = path + file_name  # The specific file path where each binary code is stored
            list.append(filepath)


    all_num = 0
    time_out = 0

    pool = Pool(processes=4)  # Start four work processes
    for i in list:
        # print(i)
        # print(type(i))
        all_num = all_num + 1
        print(all_num)
        try:
            # if all_num == 100 :
            #     break
            f = open(i, "r")  # Open i, read the string of binary code
            str = f.read()
            # print(str)
            print(str)
            addr_list = address = i.split('/')
            add = addr_list[-1]
            add_list = add.split('.')
            address = add_list[0]


            pool.apply_async(panoramix_str, args=(str, address, result_path,))
        except Exception as e:
            time_out = time_out + 1
            print(e)
            pass
            continue

    pool.close()
    pool.join()
    print("all_num", all_num)
    print("time_out", time_out)
