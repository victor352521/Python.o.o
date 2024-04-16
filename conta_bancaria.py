#Objeto é uma única coleção de dados(atributos) e comportamentos (métodos)

class ContaBancaria:
    #Atributos são variáveis internas dentro do objeto
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

#Métodos sõ funções do objeto que produzem algum comportamento

    def depositar(self,valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Número da Conta", self.numero)
        print("Titular:", self.titular)
        print("Saldo", self.saldo)

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")

#aqui estou criando uma instancia do objeto ContaBancaria
#com o nome conta_do_victor

def exibir_menu():
    print("\nMENU:")
    print("1 - Exibir detalhes da conta")
    print("2 - Realizar depósito")
    print("3 - Realizar saque")
    print("0 - Sair do Programa")

numero_acc = input("Digite o número da sua conta: ")

titular_acc = input("Digite o nome do titular: ")

saldo_acc = float(input("Digite seu saldo atual: ").replace(",","."))


conta_do_usuario = ContaBancaria(numero_acc, titular_acc, saldo_acc)

opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o número da opção desejado"))

    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor a ser depositado: ").replace(",","."))
        conta_do_usuario.depositar(valor_deposito)
    elif opcao == 3:
        valor_saque = float(input("Digite o valor do seu saque: ").replace(",","."))
        conta_do_usuario.sacar(valor_saque)