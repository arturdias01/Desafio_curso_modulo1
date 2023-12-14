import os

def limpar():
    os.system('pause')
    os.system('cls')


def saque(saldo_atual, quantia_saque):
    saldo_atual -= quantia_saque
    return saldo_atual


def deposito(saldo_atual, quantia_deposito):
    saldo_atual += quantia_deposito
    return saldo_atual


def mostrar_extrato(seu_extrato, saldo_atual):
    print('-----Seu Extrato-----\n')

    if len(seu_extrato) == 0:
        print('Não há operações no momento...')
    else:
        for i in seu_extrato:
            print(i)
    print(f'\nSaldo: R${saldo_atual:.2f}\n')
    print('---------------------')
    limpar()


def verificar_cpf_existente(lista, teste_cpf):
    for usuario in lista:
        if usuario.get('cpf') == teste_cpf:
            return True
    return False

def cadastrar_usuario(lista, nome, cpf):
    novo_dicionario = {"nome": nome, "cpf": cpf}
    lista.append(novo_dicionario)

def listar_usuarios(lista):
    for i in lista:
        print(i)
    
# ----------------------------------------------------

usuarios = []
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
Saldo indisponivel.

Prezado(a) cliente, lamentamos informar que, no momento, seu saldo está indisponível.
Por favor, entre em contato com o nosso suporte para mais informações. 
Agradecemos sua compreensão.
"""

menu = f"""
[1]-Sacar
[2]-Depositar
[3]-Visualizar extrato
----------------------
[4]-Cadastrar usuario
[5]-Listar usuarios
----------------------
[0]-Sair

"""

# ----------------------------------------------------

while True:
    print(f'Saldo: R${saldo:.2f}')
    opcao = input(menu)

    if opcao == "0":
        os.system('cls')
        break

    elif opcao == "1":
        os.system('cls')
        quantia = float(input('Informe a quantia que deseja sacar: '))
        
        if quantia > limite or numero_saques >= limite_saques:
            print(msg_limite)
            limpar()

        elif quantia <= saldo and quantia != 0:
            saldo = saque(saldo_atual= saldo, quantia_saque= quantia)
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
            saldo = deposito(saldo, quantia)
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
        mostrar_extrato(seu_extrato=extrato, saldo_atual=saldo)


    elif opcao == "4":

        os.system('cls')
        nome = str(input('Digito o nome: '))
        cpf = str(input('Digite o CPF: '))

        teste = verificar_cpf_existente(usuarios, cpf)

        if teste == False:
            cadastrar_usuario(usuarios, nome, cpf)
            print('Usuario cadastrado com sucesso.')
        else:
            print('Usuario ja existe.')
        limpar()


    elif opcao == "5":

        if usuarios == []:
            print('Não há nenhum usuario cadastrado.')
        else:
            listar_usuarios(usuarios)
        limpar()
        
    else:
        print('Operação indisponível...')
        limpar()

