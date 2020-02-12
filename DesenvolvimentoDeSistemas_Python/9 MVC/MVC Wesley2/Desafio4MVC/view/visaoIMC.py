class VisaoIMC:

    def start(self):
        print("Vamos calcular seu IMC, cidadã(o) brasileir@?!")


    def getPeso(self):
        peso = float(input("Informe seu peso, querid@: "))
        return peso


    def getAltura(self):
        altura = float(input("Informe a sua altura, querid@: "))
        return altura


    def exibirResultado(self, resultado):
        print("O seu IMC é %5.2f" % resultado)


    def exibirCategoriaAbaixoDoPeso(self):
        print("Abaixo do peso!")


    def exibirCategoriaPesoNormal(self):
        print("Seu peso está normal.")


    def exibirCategoriaSobrepeso(self):
        print("Você está acima do peso recomendado.")


    def exibirCategoriaObesoI(self):
        print("Você está na obesidade I!")


    def exibirCategoriaObesoII(self):
        print("Você está na obesidade II!!")


    def exibirCategoriaObesoIII(self):
        print("Você está na obesidade III!!!")
