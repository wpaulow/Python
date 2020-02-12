from controller.controleCalculadoraCirculo import ControleCalculadora

from view.visaoCalcCirc import VisaoCalcCirculo

telaCalc = VisaoCalcCirculo()
telaCalc.start()
ctrlCalc = ControleCalculadora()
ctrlCalc.lerDados()
