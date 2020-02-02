'''
Created on Jan 30, 2020

@author: Siddhartha
'''
import configparser

class ConfigUtil:

    defaultPath = "../../../config/ConnectedDevicesConfig.props"
    def __init__(self):
        self.cp= configparser.ConfigParser()
    
    #Method to fetch the value based on the section and key passed.
    def getValue(self,section, prop):
        return self.cp[section][prop]
    
    # method to check if the there is any data loaded    
    def hasConfigData(self):
        if(len(self.cp)>0):
            return True
        else:
            return False
    # Method to load data   
    def loadConfig(self,filepath):
        try:
            self.cp.read(filepath)
            #print (this.cp.sections())
            return True 
        except:
            self.cp.read("../../../config/ConnectedDevicesConfig.props")
            #print("False")
            return False
        
        