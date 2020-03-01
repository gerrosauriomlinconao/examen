from time import sleep
#
# from selenium import webdriver
# executable_path = "../ML/drivers/chromedriver.exe"
# driver = webdriver.Chrome(executable_path)
#
# driver.maximize_window()
# url = "https://www.neoteo.com"
# driver.get(url)
# sleep(50)
#
# driver.close()
#########
#Corrige un problema con los import
import sys
sys.path.append('../')
from ML.commons import Driver
#from ML.commons.Driver import Driver


c = Driver()
url =  "https://www.neoteo.com"
c.maximizar()
c.visit(url)

sleep (50)
