import random

def validar_sorteio(participantes, embaralhados):
       for item in range(len(participantes)):
            if participantes[item] == embaralhados[item]:
                return False
            else:
                return True 

n = int(input('Digite o número de participantes: '))
participantes = list()

for item in range(n):
    nome = str(input(f'Digite o nome do {item + 1}º participante: ')).title().strip()
    participantes.append(nome)

embaralhados = random.sample(participantes, len(participantes))
while not validar_sorteio(participantes, embaralhados):
    embaralhados = random.sample(participantes, len(participantes))

# print("Resultado do amigo oculto: ")
# for item in range(len(participantes)):
    # print(f"{participantes[item]} tirou {embaralhados[item]}!")

for pessoa in range(len(participantes)):
     with open(f"{participantes[pessoa]}.txt", "w", encoding='utf-8') as arquivo:
        arquivo.write(f'Para sua alegria ou tristeza, você sorteou o(a) {embaralhados[pessoa]}!')

