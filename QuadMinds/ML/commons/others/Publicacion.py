
class Publicacion():

    def __init__(self):
        self.titulo = ''
        self.precio = 0
        self.shipping = ''

    def set_titulo(self,Tit):
        self.titulo = Tit

    def set_precio(self,valor):
        self.precio = valor

    def set_shipping(self,valor):
        self.shipping = valor

    def get_titulo(self):
        return self.titulo

    def get_precio(self):
        return self.precio

    def get_shipping(self):
        return self.shipping
