class Circulo:  # Define o nome da classe
    # __init__() é o método inicializador da classe recebendo
    # um parâmetro: raio
    def __init__(self, raio):  # self faz referencia ao proprio obj
        self.raio = raio  # entãos estamos definindo os atributos
        self.area = 0  # do proprio obj instanciado e os tornando
        self.perimetro = 0  # acessiveis pros outros metodos(def)

    def calc_area(self):  # Definição do método calc_Area
        self.area = 3.1416 * (self.raio ** 2)

    def calc_perimetro(self):  # Definição do método calc_Perimetro
        self.perimetro = 2 * 3.1416 * self.raio
