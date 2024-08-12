class ContaBancaria:
    def __init__(self, saldo_inicial = 0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else: 
            print("O valor do deposito é positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente ou valor negativo")

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
        else:
            print ("Saldo insuficiente ou valor inválido")

    def consultar_saldo(self):
        return self.saldo
    
    def peek(self):
        return self.consultar_saldo[len(self.items)-1]
    
    def pop(self):
        return self.consultar_saldo.pop

    
#Exemplos:
    
conta1 = ContaBancaria(1000)
conta2 = ContaBancaria(5000)

conta1.depositar(200)
conta1.transferir(150, conta2)

print(f"Saldo conta1: {conta1.consultar_saldo()}")
print(f"Saldo conta2: {conta2.consultar_saldo()}")

