'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import psutil
from builtins import str

def getDataFromMachine():
    cmu=psutil.virtual_memory() #Fetching memory utilization data
    str(cmu).split(",")
    return float(cmu[2])