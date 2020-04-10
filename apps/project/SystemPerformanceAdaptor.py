'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import logging
from project import sysMemUtilTask,sysCpuUtilTask

def getSystemUtil():
    mem = sysMemUtilTask.getDataFromMachine()
    cpu = sysCpuUtilTask.getDataFromMachine()
    logging.info("Memory Utilization :" +str(mem) +"%") #Logging memory Utilization
    logging.info("Cpu Utilization    :"+ str(cpu) +"%") #Logging CPU utilization
    return ("\"constrainMemory\":"+str(mem) + "," + "\"constrainCpu\":"+str(cpu))