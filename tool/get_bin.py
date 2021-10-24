import struct
import os
def get_bin(filepath):
    """

    :param filepath: The address of the file, including the path plus the name of the contract address of the file
    :return: Returns the size of the binary code file corresponding to this contract address, and the binary string
    """
    binfile = open(filepath, 'r') # Open binary file
    size = os.path.getsize(filepath) # Get file size
    # print(binfile.read())
    s = binfile.read()
    return size, s
    # for i in range(size):
    #     data = binfile.read(1) # Output one byte at a time
    #     print(data)
    # binfile.close()