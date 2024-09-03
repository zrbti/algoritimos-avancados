#16) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

maçãs=int(input("Quantas maçãs serão compradas:"))
maçãs_sem=(maçãs)*1.30
maçãs_com=(maçãs)*1

if maçãs<=11:
       print(f"você comprou as {maçãs} maçãs sem desconto, elas custaram {maçãs_sem}R$")
else:
       print(f"você comprou as {maçãs} maçãs com desconto, elas custaram {maçãs_com}R$")
