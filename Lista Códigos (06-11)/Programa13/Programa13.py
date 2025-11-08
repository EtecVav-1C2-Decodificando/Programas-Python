r = "s"

while r == 's':
	
	def media (v):
		return sum(v)/len(v)
		
	lista = list(map(int, input(f"Digite a lista separada por espaços: ").split()))
	
	print("A media é: ", media(lista))
	
	r = input("Deseja continar (s/n)?: ")
	