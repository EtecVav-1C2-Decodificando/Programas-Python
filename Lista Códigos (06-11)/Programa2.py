r = "s"

while r == "s":

    u = input("Qual a unidade de temperatura? C/F: ")

    t = int(input("Valor da temperatura: "))

    if u == "C":
        u = "Fahrenheit"
        resp = t * (9/5) + 32

    if u == "F":
        u = "Celsius"
        resp = (t - 32) * (5/9)

    print   (f"A temperatura em {u} é: {resp} ")
      
    r = input("Deseja continuar? s/n: ")