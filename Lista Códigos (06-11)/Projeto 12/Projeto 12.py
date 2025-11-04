#12. Faça um programa que receba um número inteiro, determinando a soma de 0 até tal número (incluso) 
#por meio de uma função soma(n) que retorne tal soma.
r = "S"

def soma(n):
    total = 0
    i = 0

    while i <= n:
        total += i
        i += 1

    return total
while r == "S":
    num = int(input("Digite um número: "))

    resultado = soma(num)

    print(f"O resultado da soma de 0 até {num} é de: {resultado}")

    r = input("Deseja continuar? (S/N)")