#O método randrange retorna um número aleatório no intervalo definido
import random
#Número aleatório no intervalo de 1(incluso) a 5 (não incluso).
a = random.randrange(1,5)
print(a)
#O terceiro parâmetro define a incrementação, isto é, de quando em quando os números irão aparecer (razão), quando não especificado é 1. No exemplo abaixo, os números aparecerão de 50 em 50 sem uma especificidade clara de soma/subtração com seu número anterior.
#Quando o primeiro parâmetro não é indicado, o padrão é 0.
b = random.randrange(0,1000,50)
print(b)