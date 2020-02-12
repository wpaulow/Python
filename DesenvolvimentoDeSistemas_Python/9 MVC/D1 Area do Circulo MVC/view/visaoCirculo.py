class VisaoCirculo:  # Definição da classe

    def start(self):  # Definição do método que inicia a interação com o usuario
        print("Bem vindo ao programa do calculo do circulo!")

    def getop(self):  # Método para obter a volar do opção
        print("O que deseja calcular???")
        op = float(input("1-Área\n2-Perímetro\n->"))
        return op  # Retorna o valor que o usuario digitou

    def getraio(self):  # Método para obter a volar do raio
        raio = float(input("Quantos centimetros tem o raio: "))
        return raio  # Retorna o valor que o usuario digitou

    def exibearea(self, area):  # Método que exibe o resultado da area
        print("A area do circulo é %5.2fcm²!" % area)

    def exibeperimetro(self, perimetro):  # Método que exibe o perimetro
        print("O perímetro do circulo é %5.2fcm!" % perimetro)
