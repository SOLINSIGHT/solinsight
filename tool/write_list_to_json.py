import json
import os


def write_list_to_json(list, json_file_name, json_file_save_path):
    """
    Write list to json file
    :param list:
    :param json_file_name: The name of the json file to be written
    :param json_file_save_path: json file storage path
    :return:
    """
    os.chdir(json_file_save_path)
    with open(json_file_name, 'w') as  f:
        json.dump(list, f)