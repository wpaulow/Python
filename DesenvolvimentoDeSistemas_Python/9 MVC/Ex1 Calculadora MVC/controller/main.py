# Arquivo principal do programa.
from controller.controleCalculadora import ControleCalculadora
# Da pasta controller do arquivo controleCalculadora importe a classe ControllerCalculadora
from view.visaoCalculadora import VisaoCalculadora
# Da pasta view do arquivo viewCalculadora importe a classe viewCalculadora

telaCalc = VisaoCalculadora()  # Instancia um obj do tipo VisaoCalculadora
telaCalc.start()  # Chama o método strart lá da classe VisãoCalculadora
ctrlCalc = ControleCalculadora()  # Instancia um obj do tipo ControleCalculadora
ctrlCalc.lerdados()  # Chama o método lerdados lá da classe ControleCalculadora
