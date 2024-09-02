#11) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$ 700,00 para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

salário_fixo=float(input("Qual o Salario fixo"))
carro=int(input("Quantos carros foram vendidos"))
vendas=float(input("Qual foi o valor total das vendas"))
comissão_carro=(carro*700)
percentual_vendas=(vendas/100)*5
salario_bonus=(salário_fixo+comissão_carro+percentual_vendas)

print(f"O salario total é {salario_bonus}")
