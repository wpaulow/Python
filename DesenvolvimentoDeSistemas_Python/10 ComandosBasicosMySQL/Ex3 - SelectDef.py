import MySQLdb

host = "localhost"
user = "PythonProjects"
password = "123456"
db = "bd_escola"
port = 3306
con = MySQLdb.connect(host, user, password, db, port)

def select (campos, tabelas, where = None):
    cur = con.cursor()
    query = ("select " + campos + " from " + tabelas)
    if where:
        query = (query + " where " + where)
    cur.execute(query)
    return cur.fetchall()

regSelect = select("*", "aluno", "idaluno = 1")
for registro in regSelect:
    print(registro)
