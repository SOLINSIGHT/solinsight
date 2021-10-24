import subprocess
import time
from tool import timeout_decorator
from tool import save_json

@timeout_decorator.timeout(60)
def panoramix(i,result_path):
    """
    :param i: i is json data item, in the form of a dictionary;
     :param result_path: is to store the result in a path
     :return:
    """
    # 一： How os.popen is executed
    # d = os.popen("panoramix " + i.get("bytecode"))
    # output = d.read()
    # print(output)
    # subprocess_popen("panoramix "+bytecode)
    # 二：subprocess.check_output（）
    out_bytes = " "

    bytecode = i.get("bytecode")
    # print(bytecode)
    address = i.get("address")
    print(address)

    # print(address+" decompiler....")
    length = 0
    try:
        try:
            i["ParseFlag"] = False  # Initial state assignment, success or failure of parsing, failure by default
            i["error_message"] = ""
            i["parsetime"] = 0
            i["size"] = 0
            i["parse_information"] = ""
            i["contract"] = ""
            start = time.time()  # Record the time when the bytecode started to be parsed
            out_bytes = subprocess.check_output(['panoramix', bytecode], stderr=subprocess.STDOUT) # the decompiler will end up in 30s/60s,and then the json file will not save
            end = time.time()  # Record the time when the bytecode is parsed
            str = out_bytes.decode('utf-8')
            # print(out_bytes.decode('utf-8'))
            print("print(-------------------------------------------)")
            list = str.split("# Palkeoramix decompiler. ", 1)

            interval = end - start
            i["parsetime"] = interval


            length = len(list)
            # list[0] Inside is paromix parsing process information
            # list[1] The inside is the source code for successful analysis. If there is no source code, the analysis failed. For example, if the list pointer is out of bounds, it means the analysis failed.
            # Create a folder for them?

            if (length == 2):
                i["ParseFlag"] = True
                i["parse_information"] = list[0]
                i["contract"] = list[1]
                i["size"] = len(list[1])
            if list[0].find("Timeout") != -1:
                i["error_message"] = "Timeout"
            # if list[0].find("C")


            name = result_path + address +".json"
            save_json.new_json(i,name) # This function is to create a new json file, the second parameter is the name of the file, i represents the content of the stored file
        except subprocess.TimeoutExpired as e:
            out_bytes = e.output  # Output generated before error
            code = e.returncode  # Return code
    except subprocess.CalledProcessError as e:
        out_bytes = e.output  # Output generated before error
        code = e.returncode  # Return code
