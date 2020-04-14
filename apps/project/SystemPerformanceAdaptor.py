'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import logging
from project import sysMemUtilTask,sysCpuUtilTask
# Method for getting memory utilization
def getSystemMemoryUtil():
    mem = sysMemUtilTask.getDataFromMachine()
    return (str(mem))
# Method for getting cpu utilization
def getSystemCpuUtil():
    cpu = sysCpuUtilTask.getDataFromMachine()
    return (str(cpu))