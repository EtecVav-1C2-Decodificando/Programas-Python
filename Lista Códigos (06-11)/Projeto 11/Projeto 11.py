#11. Faça um programa que preencha um vetor com oito números inteiros, calcule e mostre dois vetores resultantes. 
# O primeiro vetor resultante deve conter os números positivos e o segundo, os números negativos. 
# Cada vetor resultante vai ter, no máximo, oito posições, que não poderão ser completamente utilizadas.
r = "S"
while r == "S":
    positivos = []
    negativos = []
    i = 0


    while i < 8:
        num = int(input(f"Digite o {i+1}º número da sequência: "))

        if num > 0:
            positivos.append(num)
        
        elif num < 0:
            negativos.append(num)
        i += 1

    print("Números positivos:", positivos)
    print("Números negativos:", negativos)
    r = input("Deseja continuar(S/N)")