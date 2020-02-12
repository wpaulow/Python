from view.visaoCirculo import VisaoCirculo
# Da pasta view do arquivo visaoCirculo importe a classe VisaoCirculo
from model.circulo import Circulo
# Da pasta model do arquivo circulo importe a classe Circulo


class ControleCirculo:  # Definição da classe

    def __init__(self):  # Metodo inicializador
        self.telaCirculo = VisaoCirculo()  # Instancia um objeto view
        self.meuCirculo = 0  # Inicia todas as variaveis vazias
        # Usando o self essas variaveis estarão
        # acessiveis em todos os metodos(def), sem o self
        # só poderiam ser usadas no def onde foram
        # criadas

    def decidecalc(self):  # Metodo para obter os dados da VisaoCirculo
        opcao = self.telaCirculo.getop()  # Obtém a opção através view
        raio = self.telaCirculo.getraio()  # Obtém a area do circulo
        self.meuCirculo = Circulo(raio)
        if opcao == 1:  # Se a opção esolhida for 1
            self.calcarea()  # Chama o metodo calcarea
        else:  # Senão
            self.calcperimetro()  # Chama o metodo calcperimetro

    def calcarea(self):  # Método de calculo da area
        area = self.meuCirculo.calc_area()  # Chama o método calc_area do obj meuCirculo
        self.telaCirculo.exibearea(area)  # Manda o view exibir
        # a área chamando o método exibearea do obj telaCirculo

    def calcperimetro(self):  # Método de calculo do perimetro
        perimetro = self.meuCirculo.calc_perimetro()  # Chama o método calc_perimetro
        self.telaCirculo.exibeperimetro(perimetro)  # Manda o
        # view exibir o perimetro chamando o método exibeperimetro do obj telaCirculo
