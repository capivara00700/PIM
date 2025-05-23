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

def verificaUsuario(usuario):
    cursor.execute("SELECT usuario from usuarios WHERE usuario = %(usuario)s", ({'usuario': usuario, }))
    if cursor.fetchone():
        print("Usuario já cadastrado, favor escolher outro nome de usuario.")
        return False
    else:
        return True

def cadastro(usuario, senha):
    sql = "INSERT INTO usuarios(usuario, senha) VALUES (%s, %s)"
    s1 = criptografia.cryptografar(senha)
    val = (usuario, s1)
    cursor.execute(sql, val)
    db.commit()
    print("Usuario cadastrado com sucesso!")
    perguntas.exercicios(usuario)

def login(usuario, senha):
    cursor.execute("SELECT senha from usuarios WHERE usuario = %(usuario)s", ({'usuario': usuario, }))
    msg = cursor.fetchone()
    s1 = criptografia.descryptografar(msg[0])
    if s1 == senha:
        perguntas.exercicios(usuario)
    else:
        print('Erro senha ou usuario incorreto')

def addPontos(pontos, dificuldade, tema, usuario):
    #Recuperando o ID
    cursor.execute("SELECT id from usuarios WHERE usuario = %(usuario)s", ({'usuario': usuario, }))
    id = cursor.fetchone()
    #Formatando o tema para facilitar o update no banco de dados
    temaSemEsp = tema.replace(" ", "")
    if dificuldade == "Nível Fácil":
        temaf = temaSemEsp+"F"
    elif dificuldade == "Nível Intermediário":
        temaf = temaSemEsp+"M"
    #adicionando os pontos a tabela
    cursor.execute("SELECT %(id)s from pontos", ({'id': id[0], }))
    idSelect = cursor.fetchone()

    if idSelect == None:
        cursor.execute(f"INSERT INTO pontos(id, {temaf}) VALUES ({id[0]}, {pontos})")
        db.commit()
    else:
        cursor.execute(f"UPDATE pontos SET {temaf} = {pontos} WHERE id = {id[0]}")
        db.commit()
