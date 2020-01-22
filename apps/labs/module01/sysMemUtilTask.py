'''
Created on Jan 20, 2020

@author: Siddhartha
'''

import psutil

from builtins import str

def getDataFromMachine():
    cmu=psutil.virtual_memory()
    str(cmu).split(",")
    return cmu[2]