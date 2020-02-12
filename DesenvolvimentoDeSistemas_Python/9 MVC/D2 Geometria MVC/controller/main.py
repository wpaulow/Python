# Arquivo principal do programa.
from view.visaoGemetria import VisaoGeometria
# Da pasta view do arqu visaoGeometria importa a classe VisaoGeometria
from controller.controleGeometria import ControleGeometria
# Da pasta controller do arquivo controleCirculo importe a classe ControleGeometria

telaGeometria = VisaoGeometria()
telaGeometria.start()
ctrlGeometria = ControleGeometria()
ctrlGeometria.decicdeforma()
