# Contador de Entradas

# Enunciado:
# O programa deve contar quantas entradas o usuário faz, incluindo entradas vazias.
# O loop continua até que o usuário digite "FIM".
# Ao final, o programa deve exibir o total de entradas realizadas.

# Inicializa o contador
contador = 0

# Loop infinito para receber entradas
while True:
    resposta = input()  # Entrada do usuário

    if resposta == 'FIM':  # Condição de parada
        break
    else:
        contador += 1  # Incrementa o contador para cada entrada

# Exibe o total de entradas
print(contador)
