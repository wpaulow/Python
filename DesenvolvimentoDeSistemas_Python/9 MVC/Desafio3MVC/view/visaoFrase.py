class VisaoFrase:

    def start(self):
        print("Vamos converter cases alucinadamente?")

    def getFrase(self):
        frase = input("Digite a frase desejada: ")
        return frase

    def getForma(self):
        forma = int(input("Digite o case desejado:\n1-MAIÚSCULA\n2-mínuscula\n3-Só a"
                          "primeira letra da frase maiúscula\n4-Cada Primeira Letra Em "
                          "Maiúscula"))
        return forma


    def exibirErroForma(self):
        print("Opção Inválida!")


    def exibirResultado(self, resultado):
        print(resultado)