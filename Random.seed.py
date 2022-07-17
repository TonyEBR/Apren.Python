#A função random.seed gera um número pseudo-aleatório, isto é, deterministíco (valor/correspondente) de acordo com um valor semente dado.
import random
#Valor da semente
random.seed(10)
#Print mostrará um número inteiro aleatório determinado pela semente no intervalo dado. Se repetir a execução verá que o valor é sempre o mesmo.
print(random.randint(0,100))
#Para provar que é um valor determinado basta repetir a operação:
random.seed(10)   
print(random.randint(0,100)) 
    
