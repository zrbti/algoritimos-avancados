#7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
anos=float(input("quantos anos "))
meses=float(input("quantos meses"))
dias=float(input("quantos dias"))

idade_dias=(anos*365)+(meses*30)+(dias)
print()
print(f"sua idade expressa em dias é {idade_dias}")
