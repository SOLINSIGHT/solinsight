'''
Description: 
LastEditTime: 2021-10-20 22:50:54
'''
# Output columnar stacking diagram of various vulnerabilities

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  
from math import *
import numpy as np
import pandas as pd
import os


csv = pd.read_csv("")# read a csv file
time = np.array(csv.parsetime)
num = np.array(csv.num)
num = [log(i) for i in num]

plt.xlabel('Time (s)')
plt.ylabel('Online Decompiler (Log)')
plt.bar(time[:-2], num[:-2])
plt.savefig("", dpi=300)

plt.show() 

# ===========================================
csv = pd.read_csv("") # read a csv file
time = np.array(csv.parsetime)
num = np.array(csv.num)
num = [log(i) for i in num]

plt.xlabel('Time (s)')
plt.ylabel('Offline  Decompiler (Log)')
plt.bar(time, num)
plt.savefig('', dpi=300) #  save a picture file in local dir

plt.show() 





# from matplotlib.colors import LogNorm
# import matplotlib.pyplot as plt
# import numpy as np


# plt.hist2d(time, num)#, bins=40, norm=LogNorm())
# plt.colorbar()
# plt.show()
