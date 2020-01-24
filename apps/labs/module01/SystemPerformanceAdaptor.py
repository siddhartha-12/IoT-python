'''
Created on Jan 20, 2020

@author: Siddhartha
'''
import logging
from labs.module01 import sysMemUtilTask,sysCpuUtilTask
from builtins import str

def run():
    mem = sysMemUtilTask.getDataFromMachine()
    cpu = sysCpuUtilTask.getDataFromMachine()
    logging.info("Memory Utilization :" +str(mem) +"%")
    logging.info("Cpu Utilization    :"+ str(cpu) +"%")

    return True