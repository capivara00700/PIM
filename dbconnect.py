import mysql.connector
import criptografia
import perguntas

#conectando com o banco de dados
db = mysql.connector.connect(
    host = 'Localhost',
    user = 'root',
    password = '',
    database = 'pim'
)
cursor = db.cursor()

def cadastro(usuario, senha):
    sql = "INSERT INTO usuarios(usuario, senha) VALUES (%s, %s)"
    s1 = criptografia.cryptografar(senha)
    val = (usuario, s1)
    cursor.execute(sql, val)
    db.commit()

def login(usuario, senha):
    sql = "SELECT usuario, senha from usuarios WHERE usuario = %s and senha = %s"
    s1 = criptografia.descryptografar(senha)
    val = (usuario, s1)
    cursor.execute(sql, val)
    if cursor.fetchall() != []:
        perguntas.exercicios()
    else:
        print('Erro senha ou usuario incorreto')
