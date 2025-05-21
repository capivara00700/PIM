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
    print("Usuario cadastrado com sucesso!")
    perguntas.exercicios()

def login(usuario, senha):
    cursor.execute("SELECT senha from usuarios WHERE usuario = %(usuario)s", ({'usuario': usuario, }))
    msg = cursor.fetchone()
    s1 = criptografia.descryptografar(msg[0])
    if s1 == senha:
        perguntas.exercicios()
    else:
        print('Erro senha ou usuario incorreto')
