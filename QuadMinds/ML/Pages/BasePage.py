import sys
#Esta es la clase base de la cual todas las necesarias heredaran de aqui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def click(self,element):
        element.click()

    def localizar(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    def scroll_to_elemnt(self,elem):
        #scroll vertical
        elem = BasePage.localizar(self,elem)
        self.driver.execute_script("return arguments[0].scrollIntoView();",elem)

    def extraer_texto(self,elem):
        elem = BasePage.localizar(self, elem)
        elem = elem.text
        return elem

    def imprimir(self,valor):
        #evito usar el print, debido a que la stout no está habilitada con behave y debo utilizar la de sys
        texto = str(valor)
        sys.stdout.write(texto+'\n')

    def esperar_elemento_cargado(self,elem):
        wait= WebDriverWait(self.driver,60)
        element = wait.until(EC.presence_of_element_located((By.XPATH,elem)))

    def esperar_elemento_clickeable(self,elem):
        wait= WebDriverWait(self.driver,60)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,elem)))
