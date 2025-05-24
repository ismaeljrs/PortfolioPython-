
from Menu_inicial import Cadastro , Acesso_ao_sistema
import os
# Fora do loop 
def titulo():
    print(
        '--------------------------------------\n'
        '       GERENCIADOR DE TAREFAS 📝     \n'
        '--------------------------------------\n'
    )

def Sair_do_Sistema(opcao_saida,flag1,flag2,flag3):
    if opcao_saida == 'n':
        return False, False, False
    elif opcao_saida == 's':
        return flag1, flag2, False 
    elif opcao_saida == 'f':
        return flag1, False, False
    else:
        print("Opção inválida. Tente novamente.")
        return flag1,flag2,flag3


# loops


cadastro = Cadastro()
acessar_o_sistema = Acesso_ao_sistema()
# Dentro do loop

flag1 = True
while flag1:
    os.system('clear') 
    titulo()
    print(cadastro.usuario)
    print(acessar_o_sistema.add_tarefa)

    print(
        '1 - Registrar novo úsuario\n'
        '2 - Fazer loguin\n'
        '3 - Sair\n'
    )

    #extrutura de descição
    try:

        opcao = int(input('Escolha uma Opção: '))
    except:
        print('Digite apenas números ')
        input('aperte enter /// ')
        continue
    if opcao == 1:
        nome = input('Digite seu nome: ')
        if  nome.isnumeric():
            print('Digite Apenas caracteres')
            input('Aperte enter ')
            continue
        if not len(nome) >= 6:
            print('Digite pelo menos 6 caracteres ')
            input('Aperte enter ')
            continue

        email = input('Digite seu E-mail: ')
        nome_titulo = cadastro.titulo(email)
        # Verifica se termina com "@gmail.com"
        if not email.endswith('@gmail.com'):
            print("Insira um número de endereço válido.")
            input('Aperte enter ')
            continue
        
        senha = input('Digite sua senha: ')
        if not len(senha) >= 6:
            print('Digite na senha pelo menos 6 letras')
            input('Aperte enter ')
            continue
        cadastro.registrar_usuario(nome,email,senha)

#Opção 2
    elif opcao == 2:
        email = input('Digite seu email: ')
        nome_titulo = cadastro.titulo(email)
        
        senha = input('Digite sua senha: ')
        sucesso = cadastro.verificar_loguin(email,senha)
        if sucesso:
            print('Login bem-sucedido!')
        else:
            print('Email ou senha incorreto!')
            continue

#Opção 3
    elif opcao == 3:
            confirm = input('Tem certeza que deseja sair? (s/n): ').lower()
            if confirm == 's':
                flag1 = False
                flag2 = False
                
    flag2 = True
    while flag2:
        os.system('clear')
        # print(
        #     '====================================\n'
        #     '        BEM-VINDO, ISMAEL! 👋\n'
        #     '====================================\n'
        # )
        print(f'Bem vindo,{nome}')
        print(
            '1 - Adicionar nova tarefa\n'
            '2 - Ver tarefa\n'
            '3 - Sair'
        )
        try: 

            menu_pri_op = int(input('Escolha uma opção: '))
        except:
            print('Digite apenas números')
            input('Aperte enter ')
            continue

        if menu_pri_op == 1:
            os.system('clear')
            try:
                print('-------------------------\n')
                print('Deseja adionar uma tarefa? \n')
                print('-------------------------\n')
                objetivo = input('Objetivo: ')

                print('Nivel de prioridade: baixa, media, alta')
                prioridade = str(input('Prioridade: '))

                data = input('Prazo de termino: ')
                acessar_o_sistema.adicionar_tarefa(objetivo,prioridade,data)
            except:
                ...
        elif menu_pri_op == 2:
            acessar_o_sistema.ver_tarefa()
            input()
        elif menu_pri_op == 3:
            os.system('clear')
            flag3 = True
            while flag3:
                print(
                'Opção de saida: S - Continuar | N - Finalizar | F - Voltar para o Menu\n'
                )
                opcao_saida = input('Digite: ').lower()
                flag1,flag2,flag3 = Sair_do_Sistema(opcao_saida,flag1,flag2,flag3)



print(
     '1 - loguin\n',
     '2 - Cadastrar\n',
)
opcao = int(input('Qual deseja escolher ?'))
usuario = input('Qual e o seu nome ? ')
cpf = input('Digite seu CPF')
telefone = input('telefone')

if opcao == 1:
     analisar1 = Cliente(usuario, cpf, telefone)
     cadastro.analisar(analisar1)
elif opcao == 2:
     clinete1 = Cliente(usuario, cpf, telefone )
     print(cadastro.adicionar(clinete1))
     cadastro.listar()
else:
     print('erro não tem')

