class VisaoGeometria:

    def start(self):
        print("Bem vindo ao programa de Geometria!")

    def getforma(self):
        print("Escolha qual forma deseja utilizar nos calculos!")
        forma = int(input("1-Circulo\n2-Retangulo\n->"))
        return forma

    def getraio(self):
        raio = float(input("Quantos centimetros tem o raio: "))  # Entrada de dados
        return raio

    def getaltuta(self):
        altura = int(input("Digite a medida da altura do retangulo: "))
        return altura

    def getlargura(self):
        largura = int(input("Digite a medida da largura do retangulo: "))
        return largura

    def exiberesultretangulo(self, area, perimetro):
        print("A área do retangulo é %5.2fcm²!" % area)
        print("O perímetro do retangulo é %5.2fcm!" % perimetro)

    def exiberesultcirculo(self, area, perimetro):
        print("A área do circulo é %5.2fcm²!" % area)
        print("O perímetro do circulo é %5.2fcm!" % perimetro)

    def msgerro(self):
        print("Opição inválida...")
