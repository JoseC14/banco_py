class Conta:
    def __init__(self,numero,cliente):
        self._saldo     = 0
        self._numero    = numero
        self._agencia   = 0001
        self._cliente   = cliente
        self._historico = ""
    

    def saldo(self):
        return self._saldo
    
    def nova_conta(self, cliente, numero):
        conta = Conta(cliente,numero)
        return conta
    
    def sacar(self,valor):
        if valor > self._saldo:
            return False
        else:
            self._saldo -= valor
            return True
    
    def depositar(self,valor):
        self._saldo += valor
        return True
    


    
