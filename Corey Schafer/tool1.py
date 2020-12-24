import psutil
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
def __init__(self):
    self.driver = webdriver.Remote(command_executor='http://10.128.220.29:4321', desired_capabilities=self.get_desired_capabilities())
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['name', 'pid'])        
           if processName.lower() in pinfo['name'].lower():
                return pinfo['pid']
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           print (processName +" is not running")

def main(self):
    listOfProcessIds = findProcessIdByName('Avaya IX Workplace')
    aut = self.driver.find_element(By.XPATH,"/*[@ProcessId='%s']".format(listOfProcessIds))
    pass

if __name__ == '__main__':
   main()
