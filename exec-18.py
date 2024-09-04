#18) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

nascimento=float(input("Insira seu ano de nascimento:"))
atual=float(input("Insira o ano atual"))
idade=(atual-nascimento)

if idade>=16:
    print("Você pode votar")
else:
    print("Você não pode votar")
