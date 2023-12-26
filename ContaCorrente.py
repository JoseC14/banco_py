import Conta

class ContaCorrente(Conta):

    def __init__(self,limite,limite_saques):
        self._limite        = limite
        self._limite_saques = limite_saques
    

    def sacar(self,valor):
        if valor > self._saldo:
            return False
        elif valor > self._limite:
            return False
        elif self._limites_saques == 0:
            return False
        else:
            self._saldo -= valor
            self._limites_saques -= 1
            return True
    