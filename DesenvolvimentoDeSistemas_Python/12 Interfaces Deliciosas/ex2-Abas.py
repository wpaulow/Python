from tkinter import *
from tkinter.ttk import *

janela = Tk()

abas = Notebook(janela, width=490, height=290)

frame_aba1 = Frame(abas)
frame_aba2 = Frame(abas)
frame_aba3 = Frame(abas)

label1 = Label(frame_aba1, text="Esse e o frame 1")
label2 = Label(frame_aba2, text="Esse e o frame 2")
label3 = Label(frame_aba3, text="Esse e o frame 3")

label1.grid()
label2.grid()
label3.grid()

abas.add(frame_aba1, text="Aba 1")
abas.add(frame_aba2, text="Aba 2")
abas.add(frame_aba3, text="Aba 3")

abas.pack(fill=BOTH, expand=1)

janela.geometry("500x300+200+200")
janela.title("Abas")
janela.mainloop()
