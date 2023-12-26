import Cliente
class PessoaFisica(Cliente):

    def __init__(self,cpf,nome,data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    

