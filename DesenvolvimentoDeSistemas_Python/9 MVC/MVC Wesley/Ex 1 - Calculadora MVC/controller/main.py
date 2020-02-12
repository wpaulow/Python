from controller.controleCalculadora import ControleCalculadora

from view.visaoCalculadora import VisaoCalculadora


telaCalc = VisaoCalculadora()
telaCalc.start()
ctrlCalc = ControleCalculadora()
ctrlCalc.lerDados()
