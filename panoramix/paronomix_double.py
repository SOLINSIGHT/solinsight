import json
from multiprocessing import Pool
from panoramix.paronomix import panoramix


def get_json_to_panoramix_double(path,result_path):
    """
   :param path: path is the path of the json file of the parsed data, which saves all solidty contract data in the form of a json file
                 path is the path of a json file, each data item is stored internally, and the data item contains the basic information of each contract
                 {address, bytecode,function_sighashes,is_erc20,is_erc721,block_timestamp,block_number,block_hash,tx_count}
     :param result_path: result_path Store the result in this path, which is a directory. Each parsing result is saved separately in a json file and saved in this path
     :return:
    """
    # list = []

    f = open(path, )
    data = json.load(f)  # data is a list, each list is a dictionary, which forms the json format
    all_num = 0
    time_out = 0

    pool = Pool(processes=4) # Start four work processes ///#Run 3
    for i in data :
        all_num = all_num + 1
        print(all_num)
        try:
            # if all_num == 100 :
            #     break
            pool.apply_async(panoramix, args=(i,result_path,))
        except Exception as e:
            time_out = time_out + 1
            print(e)
            pass
            continue

    pool.close()
    pool.join()
    print("all_num", all_num)
    print("time_out", time_out)
    # parsejson.new_json(list, "result"+ ".json")
    # with open(result_path, 'w', encoding='utf-8') as file:
    #     json.dump(list, file, ensure_ascii=False)
