def retirar_mascara(a):
    cpfsemponto = a.split(".")
    print(cpfsemponto)
    cpfsemhifen = cpfsemponto[1].split("-")
    #listacpfseparado = (listacpfseparado[0], listacpfseparado[1] , listacpfseparado[2], listacpfseparado[3] )
    cpfsemmasc ="".join(cpfsemponto[0],cpfsemponto[1],cpfsemhifen[0],cpfsemhifen[1])
    print(cpfsemmasc)


cpf = (input("Digite seu CPF:"))
codigo = input("Digite 1 para CPF com máscara e 2 para CPF sem máscara:")

if codigo == 1:
    retirar_mascara(cpf)
'''elif codigo == 2:
    print("ashdfsoi")
else:
    print("opção inválida")'''
