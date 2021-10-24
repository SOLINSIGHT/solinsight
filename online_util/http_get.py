
# online decompiler tool
import requests
from tool.save_file import save_to_file


def http_get(contract,save_path):
    """

    :param contract: The address of the contract contract
    :param save_path: Save the html file obtained according to this address in this address
    :return: none
    """
    url = "https://ethervm.io/decompile?address="+contract+"&network="  # Request interface
    req = requests.get(url)  # send request
    # print(req.text)  # Get the request, get the json format
    save_to_file(save_path+contract+".html",req.text)
    # print(json.load(req.text))  # Get the request, get the dictionary format
    # print(type(req.text))

