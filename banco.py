
LIMITES_SAQUE = 3
MAXIMO_SAQUE  = 500
numeros_saque = 0
deposito      = 0
transacao     = 0
saques        = 0
extrato       = ""
opcao         = ""
menu          = """
    SISTEMA BANCÁRIO

    (s) Sacar
    (d) Depositar
    (e) Extrato
    (q) Sair do Sistema
"""

def sacar(valor,saques,LIMITES_SAQUE, /):
    global deposito
    global extrato
    while True:
        if valor > deposito:
            print("Erro! Você não tem saldo suficiente na conta.")
            break
        elif valor > MAXIMO_SAQUE:
            print("Erro! Saques permitidos apenas até 500 reais.")
            break
        elif saques >= LIMITES_SAQUE:
            print("Erro! Limite de Saques Diários atingido!")
        else:
            deposito -= valor
            saques   += 1
            print("Saque efetuado com sucesso!")
            extrato = extrato + "Saque: R$"+str(valor)+"\n"
            break


def depositar(*,transacao): 
    global deposito
    global extrato
    deposito += transacao
    print("Depósito feito com sucesso!")
    extrato = extrato + "Depósito: R$"+str(transacao)+"\n"

while True:
    print(menu)
    print("Digite uma opção")
    opcao = input()
    if opcao == "s":
        print("SAQUE")
        transacao = float(input())
        sacar(transacao,saques,LIMITES_SAQUE)
    elif opcao == "d":
        print("DEPÓSITO")
        print("Quanto deseja depositar")
        transacao = float(input())
        depositar(transacao=transacao)
        print(f"Saldo atual:{deposito}")

    elif opcao == "e":
        print("EXTRATO")
        print(extrato)
    elif opcao == "q":
        break;
    else:
        print("Opção Inválida")
    
