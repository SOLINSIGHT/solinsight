from bs4 import BeautifulSoup

from tool import timeout_decorator


@timeout_decorator.timeout(150)
def parsehtml(url,path):
    """

    :param url: Resolve contract address
    :param path: The path of the folder where the obtained html file is saved
    :return: Return str1 is the data of the first part of the analysis, which is the parsed contract code
             str2 parses the data of the opcode
    """
    path = path +url+".html"
    # print(path)
    htmlfile = open(path, 'r', encoding='utf-8')  # open a file
    htmlhandle = htmlfile.read()  # The format of the first parameter of the method called below should be an html handle, not a file

    soup = BeautifulSoup(htmlhandle, 'lxml')
    list= soup.select('.container div div[class="code javascript"]')
    # str1 = soup.select('.container div div[class="code javascript"]')[0].get_text()
    str1 = ""
    if(len(list)<1):
        print("parse fail!")
    else:
        str1 = list[0].get_text()

    # print()
    # print(str1)\
    # if(soup.select('.container .hljs')[0] < 1):
    #     # print("lose")
    # str2 = soup.select('.container .hljs')[0].get_text()
    str2 = ""
    # print()
    return str1,str2
