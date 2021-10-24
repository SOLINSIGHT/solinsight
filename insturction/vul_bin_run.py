import json
import os

from panoramix import paronomix_str_double


def vul_bin_run(path,reult_path):
    """

    :param path: The path of the binary folder
    :param reult_path: Where to store the results
    :return:
    """
    # First iterate through the folders
    g = os.walk(path)
    # Traverse the results of the analysis and make statistics
    for path, dir_list, file_list in g:
        
        for file_name in file_list:
            print(path+file_name)
            # f = open(path + file_name, "r")
            # content = f.read()
            # print(content)

    # paronomix_str_double.get_str_to_panoramix_double(path,reult_path)