#13) Faça um algoritmo que leia três notas de um aluno,  calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:

#media_final = n1 * 2 + n2 * 3 + n3 * 5 /10
                        
n1=float(input("Insira sua primeira nota:"))
n2=float(input("Insira sua segunda nota"))
n3=float(input("Insira sua terceira nota"))
media_final=((n1)*2+(n2)*3+(n3)*5)/10

print(f"sua media final é {media_final}")
