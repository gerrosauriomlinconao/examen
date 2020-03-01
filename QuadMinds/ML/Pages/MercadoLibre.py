from Pages.BasePage import BasePage
import time
from hamcrest import assert_that, equal_to


class MercadoLibre(BasePage):

    def ingresar_categoria_Tecno(self):
        categoria_header = '//a[contains(text(),"Categor")]'
        MercadoLibre.esperar_elemento_clickeable(self,categoria_header)
        MercadoLibre.click(self, MercadoLibre.localizar(self, categoria_header))
        cat_xpath = '//a[contains(text(),"Tecno")]'
        MercadoLibre.esperar_elemento_clickeable(self, cat_xpath)
        MercadoLibre.click(self,MercadoLibre.localizar(self,cat_xpath))

    def ingresar_sub_categoria_ComponentesPc(self):
       subCat = '//a[contains(text(),"Componentes de PC")]'
       MercadoLibre.click(self, MercadoLibre.localizar(self, subCat))

    def filtrar_por_ciudad(self,ciudad):
        #Este metodo hace clic en el filtro de ciudad enviado por parámetro e informa la cantidad que hay para ese filtro
       filtro = '//div[@id="inner-main"]//span[contains(text(),"'
       tmp = '")]'
       xpath_ciudad = filtro + str(ciudad) + tmp
       MercadoLibre.esperar_elemento_clickeable(self, xpath_ciudad)
       MercadoLibre.scroll_to_elemnt(self,xpath_ciudad)
       #el elemernto hermano contiene el valor de la cantidad de elementos:
       xpath_cantidad = xpath_ciudad + '/following-sibling::*[1]'
       MercadoLibre.imprimir(self,'Cantidad de Productos: ')
       cantidad = MercadoLibre.extraer_texto(self,xpath_cantidad)
       #se cortan los paréntesis que vienen en el texto
       texto = cantidad[1:len(cantidad)-1]
       MercadoLibre.imprimir(self,texto)
       MercadoLibre.click(self, MercadoLibre.localizar(self, xpath_ciudad))

    def obtener_datos_item(self, item):
        #guardo los datos de la ultima publicacion en un objeto para luego compararlos
        xpath_precio = '//*[@id="searchResults"]/li[1]/div/a/div/div/span[2]'
        xpath_shipping = '//*[@id="searchResults"]/li[1]/div/a/div/div[2]/span'
        xpath_titulo = '//*[@id="searchResults"]/li[1]/div/a/div/h2/span'
        MercadoLibre.esperar_elemento_clickeable(self,xpath_precio)
        MercadoLibre.imprimir(self,'-----')
        MercadoLibre.imprimir(self, ' Nombre del Item: ')
        titulo = MercadoLibre.extraer_texto(self, xpath_titulo)
        item.set_titulo(titulo)
        MercadoLibre.imprimir(self,titulo)
        MercadoLibre.imprimir(self, '-----')
        MercadoLibre.imprimir(self,' Precio: ')
        valor = MercadoLibre.extraer_texto(self,xpath_precio)
        item.set_precio(valor)
        MercadoLibre.imprimir(self, valor)
        MercadoLibre.imprimir(self, '-----')
        MercadoLibre.imprimir(self, ' Envío: ')
        env = MercadoLibre.extraer_texto(self, xpath_shipping)
        item.set_shipping(env)
        MercadoLibre.imprimir(self, env)
        element_xpath = '//*[@id="searchResults"]/li/div/div/div'
        MercadoLibre.click(self,MercadoLibre.localizar(self,element_xpath))

    def comparar(self,item):
        MercadoLibre.imprimir(self, 'Acá se imprimirá la comparativa: ')
        MercadoLibre.imprimir(self, item.get_precio())
        xpath_titulo = '//*[@class = "ui-pdp-header"]/h1'
        xpath_precio = '//*[@class = "price-tag-fraction"][1]'
        tit = MercadoLibre.extraer_texto(self,xpath_titulo)

        MercadoLibre.imprimir(self, ' ----- ----- ------')
        precio = MercadoLibre.extraer_texto(self,xpath_precio)

        assert_that(tit, equal_to(item.get_titulo()))
        #EN CASO DE SER DIFERENTE, HAMSCRET CORTA LA EJECUCIÓN POR LO QUE NO HACE FALTA PONER UN IF.
        #EN CASO DE DAR TRUE LA COMPARATIVA, CONTINUA LA EJECUCIÓN.
        #Se puede comprobar descomentando la siguiente linea:
        #assert_that(0, equal_to(item.get_precio()))
        MercadoLibre.imprimir(self, ' El Titulo es el Mismo ')
        assert_that(precio, equal_to(item.get_precio()))
        MercadoLibre.imprimir(self, ' El Precio es el Mismo ')