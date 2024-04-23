class Carro:
    def __init__(self, marca , modelo, cor , ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_informacoes(self):
        print ("Marca:", self.marca)
        print ("Modelo:", self.modelo)
        print ("Cor:", self.cor)
        print ("Ano:", self.ano)

carros = []

while True: 
    marca = input("Digite a Marca ou 'sair' para fechar o programa:")
    
    if marca.lower() == "sair":
        break
    
    modelo = input("Digite o modelo:")
    cor = input ("Digite a cor:")
    ano = input("Digite o ano:")

    carro = Carro(marca,modelo,cor,ano)
    carros.append(carro)

print("\n Informações dos carros:")
for i, carro in enumerate(carro, start = 1):
    print("f\n Carro {i}")
    carro.exibir_informacaoes()

input()