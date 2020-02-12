import MySQLdb

class ConectaBanco: #define a classe

    def __init__(self): #método inicializador da classe
        self.con = "" #cria variável de conexão vazia


    def conecta(self): #método para conectar no banco
        host = "localhost" #nome utilizado no host no workbench
        user = "PythonProjects" #nome do usuário que criamos no workbench
        password = "123456" #senha que colocamos para o usuário
        db = "bd_escola" #nome do banco de dados
        port = 3306 #porta configurada para o server
        self.con = MySQLdb.connect(host, user, password, db, port) #na variável con cria a nossa conexão


    def select(self, campos, tabelas, where = None): # define o método, o parâmetro where é opcional
        self.conecta() #cria a conexão com o banco
        cur = self.con.cursor() #cria uma variável do tipo cursor capaz de executar as queries
        query = ("select " + campos + " from " + tabelas)
        if where: #caso o parâmetro where seja colocado
            query = (query + " where " + where) #adiciona where na query
        cur.execute(query) #executa um select através do cur
        result = cur.fetchall() #gera uma tupla com os registros encontrados
        self.con.close() #encerrar a conexão, por segurança e produtividade da estação de trabalho
        return result


    def insert(self, tabela, valores, campos = None):
        self.conecta()
        cur = self.con.cursor()
        query = ("insert into " + tabela)
        if campos:
            query = (query + "(" + campos + ")")
        query = (query + " values(" + valores + ")")
        print(query)
        cur.execute(query)
        self.con.commit()
        self.con.close()


    def update(self, tabela, sets, where):
        self.conecta()
        cur = self.con.cursor()
        query = ("update " + tabela + " set " + sets + " where " + where)
        print(query)
        cur.execute(query)
        self.con.commit()
        self.con.close()


    def delete(self, tabela, where):
        self.conecta()
        cur = self.con.cursor()
        query = ("delete from " + tabela + " where " + where)
        print(query)
        cur.execute(query)
        self.con.commit()
        self.con.close()
