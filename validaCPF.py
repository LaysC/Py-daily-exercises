# Validação de CPF

# Enunciado:
# O programa deve receber um CPF como entrada, verificando se ele contém apenas caracteres válidos (números, pontos e traços).
# Além disso, deve validar se há exatamente 11 dígitos numéricos.
# Se houver caracteres inválidos, o programa deve exibir "Erro de codificação".
# Se a quantidade de números for diferente de 11, deve exibir "Erro no tamanho".
# Se ambas as condições forem inválidas, ambas as mensagens devem ser exibidas.
# Caso contrário, o programa deve exibir apenas os números do CPF sem pontos e traços.

# Entrada do CPF
cpf = input("Digite o CPF: ")

# Definição de caracteres permitidos
caracteres_validos = '0123456789.-'
numeros = ''  # Armazena apenas os números do CPF
estado = False  # Indica se há caracteres inválidos

# Loop para percorrer cada caractere do CPF
for caractere in cpf:
    if caractere not in ".-":  # Ignora pontos e traços, armazenando apenas números
        numeros += caractere

    if caractere not in caracteres_validos:  # Verifica caracteres inválidos
        estado = True

# Validação do CPF
if estado and len(numeros) != 11:
    print("Erro de codificação")
    print("Erro no tamanho")
elif estado:
    print("Erro de codificação")
elif len(numeros) != 11:
    print("Erro no tamanho")
else:
    print(numeros)  # Exibe apenas os números do CPF
