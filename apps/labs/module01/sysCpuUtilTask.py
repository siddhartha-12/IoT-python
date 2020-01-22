'''
Created on Jan 20, 2020

@author: Siddhartha
'''
import psutil

def getDataFromMachine():
    cpup=psutil.cpu_percent(2)
    return cpup


