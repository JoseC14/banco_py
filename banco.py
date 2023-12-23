
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
    (cu) Criar Usuário
    (cc) Criar Conta
    (l) Listar Clientes
    (l) Listar Contas
    (q) Sair do Sistema
"""
usuarios = []
contas   = []
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


def criar_usuario(usuarios):
    nome                  = input("Digite seu nome: ")
    data_nascimento       = input("Digite sua data de nascimento: ")
    
    while True:
        cpf = input("Digite seu CPF(somente números): ")
        if(checa_repetido(cpf,usuarios)):
            print("CPF Já existe no banco de dados")
        else:
            break

        
    logradouro            = input("Digite seu logradouro: ")
    numero                = input("Digite o número da sua casa: ")
    bairro                = input("Digite seu bairro: ")
    cidade                = input("Agora a cidade em que você reside: ")
    estado                = input("Estado: ")

    endereco = logradouro + " - " + numero + " - " + bairro + " - " + cidade + " - " + estado
    
    usuarios.append(dict({
        "Nome":nome,
        "Data de Nascimento": data_nascimento,
        "CPF":cpf,
        "Endereço":endereco
    }))

def checa_repetido(cpf,clientes):
    if clientes:
        for k,v in clientes[0].items():
            if v == cpf:
                return True
            else: 
                return False

def lista_clientes(clientes):
    for cliente in clientes:
        for k,v in cliente.items():
            print(f"{k} : {v}")
    print("-------------------------------------")


def criar_conta(contas):
    agencia = input("Digite o número da agência: ")
    numero_conta = input("Digite o número da conta(XXXX): ")
    while True:
        cpf = input("Digite o CPF da sua conta cadastrada: ")
        if(not achaCliente(cpf)):
            print("CPF não encontrado no banco de dados")
        else: 
            break

    contas.append({
        "Agência: ": agencia,
        "Número da Conta": numero_conta,
        "CPF do Usuário" : cpf 
    })

def achaCliente(cpf):
    for cliente in usuarios:
        if cliente["CPF"] == cpf:
            return True
        else:
            return False
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
    elif opcao == "cu":
        print("CRIAR USUÁRIO")
        criar_usuario(usuarios)
    elif opcao == "cc":
        print("CRIAR CONTA")
        criar_conta(contas)
    elif opcao == "l":
        lista_clientes(usuarios)
    elif opcao == "q":
        print("LISTAR CLIENTES")
        lista_clientes(usuarios)
    elif opcao == "q":
        break;
    else:
        print("Opção Inválida")
    
