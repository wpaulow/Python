from tkinter import *
from conectaBanco import ConectaBanco


def btExit():
    janela.destroy()


def btSalvar():
    idProduto = edId.get()
    nome = edNome.get()
    marca = edMarca.get()
    dtVal = edVal.get()
    banco = ConectaBanco()
    valores = ("'%s','%s','%s','%s'" % (idProduto, nome, marca, dtVal))
    sets = ("nome='%s',marca='%s',dtVal='%s'" % (nome, marca, dtVal))
    where = ("idProduto = '%s'" % idProduto)
    try:
        reg = banco.select("*", "produtos", where)
        if not reg:
            banco.insert("produtos", valores)
            lbMensagem["text"] = "Cadastrado com sucesso!"
            btDelete['state'] = "normal"
        else:
            banco.update("produtos", sets, where)
            lbMensagem["text"] = "Registro atualizado!"
    except:
        lbMensagem["text"] = "Erro no BD, notifique o ADM!"


def btBuscar():
    edNome['state'] = "normal"
    edVal['state'] = "normal"
    edMarca['state'] = "normal"
    btSalvar['state'] = "normal"
    edNome.delete(0, END)
    edMarca.delete(0, END)
    edVal.delete(0, END)
    idProduto = edId.get()
    banco = ConectaBanco()
    where = ("idProduto = '%s'" % idProduto)
    try:
        reg = banco.select("*", "produtos", where)
        if not reg:
            lbMensagem["text"] = "Registro não encontrado!"
            btDelete['state'] = "disabled"
        else:
            lbMensagem["text"] = "Registro encontrado!"
            btDelete['state'] = "normal"
            for registro in reg:
                edNome.insert(0, registro[1])
                edMarca.insert(0, registro[2])
                edVal.insert(0, registro[3])
    except:
        lbMensagem["text"] = "Erro no BD, notifique o ADM!"


def btDeletar():
    idProduto = edId.get()
    banco = ConectaBanco()
    where = ("idProduto = '%s'" % idProduto)
    try:
        banco.delete("contatos", where)
        btDelete['state'] = "disabled"
        lbMensagem["text"] = "Registro deletado com sucesso!"
        edId.delete(0, END)
        edNome.delete(0, END)
        edMarca.delete(0, END)
        edVal.delete(0, END)
        edNome['state'] = "disabled"
        edVal['state'] = "disabled"
        edMarca['state'] = "disabled"
        btSalvar['state'] = "disabled"
    except:
        lbMensagem["text"] = "Erro no BD, notifique o ADM!"


janela = Tk()  # Cria a tela principal
janela.resizable(0, 0)
quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)
quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
fonte = ('Arial', '16', 'bold')  # Define o padrão de fonte

# Criando os componentesdo formulario
lbId = Label(quadro, text="IdProduto:", font=fonte, pady=10, padx=10)
lbNome = Label(quadro, text="Nome:", font=fonte, pady=10, padx=10)
lbMarca = Label(quadro, text="Marca:", font=fonte, pady=10, padx=10)
lbVal = Label(quadro, text="Validade:", font=fonte, pady=10, padx=10)
edId = Entry(quadro, font=fonte, width=25)
edNome = Entry(quadro, font=fonte, width=25, state="disabled")
edMarca = Entry(quadro, font=fonte, width=25, state="disabled")
edVal = Entry(quadro, font=fonte, width=25, state="disabled")
btSalvar = Button(quadro, font=fonte, text="Salvar", fg="Blue", state="disabled",
                  activebackground="#A9A9A9", activeforeground="white", command=btSalvar)
btDelete = Button(quadro, font=fonte, text="Excluir", fg="Blue", state="disabled",
                  activebackground="#A9A9A9", activeforeground="white", command=btDeletar)

# Exibindo os componentes do formulario com grid
lbId.grid(row=0, column=0)
lbNome.grid(row=1, column=0)
lbMarca.grid(row=2, column=0)
lbVal.grid(row=3, column=0)
edId.grid(row=0, column=1)
edNome.grid(row=1, column=1)
edMarca.grid(row=2, column=1)
edVal.grid(row=3, column=1)
btSalvar.grid(row=4, column=0)
btDelete.grid(row=4, column=1)

# criando o botão de busca
photoLupa = PhotoImage(file="img/lupa2.png")
logoLupa = photoLupa.subsample(15, 15)
btBusca = Button(quadro, image=logoLupa, bd=0, command=btBuscar)
btBusca.grid(row=0, column=3)

# criando o botão de sair
photoSair = PhotoImage(file="img/sair.png")
logoSair = photo