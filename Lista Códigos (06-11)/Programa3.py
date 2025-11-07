n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Escolha um operador aritimétrico: '+', '-','*', '/'.")

Operador = input("Digite o operador: ")

if operador == "+":
	print(f"O resultado é: {n1+n2}")
elif operador == "-":
	print(f"O resultado é: {n1-n2")
elif operador == "*":
	print(f"O resultado é: {n1*n2}")
elif operador == "/":
	print (f"O resultado é: {n1/n2}")
else:
	print("É necessario um operador válido")