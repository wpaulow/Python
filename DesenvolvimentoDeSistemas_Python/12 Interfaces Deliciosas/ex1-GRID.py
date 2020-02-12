from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1", bg="green")
lb2 = Label(janela, text="Label 2", bg="pink")
lb3 = Label(janela, text="Label 3", bg="blue")
lb4 = Label(janela, text="Label 4", bg="red")

lb1.grid(row=3, column=5)
lb2.grid(row=300, column=300)
lb3.grid(row=400, column=500)
lb4.grid(row=500, column=700)


janela.geometry("500x200+200+200")
janela.title("Conhecendo o Grid")
janela.mainloop()

