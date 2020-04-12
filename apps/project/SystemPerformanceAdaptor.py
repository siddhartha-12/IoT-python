'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import logging
from project import sysMemUtilTask,sysCpuUtilTask

def getSystemMemoryUtil():
    mem = sysMemUtilTask.getDataFromMachine()
    return (str(mem))

def getSystemCpuUtil():
    cpu = sysCpuUtilTask.getDataFromMachine()
    return (str(cpu))