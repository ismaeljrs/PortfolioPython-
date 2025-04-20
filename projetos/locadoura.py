import os

Carros = [
    ('Chevrolet Tracker', 120),
    ('Chevrolet Onix', 90),
    ('Chevrolet Spin', 150),
    ('Hyundai HB20', 85),
    ('Hyundai Tucson', 120),
    ('Fiat Uno', 60),
    ('Fiat Mobi', 70),
    ('Fiat Pulse', 130),
]

alugados = []


def  mostrar_lista_de_carros(lista_de_carros):
    for i,car in enumerate(lista_de_carros):
        print(f'[{i}] {car[0]} - R$ {car[1]} /dia')

while True:
    os.system('clear')
    print('===============================')
    print('Bem vindo a locadora de carros')
    print('===============================')

    print('O que deseja fazer? ')
    print('0 - Mostrar portifório | 1 - Alugar um carro | 2 - Desolver um carro')
    op = int(input())

    os.system('clear')
    if op == 0:
        mostrar_lista_de_carros(Carros)
    elif op == 1:
        mostrar_lista_de_carros(Carros)
        print('Escolha o codigo do carro:')
        cod_car = int(input())
        print('Por quantos dias você desenha alugar esse carro?')
        dias = int(input())
        os.system('clear')
        print(f'Você escolheu {Carros[cod_car][0]} por {dias} dias. ')
        print(f'O aluguel totalizaria R$ { dias * Carros[cod_car][1]}')

        print('0 - Sim  | 1 - Não')
        conf = int(input())
        if conf == 0:
            print('Parabéns você alugou o carro')
            alugados.append(Carros.pop(cod_car))
    elif op == 2:
        if len(alugados) == 0:
            print('Não há carros para devolver.')
        else:
            print('Segue a lista de carros qual vc deseja devolver?')
            mostrar_lista_de_carros(alugados)
            print('')
            print('Escolha o código do carro que deseja devolver: ')
            cod = int(input())
            if conf == 0:
                print('Obrigado por devolver o carro')
                Carros.append(alugados.pop(cod))


    print('0 - CONTINUAR | 1 - SAIR')
    if  float(input()) == 1:
        break





    



