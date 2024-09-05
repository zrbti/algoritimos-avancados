#21) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte. 
inicio_partida=int(input("insira a hora de começo da partida (0 ate 23):"))
termino_partida=int(input("insira a hora de termino da partida (0 ate 23):"))
inicio_partida=(inicio_partida*60)
termino_partida=(termino_partida*60)

if      inicio_partida>termino_partida:
        duração=(inicio_partida-termino_partida)/60
else:
        inicio_partida<termino_partida
        duração=(termino_partida-inicio_partida)/60

print(f"o jogo terminou em {duração:.0f}hrs")

