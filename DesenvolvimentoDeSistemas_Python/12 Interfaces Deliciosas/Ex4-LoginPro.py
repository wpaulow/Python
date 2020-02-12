# Exemplo 3 - Tela de login
from tkinter import *


janela = Tk()

def bt_exit():
    janela.destroy()

janela.resizable(0, 0)
quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)

quadro.place(x=20, y=20)
fonte = ('Arial', '16', 'bold')

lb1 = Label(quadro, text="Login:", font=fonte, pady=10, padx=10)

lb2 = Label(quadro, text="Senha:", font=fonte, pady=10, padx=10)
ed1 = Entry(quadro, font=fonte)
ed2 = Entry(quadro, font=fonte, show="*")
bt1 = Button(quadro, font=fonte, text="Confirmar", fg="Blue",
             activebackground="#A9A9A9", activeforeground="white")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=0, columnspan=2)

photo = PhotoImage(file="img/sair.png")
logo = photo.subsample(20, 20)
btExit = Button(janela, image=logo, bd=0, command=bt_exit)
btExit.place(x=350, y=185)

janela.geometry("400x225+200+200")  #
janela.title("Login")
janela.iconbitmap("img/Sharingan_Icone.ico")
janela.mainloop()