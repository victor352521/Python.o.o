class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano 

    def exibir_informacoes(self):
        print("Marca: ", self.marca)
        print("Modelo ", self.modelo)
        print("Ano ", self.ano)

carro1 = Carro("Chevrolet", "Camaro Z28", "2014")
carro2 = Carro("Chevrolet", "Corvette ZR1", "2019")
carro3 = Carro("Chevrolet", "Opala SS", "1974")

carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()