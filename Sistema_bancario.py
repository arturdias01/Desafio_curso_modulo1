import os

def limpar():
    os.system('pause')
    os.system('cls')

# ----------------------------------------------------

saldo = float(600)
limite = 500.00
extrato = []
limite_saques = int(3)
numero_saques = 0
str_extrato = None

# ----------------------------------------------------
msg_limite = """
Limite maximo de saques atingido.

Prezado(a) cliente gostaríamos de informar que o limite diário de saques em sua conta foi atingido.
Por favor, aguarde até o próximo dia útil para realizar novas transações de saque ou entre em
contato com o nosso suporte.
"""

saldo_indisponivel = """
Saldo indisponivel...

Prezado(a) cliente, lamentamos informar que, no momento, seu saldo está indisponível.
Por favor, entre em contato com o nosso suporte para mais informações. 
Agradecemos sua compreensão.
"""

menu = f"""
[1]-Sacar
[2]-Depositar
[3]-Visualizar extrato 
[0]-Sair
"""

# ----------------------------------------------------

teste = True

while teste == True:
    print(f'Saldo: R${saldo:.2f}')
    print(menu)

    opcao = input('Oque deseja fazer? ')

    if opcao == "0":
        print('Saindo...')
        os.system('Pause')
        teste = False

    elif opcao == "1":
        os.system('cls')
        quantia = float(input('Informe a quantia que deseja sacar: '))
        
        if quantia > limite or numero_saques >= limite_saques:
            print(msg_limite)
            limpar()

        elif quantia <= saldo and quantia != 0:
            saldo -= quantia
            numero_saques += 1
            str_extrato = f"Saída: R${quantia:.2f}"
            extrato.append(str_extrato)
            print('Saque realizado com sucesso!')
            limpar()
            quantia = 0
            str_extrato = None
            

        elif quantia == 0:
            print('Não é possível realizar a operação')
            limpar()

        else:
            print(saldo_indisponivel)
            limpar()
    
    elif opcao == "2":
        os.system('cls')
        quantia = float(input('Informe a quantia que deseja depositar: '))

        if quantia > 0:
            saldo += quantia
            str_extrato = f'Entrada: R${quantia:.2f}'
            extrato.append(str_extrato)
            print('Depósito realizado com sucesso!\n')
            limpar()
            str_extrato = None
            quantia = 0

        else:
            print('Não foi possível realizar a operação.\n')
            limpar()


    elif opcao == "3":
        
        os.system('cls')
        print('-----Seu Extrato-----\n')

        if len(extrato) == 0:
            print('Não há operações no momento...')
        else:
            for i in extrato:
                print(i)
        print(f'\nSaldo: R${saldo:.2f}\n')
        print('---------------------')
        limpar()

    else:
        print('Operação indisponível...')
        limpar()