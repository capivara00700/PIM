import dbconnect 

print('=' * 50 + '\n{:^50}\n'.format('Bem - Vindo') + '=' * 50)
print('Selecione alguma das seguintes opções para acessar a plataforma:')
e = int(input('Login [1]\nCadastrar [2]\n> '))

while True:
    if e == 1: #--Login--
        usuario = str(input('Digite seu usuario: '))
        senha = str(input('Digite sua senha: '))
        dbconnect.login(usuario, senha)
        break
    elif e == 2: #--Cadastro--
        usuario = str(input('Digite seu usuario: ')) #colocar um sistema para não ter dois usuarios com o mesmo nome
        while True:
            s1 = str(input('Digite sua senha: '))
            s2 = str(input('Confirme sua senha: '))
            if s1 == s2:
                dbconnect.cadastro(usuario, s1)
                break
            else:
                print('=' * 50, '\nErro, as senhas estão diferentes, por favor confirme sua senha novamente.')
        break
    else: #--prevenção de erros--
        print('=' * 50)
        print('Opção inválida! tente novamente.')
        e = int(input('Login [1]\nCadastrar [2]\n'))
