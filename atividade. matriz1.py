# 1️⃣ Criar uma matriz 3x3 e imprimir todos os elementos.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in matriz:
    print(linha)

    
# 2️⃣ Criar uma matriz 4x4 e acessar o elemento da segunda linha e terceira coluna.
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Elemento na segunda linha e terceira coluna:", matriz[1][2])


# 3️⃣ Criar uma matriz identidade 3x3 manualmente.
matriz_identidade = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
for linha in matriz_identidade:
    print(linha)


# 4️⃣ Criar uma matriz 3x3 e calcular a soma de todos os elementos.
soma = sum(sum(linha) for linha in matriz)
print("Soma dos elementos:", soma)


# 5️⃣ Criar uma matriz 3x3 e exibir apenas os elementos da diagonal principal.
diagonal_principal = [matriz[i][i] for i in range(3)]
print("Diagonal principal:", diagonal_principal)


# 6️⃣ Criar uma matriz 3x3 e exibir apenas os elementos da diagonal secundária.
diagonal_secundaria = [matriz[i][2 - i] for i in range(3)]
print("Diagonal secundária:", diagonal_secundaria)


# 7️⃣ Criar uma matriz 3x3 e inverter a ordem das linhas.
matriz_invertida = matriz[::-1]
for linha in matriz_invertida:
    print(linha)


# 8️⃣ Criar uma matriz 3x3 e calcular a média dos elementos.
quantidade_elementos = 3 * 3
media = soma / quantidade_elementos
print("Média dos elementos:", media)


# 9️⃣ Criar uma matriz 3x3 e encontrar o maior e o menor elemento.
maior = max(max(linha) for linha in matriz)
menor = min(min(linha) for linha in matriz)
print("Maior elemento:", maior)
print("Menor elemento:", menor)


# 🔟 Criar uma matriz 4x4 e verificar se um determinado número existe nela.
numero_procurado = 10
encontrado = any(numero_procurado in linha for linha in matriz)
print(f"O número {numero_procurado} {'existe' if encontrado else 'não existe'} na matriz.")

