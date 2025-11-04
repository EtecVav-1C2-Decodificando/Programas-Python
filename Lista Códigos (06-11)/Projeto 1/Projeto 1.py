r= "S"

while r=="S":
        num= int(input("Digite o número a ser verificado: "))
        if(num >= 100 and num <= 200):
            print("Este número está no intervalo de 100 a 200!")
        else:
            print("Este número não está no intervalo de 100 a 200!")
        r= input("Deseja continuar?(S/N)")