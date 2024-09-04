#19) Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles. 

valor1=float(input("Insira o primeiro valor"))
valor2=float(input("Insira o segundo valor"))

if valor1>valor2:
    print(f"O primeiro valor é maior que o segundo valor portanto {valor1} > {valor2}")
else:
    print(f"O segundo valor é maior que o primeiro valor portanto {valor2} > {valor1}")
 
