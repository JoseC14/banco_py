
saldo         = 0
LIMITES_SAQUE = 3
MAXIMO_SAQUE  = 500
numeros_saque = 0
deposito      = 0
saques        = 0
transacao     = 0
extrato       = ""
opcao         = ""
menu          = """
    SISTEMA BANCÁRIO

    (s) Sacar
    (d) Depositar
    (e) Extrato
    (q) Sair do Sistema
"""



while True:
    print(menu)
    print("Digite uma opção")
    opcao = input()
    if opcao == "s":
        print("SAQUE")
        while True:
            print("Quanto deseja sacar?")
            transacao = float(input())
            if transacao > deposito:
                print("Erro! Você não tem saldo suficiente na conta.")
                break
            elif transacao > MAXIMO_SAQUE:
                print("Erro! Saques permitidos apenas até 500 reais.")
            elif saques >= LIMITES_SAQUE:
                print("Erro! Limite de Saques Diários atingido!")
            else:
                deposito -= transacao
                saques   += 1
                print("Saque efetuado com sucesso!")
                extrato = extrato + "Saque: "+str(transacao)+"\n"
                break
    elif opcao == "d":
        print("DEPÓSITO")
        print("Quanto deseja depositar")
        transacao = float(input())
        deposito += transacao
        print("Depósito feito com sucesso!")
        extrato = extrato + "Depósito: "+str(transacao)+"\n"
    elif opcao == "e":
        print("EXTRATO")
        print(extrato)
    elif opcao == "q":
        break;
    else:
        print("Opção Inválida")
    
