# https://wiki.python.org.br/EstruturaDeRepeticao

from os import system, name
from utils import msg_aguardar
import numpy
import math

menu = """
    Informe qual o exercicio que resolver:

    [1] Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
    [2] Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
    [3] Faça um programa que leia e valide as seguintes informações:
            Nome: maior que 3 caracteres;
            Idade: entre 0 e 150;
            Salário: maior que zero;
            Sexo: 'f' ou 'm';
            Estado Civil: 's', 'c', 'v', 'd';
    [4] Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
    [5]
    [6] Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

    [q] Sair

=> """

while True:
    op = input(menu)

    print("")

    match op:
        case "1":
            nota_valida = range(0, 10, 1)

            while True:
                nota = float(input("Informe uma nota entre zero e dez: "))

                if nota in nota_valida:
                    print(f"A nota informada {nota} é válida, pois está entre 0 e 10.")

                    msg_aguardar()
                    break
                else:
                    print(f"A nota informada {nota} não é valida, informe um numero entre 0 e 10.")
                    msg_aguardar()

        case "2":
            while True:
                nome = input("Informe seu nome: ")
                senha = input("Informe sua senha: ")

                if nome == senha:
                    print("\nErro! Nome e senha não podem ser iguais, tente novamente.")
                    msg_aguardar()
                else:
                    print("\nDados aceitos.")
                    msg_aguardar()
                    break

        case "3":
            while True:
                nome_validado = False
                idade_validada = False
                salario_validado = False
                sexo_validado = False
                estado_civil_validado = False

                idade_range = range(0, 150, 1)
                sexo_valores = ["f", "m"]
                estado_civil_valores = ["s", "c", "v", "d"]

                dado = ""

                while not nome_validado:
                    dado = input("Informe seu nome: ")

                    if len(dado) < 3:
                        print("O nome informado deve ter mais de 3 caracteres.")
                        msg_aguardar()

                    else:
                        print("nome validado.")
                        nome = dado
                        nome_validado = True
                        msg_aguardar()

                while not idade_validada:
                    dado = int(input("Informe sua idade: "))

                    if dado not in idade_range:
                        print(f"Idade informada {dado} inválida, o valor deve estar entre 0 e 150")
                        msg_aguardar()

                    else:
                        print("Idade validada.")
                        idade = dado
                        idade_validada = True
                        msg_aguardar()

                while not salario_validado:
                    dado = float(input("Informe seu salário: "))

                    if dado <= 0:
                        print("O salário informado deve ser maior que zero.")
                        msg_aguardar()
                    else:
                        print("Salario validado.")
                        salario = dado
                        salario_validado = True
                        msg_aguardar()

                while not sexo_validado:
                    dado = input("Informe seu sexo: ")

                    if not dado.lower() in sexo_valores:
                        print("Sexo informado inválido, valores aceitos, 'f' e 'm'.")
                        msg_aguardar()
                    else:
                        print("Sexo validado.")
                        sexo = dado.lower()
                        sexo_validado = True
                        msg_aguardar()

                while not estado_civil_validado:
                    dado = input("Informe seu estado civil: ")

                    if not dado.lower() in estado_civil_valores:
                        print("Estado civil inválido, valores válidos: 's', 'c', 'v', 'd'.")
                        msg_aguardar()
                    else:
                        print("Estado Civil validado.")
                        estado_civil = dado.lower()
                        estado_civil_validado = True
                        msg_aguardar()

                if (
                    nome_validado
                    and idade_validada
                    and salario_validado
                    and sexo_validado
                    and estado_civil_validado
                ):
                    texto = f"Dados validos.\n\t"
                    texto += f"Nome: {nome}\n\t"
                    texto += f"Idade: {idade}\n\t"
                    texto += f"Salario: R${salario:.2f}\n\t"
                    texto += f"Sexo: {sexo}\n\t"
                    texto += f"Estado Civil: {estado_civil}\n\t"

                    print(texto)
                    msg_aguardar()
                    break

        case "4":
            populacao_a = 80000
            taxa_a = 1.03
            populacao_b = 200000
            taxa_b = 1.015

            anos = 0

            while populacao_a < populacao_b:
                populacao_a *= taxa_a
                populacao_b *= taxa_b

                anos += 1

            print(f"Serão necessários {anos} anos para que a populacao a iguale ou ultrapasse a populacão b")
            print(f"Populacao a {populacao_a:.0f}")
            print(f"Populacao a {populacao_b:.0f}")

            msg_aguardar()

        case "5":
            msg_aguardar()

        case "6":
            print()

            for numero in range(1, 21, 1):
                print(f"{numero}", end="\n")

            msg_aguardar()

            for numero in range(1, 21, 1):
                print(f"{numero}", end=" ")

            print()
            msg_aguardar()

        case "q":
            print("Saindo...")
            break

        case _:
            print("opcao invalida!")
