'''
Created on Jan 30, 2020

@author: Siddhartha
'''
import configparser

class ConfigUtil:

    def __init__(self):
        self.cp = None

    def getValue(self,section, prop):
        return self.cp[section][prop]
        
    def hasConfigData(self):
        if(len(self.fileprop)>0):
            return True
        else:
            return False
        
    def loadConfig(self,filepath):
        try:
            self.cp= configparser.ConfigParser()
            self.cp.read(filepath)
            #print (this.cp.sections())
            return True 
        except:
            print("False")
            return False
        
        