# Impressão de Asteriscos

# Enunciado:
# O programa deve receber uma sequência de dígitos (0-9) como entrada.
# Para cada dígito fornecido, o programa deve imprimir uma linha com a quantidade correspondente de asteriscos.
# Por exemplo, se a entrada for "305", a saída será:
# ***
#
# *****
# (uma linha com 3 asteriscos, seguida de uma linha vazia, e depois nenhuma linha para 0).

# Entrada da sequência de dígitos
valor1 = input("Digite uma sequência de dígitos (0-9): ")

# Loop para percorrer cada caractere da entrada
for item in valor1:
    valor = int(item)  # Converte o caractere para um inteiro

    if 0 <= valor <= 9:  # Verifica se o valor está entre 0 e 9
        print('*' * valor)  # Imprime a quantidade correspondente de asteriscos