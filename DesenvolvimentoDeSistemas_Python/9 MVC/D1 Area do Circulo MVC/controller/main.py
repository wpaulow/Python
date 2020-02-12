# Arquivo principal do programa.
from controller.controleCirculo import ControleCirculo
# Da pasta controller do arquivo controleCirculo importe a classe ControleCirculo
from view.visaoCirculo import VisaoCirculo
# Da pasta view do arquivo visaoCirculo importe a classe VisaoCirculo

telaCirculo = VisaoCirculo()  # Instancia um obj do tipo VisaoCirculo
telaCirculo.start()  # Chama o método strart lá da classe VisãoCirculo
ctrlCirculo = ControleCirculo()  # Instancia um obj do tipo ControleCirculo
ctrlCirculo.decidecalc()  # Chama o método carregadados lá da classe ControleCirculo
