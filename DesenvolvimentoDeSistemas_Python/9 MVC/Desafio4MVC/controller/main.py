from controller.controleIMC import ControleIMC

from view.visaoIMC import VisaoIMC

telaIMC = VisaoIMC()
telaIMC.start()

ctrlIMC = ControleIMC()
ctrlIMC.lerDados()