import time
from behave import *
import sys
# Corrige un problema con los import
sys.path.append('../')
from commons.Driver import Driver
from Pages.MercadoLibre import MercadoLibre
from commons.others.Publicacion import Publicacion

@given('Ingresar al Sitio de Mercado Libre')
def step_impl(context):
   context.driver = Driver()
   context.driver.maximizar()
   url = "https://www.mercadolibre.com.ar/"
   context.driver.visit(url)

@when('Ir a la Categoria Tecnologia -> Computacion -> Componentes de PC')
def step_impl(context):
    MercadoLibre.ingresar_categoria_Tecno(context.driver)
    MercadoLibre.ingresar_sub_categoria_ComponentesPc(context.driver)

@when('Filtrar por {ciudad} e Informar la Cantidad Listada.')
def step_impl(context,ciudad):
    MercadoLibre.filtrar_por_ciudad(context.driver,ciudad)

@when('Informar los Datos de la Ultima Publicacion y acceder')
def step_impl(context):
    context.item = Publicacion()
    MercadoLibre.obtener_datos_item(context.driver,context.item)

@Then('Verificar los datos de la Publicacion')
def step_impl(context):
    MercadoLibre.comparar(context.driver,context.item)