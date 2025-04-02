class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor 
    
    def consulta(self):
        return self.__saldo
    
