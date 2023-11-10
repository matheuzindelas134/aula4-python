def IMC(peso, altura):
    return peso/altura**2

peso_altura = []

for i in range(4):
    nome = str(input("digite o nome da pessoa: "))
    peso = float(input("digite o peso da pessoa: "))
    altura = float(input("digite a altura da pessoa: "))

    peso_altura.append([nome,IMC(peso, altura)])

    print(peso_altura)



