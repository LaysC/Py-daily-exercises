# Tabuada

# Enunciado:
# O programa deve receber um número como entrada e exibir sua tabuada de 1 a 10.
# A saída deve seguir o formato:
# "X x Y = Z", onde X é o número informado, Y varia de 1 a 10, e Z é o resultado da multiplicação.

# Solicita ao usuário qual tabuada deseja visualizar
valor = float(input("Digite o número para ver sua tabuada: "))

# Exibe o cabeçalho da tabuada
print("Tabuada do", valor)

# Loop para calcular e exibir a tabuada de 1 a 10
for item in range(1, 11):
    resultado = valor * item  # Multiplicação do número pelo item da tabuada
    print(valor, "x", item, "=", resultado)  # Exibição do resultado
