# Controle de Nível de Bateria

# Enunciado:
# O programa deve monitorar o nível da bateria de um dispositivo.
# Enquanto o nível de bateria for superior a 5, o programa continuará recebendo entradas de dois sensores.
# Quando o nível de bateria atingir 5 ou menos, o programa deve solicitar que a bateria seja recarregada.
# Dependendo das leituras dos sensores, o programa irá diminuir o nível da bateria e imprimir ações correspondentes:
# - Se o sensor1 for 'B' e o sensor2 for 'P' ou 'A', a bateria diminuirá em 5 e imprimirá "virar".
# - Se o sensor1 for 'L' e o sensor2 for 'P', a bateria diminuirá em 1 e imprimirá "avançar".
# - Se o sensor1 for 'L' e o sensor2 for 'A', a bateria diminuirá em 5 e imprimirá "virar".

# Entrada do nível inicial da bateria
nivel_bateria = int(input("Digite o nível da bateria: "))

# Loop para monitorar o nível da bateria
while True:
    # Verifica se o nível da bateria está baixo
    if nivel_bateria <= 5:
        print("recarregar: {}".format(nivel_bateria))
        break  # Encerra o loop se a bateria estiver baixa

    # Entrada dos sensores
    sensor1 = input("Digite a leitura do sensor 1 (B ou L): ")
    sensor2 = input("Digite a leitura do sensor 2 (P ou A): ")

    # Verifica novamente se o nível da bateria está baixo
    if nivel_bateria <= 5:
        print("recarregar: {}".format(nivel_bateria))
        break  # Encerra o loop se a bateria estiver baixa

    # Processa a leitura dos sensores
    if sensor1 == 'B':
        if sensor2 == 'P' or sensor2 == 'A':
            nivel_bateria -= 5  # Reduz a bateria em 5
            print("virar: {}".format(nivel_bateria))
    elif sensor1 == 'L':
        if sensor2 == 'P':
            nivel_bateria -= 1  # Reduz a bateria em 1
            print("avançar: {}".format(nivel_bateria))
        elif sensor2 == 'A':
            nivel_bateria -= 5  # Reduz a bateria em 5
            print("virar: {}".format(nivel_bateria))
