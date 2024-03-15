from os import name
import subprocess
import numpy
import math

def msg_aguardar():
    print("\nPressione qualquer tecla para continuar.")
    input()

    if name == "nt":
        command= "cls"      
        subprocess.run(command, shell=False)
    else:
        command= "clear"
        subprocess.run(command, shell=False)

# menu = """
#     Informe qual o exercicio que resolver:
    
#     [1] 
#     [2] 
#     [3] 
#     [4] 
#     [5] 
#     [6] 
    
#     [q] Sair
    
# => """

# while True:
#     op = input(menu)

#     print("")
    
#     match op:
#         case "1":
#             msg_aguardar()

#         case "2":
#             msg_aguardar()

#         case "3":
#             msg_aguardar()

#         case "4":
#             msg_aguardar()

#         case "5":
#             msg_aguardar()

#         case "6":
#             msg_aguardar()

#         case "q":
#             print("Saindo...")
#             break

#         case _:
#             print("opcao invalida!")
