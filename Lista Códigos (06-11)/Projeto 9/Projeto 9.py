#9. Faça um programa que leia duas sequências de números inteiros ordenados e 
#imprima uma sequência com os números ordenados das duas sequências anteriores. Você não deve usar o método sort.
r = "S"

while r == "S":
    lista1 = list(map(int, input("Digite a sequência da lista 1: ").split()))
    lista2 = list(map(int, input("Digite a sequência da lista 2: ").split()))

    i = 0
    j = 0
    resultado = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])

            i = i + 1

        else:
            resultado.append(lista2[j])

            j = j + 1

    while i < len(lista1):
        resultado.append(lista1[i])

        i = i + 1

    while j < len(lista2):
        resultado.append(lista2[j])

        j = j + 1

    print("A sequência final será: ", resultado)
    r = input("Deseja continuar(S/N)")