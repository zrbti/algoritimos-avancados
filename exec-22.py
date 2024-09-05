#22) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
horas_trabalhadadas=int(input("Quantas horas de trabalho foram realizadas nesse mes:"))
salario_horas=int(input("Quanto ele recebe por hora "))
horas_minimas=160
hora_extra=horas_trabalhadadas-horas_minimas
salario_extra=((50/100)*salario_horas)*hora_extra
salario_final=(horas_trabalhadadas-hora_extra)*salario_horas


if horas_trabalhadadas>horas_minimas:
    salario_final+=salario_extra
    print(f"seu salario final é {salario_final}")
else:
    print(f"seu salario final é {salario_final}")
