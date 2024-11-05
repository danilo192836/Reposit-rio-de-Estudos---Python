class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

    def acelerar_juntos(self, outro_carro):
        print(f'{self.nome} e {outro_carro.nome} estão acelerando juntos')

valor = int(input('Digite 2 para ver "fusca e celta" acelerando ou 1 para ver apenas "fusca": '))

if valor == 1:
    fusca = Carro('Fusca')
    fusca.acelerar()
elif valor == 2:
    fusca = Carro('Fusca')
    celta = Carro('Celta')
    fusca.acelerar()
    celta.acelerar()
    fusca.acelerar_juntos(celta)
else:
    print("Opção inválida. Digite 1 ou 2.")

