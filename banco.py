
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
    (lu) Listar Usuários
    (lc) Listar Contas
    (q) Sair do Sistema
"""
usuarios = []
contas   = []

#OPERAÇÕES BANCÁRIAS
def sacar(valor,saques,LIMITES_SAQUE,numero_agencia, /):
    global extrato
    conta = acha_agencia(numero_agencia)
    while True:
        if valor > conta["Saldo"]:
            print("Erro! Você não tem saldo suficiente na conta.")
            break
        elif valor > MAXIMO_SAQUE:
            print("Erro! Saques permitidos apenas até 500 reais.")
            break
        elif saques >= LIMITES_SAQUE:
            print("Erro! Limite de Saques Diários atingido!")
        else:
            conta["Saldo"] -= valor
            saques   += 1
            print("Saque efetuado com sucesso!")
            conta["Extrato"] = conta["Extrato"] + "Saque: R$"+str(valor)+"\n"
            break


def depositar(*,transacao,numero_agencia): 
    global extrato
    conta = acha_agencia(numero_agencia)
    conta["Saldo"] += transacao
    print("Depósito feito com sucesso!")
    conta["Extrato"] = conta["Extrato"] + "Depósito: R$"+str(transacao)+"\n"


#OPERAÇÕES DE CRIAR CONTAS
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

def criar_conta(contas):
    numero_conta = input("Digite o número da conta: ")
    agencia      = input("Digite o número da agência(XXXX): ")
    while True:
        cpf = input("Digite o CPF da sua conta cadastrada: ")
        if(not achaCliente(cpf)):
            print("CPF não encontrado no banco de dados")
        else: 
            break

    contas.append({
        "Número da Conta": numero_conta,
        "Agência": agencia,
        "CPF" : cpf,
        "Saldo" : 0,
        "Extrato" : ""
    })

#OPERAÇÕES DE CHECAGEM
def checa_repetido(cpf,clientes):
    if clientes:
        for cliente in clientes:
            for k,v in cliente:        
                if v == cpf:
                    return True
                else: 
                    return False

def checa_agencia(numero_agencia):
    for conta in contas:
        if conta["Número da Conta"] == numero_agencia:
            return True
        else:
            return False
        
#OPERAÇÕES DE LISTAGEM
def lista_clientes(clientes):
    for cliente in clientes:
        print("-------------------------------------")
        for k,v in cliente.items():
            print(f"{k} : {v}")
    
def lista_contas(contas):
    for conta in contas:
        print("-------------------------------------")
        for k,v in conta.items():
            print(f"{k}: {v}")


#OPERAÇÕES PARA ACHAR DADOS
def achaCliente(cpf):
    for cliente in usuarios:
        if cliente["CPF"] == cpf:
            return True
        else:
            return False

def acha_agencia(numero_agencia):
    for conta in contas:
        if conta["Número da Conta"] == numero_agencia:
            return conta

def ver_extrato(tipo,num_conta,contas):
    if tipo == "1":
        for conta in contas:
            if conta["Número da Conta"] == num_conta:
                print(conta["Extrato"])
    elif tipo == "2":
        for conta in contas:
            if conta["CPF"] == num_conta:
                print(conta["Extrato"])

while True:
    print(menu)
    print("Digite uma opção")
    opcao = input()
    if opcao == "s":
        print("SAQUE")
        transacao = float(input())
        agencia = input("Digite o número da Conta: ")
        if checa_agencia(agencia):       
            sacar(transacao,saques,LIMITES_SAQUE,agencia)
        else:
            print("Número de Agência não encontrado!")

    elif opcao == "d":
        print("DEPÓSITO")
        print("Quanto deseja depositar")
        transacao = float(input())
        num_agencia = input("Digite o número da Conta")
        if(checa_agencia(num_agencia)):        
            depositar(transacao=transacao,numero_agencia=num_agencia)
        else:
            print("Número da Conta não encontrado")

    elif opcao == "e":
        print("EXTRATO")
        print("VOcê deseja ver o extrato de uma conta ou de todas as suas contas?")
        print("(1) de Apenas uma conta")
        print("(2) de Todas minhas contas cadastradas")
        opcao = input()
        if opcao == "1":
            num_conta = input("Digite o número da conta: ")
        elif opcao == "2":
            num_conta = input("Digite seu cpf")

        ver_extrato(num_conta,contas)

    elif opcao == "cu":
        print("CRIAR USUÁRIO")
        criar_usuario(usuarios)

    elif opcao == "cc":
        print("CRIAR CONTA")
        criar_conta(contas)

    elif opcao == "lu":
        lista_clientes(usuarios)
    elif opcao =="lc":
        lista_contas(contas)
    elif opcao == "q":
        break;
    else:
        print("Opção Inválida")
    
