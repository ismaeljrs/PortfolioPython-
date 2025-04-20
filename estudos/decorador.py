# def meu_decorador(func):
#     def decora():
#         print('Decora primeiro')
#         func()
#         print('Decorador segundo')
#     return decora

# @meu_decorador
# def diz():
#     print('Ola meu nome e ismael')

# diz()

usuario_login = False

def verificar_loguin(func):
    def entrada():
        if usuario_login:
            func()
        else:
            print("Acesso negado! Faça login.")
    return entrada

@verificar_loguin
def ver_saldo():
    print('Seu saldo e R$ 10.000')
    
# entrada 
usuario = str(input('Qual e o seu nome?: '))
senha_usuario =  int(input('Informe uma Senha: '))

# solicitação de senha para entrada 
senha_entrada = int(input('Senha: '))


if senha_entrada == senha_usuario:
    print(f'Seja Bem-Vindo {usuario}')  
    usuario_login = True 
else:
    print("Senha incorreta!")

# chama a função
ver_saldo()  





