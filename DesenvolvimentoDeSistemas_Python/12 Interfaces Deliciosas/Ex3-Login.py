# Exemplo 3 - Tela de login
from tkinter import *

janela = Tk()  # Cria a tela principal
janela.resizable(0, 0)  # Impede que a telaseja redimensionada
quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)
# Cria um frame com borda de tamanho 2 px com raise(efeito de elevação) e com
# espaço interno horizontal(y) e vertical(x) de 10
quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
fonte = ('Arial', '16', 'bold')  # Define o padrão de fonte
# Criando os componentes
lb1 = Label(quadro, text="Login:", font=fonte, pady=10, padx=10)  # cria a variavel
# lb1 e atribui a ela um Label
lb2 = Label(quadro, text="Senha:", font=fonte, pady=10, padx=10)
ed1 = Entry(quadro, font=fonte)
ed2 = Entry(quadro, font=fonte, show="*")  # Aparece * no lugar da senha
bt1 = Button(quadro, font=fonte, text="Confirmar", fg="Blue",
             activebackground="#A9A9A9", activeforeground="white")
# Exibindo os componentes com grig
lb1.grid(row=0, column=0)  # Define que o Label aparecerá na linha 0 coluna 0
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=0, columnspan=2)  # Mescla a coluna o com a 1 na linha 2
# Configurações da janela
janela.geometry("400x225+200+200")  # Larg x Alt + DistaciaEsq + DistandiaTop
janela.title("Login")  # Define o titulo da janela
janela.mainloop()  # Exibe a janela
