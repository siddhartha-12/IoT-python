'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import psutil

def getDataFromMachine():
    cpup=psutil.cpu_percent(2) #Fetching PC utilization  
    return float(cpup)


