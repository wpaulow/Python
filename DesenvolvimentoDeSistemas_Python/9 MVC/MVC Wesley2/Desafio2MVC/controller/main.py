from controller.controleGeometria import ControleCalculadora

from view.visaoGeometria import VisaoGeometria

telaCalc = VisaoGeometria()
telaCalc.start()
ctrlCalc = ControleCalculadora()
ctrlCalc.lerDados()
