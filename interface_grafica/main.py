# Sistema bancario simples 
# Classes Cliente, Conta, Banco. Depósito, saque, extrato.

'''
1. Cadastro e gerenciamento de clientes
Aqui o banco armazena os dados do cliente: nome, CPF, endereço, telefone, etc. Cada cliente pode ter uma ou mais contas.

Gerenciar contas: criar, alterar, consultar saldo, extrato, etc.
'''

class Cliente:
    def __init__(self, nome, cpf, telefone, dinheiro= None):
            self.nome = nome
            self.cpf = cpf
            self.telefone = telefone
            self.dinheiro = dinheiro
 

class Cadastro:
    def __init__(self):
          self._dados = []

    def analisar(self, dado):
        print('chegou aqui')
        for i in self._dados:
            if i['Nome'] == dado.nome and i['CPF'] == dado.cpf and i['Telefone'] == dado.telefone :
                return True
                 
        return False
    
    
    def adicionar(self, dado):
      #     self._dados.append(dados)
      clinete = {
           'Nome': dado.nome,
           'CPF': dado.cpf,
           'Telefone': dado.telefone
      }
      self._dados.append(clinete)

    def listar(self):
          for c in self._dados:
                print(f'Nome: {c['Nome']}, CPF: {c['CPF']}, Telefone: {c['Telefone']}')

cadastro = Cadastro()
# cadsatro do cleinte
import os
flag1 = True
while flag1:
    os.system('clear')
    print('\n')

    print('=================')
    print(' BANCO DO BRASIL ')
    print('=================')
    print('Bem vindo...')
    print('\n')
    print(
        '1 - loguin\n',
        '2 - Cadastrar\n',
    )
    print('-----------------')

    opcao = int(input('Qual deseja escolher?: '))
    os.system('clear')
    print('-----------------------------')
    print('Informaçoes Para se entrar')
    print('-----------------------------')
    if opcao == 1 or opcao == 2:
        usuario = input('Digite usuario: ')
        cpf = input('CPF: ')
        telefone= input('telefone: ')
        if opcao == 1:
            analisar1 = Cliente(usuario, cpf, telefone)
            loguin = cadastro.analisar(analisar1)
            print(loguin)
            if  loguin == True:
                 flag1 = False
            else :   
                input('Aperte enter ///')
        elif opcao == 2:
            print('entrou no Cadastro')

            clinete1 = Cliente(usuario, cpf, telefone )
            print(cadastro.adicionar(clinete1))
            cadastro.listar()
    else:
        print('erro não tem')
        continue
    while True:
         
         print(f'Olá {...}')
         print(f'Saldo da conta: {...}')
         print('\n')

         
         
