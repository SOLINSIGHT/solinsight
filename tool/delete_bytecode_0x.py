import json
import os

from tool import save_json


def json_bytecode(path,file,new_path):
    all_num = 0
    bytecode_null = 0

    with open(path+file, 'r') as load_f:
        load_dict = json.load(load_f)
        print(type(load_dict))
        for i in load_dict:
            all_num = all_num +1
            if(i["bytecode"] == "0x"):
                bytecode_null = bytecode_null + 1
                print(all_num)
                print(i["bytecode"])
                load_dict.pop(all_num-1)
            # print(i)
        save_json.new_json(load_dict,new_path+file)
    print("-----------------------------")
    print(bytecode_null)
    print(all_num)

def all_delete_0x(path,new_path):
    for root,dirs,files in os.walk(path):
        for file in files:
            # Get the directory of the file
            print(root)
            print(file)
            # Get file path
            file_name = os.path.join(root,file)
            print(file_name)
            json_bytecode(root,file,new_path)
            # print(os.path.join(root,file))
