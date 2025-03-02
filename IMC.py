# Cálculo do IMC (Índice de Massa Corporal)

# Enunciado:
# O programa deve receber o peso e a altura de uma pessoa e calcular o IMC (Índice de Massa Corporal).
# Com base no valor do IMC, o programa deve classificar a condição de peso da seguinte forma:
# - Muito abaixo do peso: IMC < 17
# - Abaixo do peso: 17 ≤ IMC ≤ 18.49
# - Peso normal: 18.50 ≤ IMC ≤ 24.99
# - Acima do peso: 25 ≤ IMC ≤ 29.99
# - Obesidade I: 30 ≤ IMC ≤ 34.99
# - Obesidade II (severa): 35 ≤ IMC ≤ 39.99
# - Obesidade III (mórbida): IMC ≥ 40

# Entrada do peso
peso = float(input("Digite seu peso (kg): "))
# Entrada da altura
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
IMC = peso / (altura ** 2)

# Classificação do IMC
if IMC < 17:
    print("{} Muito abaixo do peso".format('%.2f' % IMC))
elif 17 <= IMC <= 18.49:
    print("{} Abaixo do peso".format('%.2f' % IMC))
elif 18.50 <= IMC <= 24.99:
    print("{} Peso normal".format('%.2f' % IMC))
elif 25 <= IMC <= 29.99:
    print("{} Acima do peso".format('%.2f' % IMC))
elif 30 <= IMC <= 34.99:
    print("{} Obesidade I".format('%.2f' % IMC))
elif 35 <= IMC <= 39.99:
    print("{} Obesidade II (severa)".format('%.2f' % IMC))
elif IMC >= 40:
    print("{} Obesidade III (mórbida)".format('%.2f' % IMC))
