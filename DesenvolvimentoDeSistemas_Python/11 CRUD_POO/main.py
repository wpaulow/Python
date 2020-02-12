from conectabanco import ConectaBanco


banco = ConectaBanco() #instancia um objeto do tipo ConectaBanco

tabela = "aluno"
'''campos = "idaluno, nome, dtnasc, endereco, cidade, estado, email"
valores = "default, 'Mauricio Vianna', '1998-09-30', 'Rua D nº 333', 'Cotia', 'SP', 'mvianna007@gmail.com'"

banco.insert(tabela, valores, campos)

updateset = "nome = 'Vitória Mendes'"
updatewhere = "idaluno = 2"


banco.update(tabela, updateset, updatewhere)'''

banco.delete(tabela, "idaluno = 4")

regSelect = banco.select("*", "aluno") # Executa o método select atribuindo
                                            #o resultado na variável select
for registro in regSelect: #o resultado na variável regSelect
    print(registro) #para cada registro na tupla de registros