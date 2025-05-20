import cryptocode

chave = "563"

def cryptografar(senha):
    mensagemCryptografada = cryptocode.encrypt(senha, chave)
    return mensagemCryptografada

def descryptografar(senha):
    mensagemCryptografada = cryptocode.decrypt(senha, chave)
    return mensagemCryptografada
