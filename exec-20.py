#20) Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1=int(input("Insira o primeiro valor:"))
valor2=int(input("Insira o segundo valor"))

if valor1>valor2:
    print(f"{valor2} {valor1}")
else:
    print(f"{valor1} {valor2}")
