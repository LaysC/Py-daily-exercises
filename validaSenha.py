# Validação de Senha

# Enunciado:
# O programa deve receber uma senha e validar se ela atende aos seguintes critérios:
# 1. Deve conter pelo menos 8 caracteres.
# 2. Deve conter pelo menos 2 dígitos numéricos.
# 3. O número de vogais deve ser maior ou igual ao número de dígitos.
# Se qualquer uma das condições não for atendida, o programa deve exibir "ERRO".
# Caso contrário, deve exibir "OK".

# Entrada da senha
senha = input("Digite a senha: ")

# Definição de caracteres considerados vogais e dígitos
vogais = 'AEIOUaeiou'
digitos = '0123456789'

# Contadores de vogais e dígitos
num_vogais = sum(1 for caracter in senha if caracter in vogais)
num_digitos = sum(1 for caracter in senha if caracter in digitos)

# Comprimento da senha
comprimento_senha = len(senha)

# Validação da senha com base nas regras estabelecidas
if num_vogais < num_digitos:
    print("ERRO")
elif num_digitos < 2:
    print("ERRO")
elif comprimento_senha < 8:
    print("ERRO")
else:
    print("OK")
