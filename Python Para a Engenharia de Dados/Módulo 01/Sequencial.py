# https://wiki.python.org.br/EstruturaSequencial

from os import system, name
import numpy
import math


def msg_aguardar():
    print("\nPressione qualquer tecla para continuar.")
    input()

    if name == "nt":
        system("CLS")
    else:
        system("clear")


menu = """
    Informe qual o exercicio que resolver:
    
    [1] Faca um programa que mostra a mensagem "Alo mundo" na tela
    [2] Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
    [3] Faça um Programa que peça dois números e imprima a soma.
    [4] Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    [5] Faça um Programa que converta metros para centímetros.
    [6] Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    
    [q] Sair
    
=> """

while True:
    op = input(menu)

    print("")

    match op:
        case "1":
            print("Alo mundo")
            msg_aguardar()

        case "2":
            numero = int(input("Informe um número inteiro: "))

            print(f"\nO número informado foi {numero}")
            msg_aguardar()

        case "3":
            numero_1 = int(input("Informe o primeiro número inteiro: "))
            numero_2 = int(input("Informe o segundo número inteiro: "))

            print(f"\nA soma dos dois números é: {numero_1 + numero_2}")
            msg_aguardar()

        case "4":
            notas = []
            notas.append(float(input("Informe a nota do primeiro bimestre: ")))
            notas.append(float(input("Informe a nota do segundo bimestre: ")))
            notas.append(float(input("Informe a nota do terceiro bimestre: ")))
            notas.append(float(input("Informe a nota do quarto bimestre: ")))

            notas_avg = numpy.average(notas)

            print(f"\nA média das notas é: {notas_avg}")
            msg_aguardar()

        case "5":
            m = float(input("Informe um número em metros: "))

            print(f"\n{m} m em cm é equivalente a {m*100} cm.")
            msg_aguardar()

        case "6":
            diametro = float(input("Informe o diametro do circulo (cm): "))

            r = diametro / 2
            area = math.pi * r**2

            print(f"os dados do circulo informado é: \n\n diametro - {diametro} cm \n raio - {r} cm \n area - {area:.2f} cm2 \n")
            msg_aguardar()

        case "q":
            print("Saindo...")
            break

        case _:
            print("opcao invalida!")
