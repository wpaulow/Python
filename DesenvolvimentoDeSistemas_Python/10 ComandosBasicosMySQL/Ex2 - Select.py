import MySQLdb

host = "localhost"
user = "PythonProjects"
password = "123456"
db = "bd_escola"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

cur = con.cursor()

cur.execute("select * from aluno")

for registro in cur.fetchall():
    print(registro)