from selenium import webdriver
#Esta clase es la encargada de manejar el webdriver.
class Driver(object):
#En principio se utilizará chromeWebdriver
#En Caso de querer usar otro Driver (firefox, opera, phantom, etc), debería crearse el siguiente constructor:
#
# def __init__(self,driver):
#    driver = driver
#----------------------------------------------------------------
    def __init__(self):
        executable_path = "../drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path)

    def get_driver(self):
        return self.driver

    def visit(self,url):
        self.driver.get(url)

    def maximizar(self):
        self.driver.maximize_window()

    def close(self):
      self.driver.close()