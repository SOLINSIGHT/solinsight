import json


def getjson_to_panoramix_single(path,result_path):
    # path is the path of a json file, each data item is stored internally, and the data item contains the basic information of each contract
    # { address, bytecode,function_sighashes,is_erc20,is_erc721,block_timestamp,block_number,block_hash,tx_count}


    paronomix_parse_result = result_path
    f = open(path, )
    data = json.load(f)  # data is a list, and each list is a dictionary, which forms the json format
    all_num = 0
    time_out = 0
    time_out_list = []

    for i in data:
        bytecode = i.get("bytecode")
        address = i.get("address")
        # d = os.popen("cat " + bytecode + " | xargs panoramix")
        print(all_num, ":" + address)
        print("bytecode:" + bytecode)
        print("decompiling ...")
        all_num = all_num + 1
        try:
            # p1 = Process(target=panoramix,args=(i,))
            # p1.start()
            panoramix(i,paronomix_parse_result)
        except Exception as e:
            time_out = time_out + 1
            time_out_list.append(address)
            print(e)
            pass
    print("all_num", all_num)
    print("time_out", time_out)
    print('decolpiler finish!')

