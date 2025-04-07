import numpy as np

# 1️⃣1️⃣ Criar uma matriz NumPy 3x3 e exibir sua transposta.
matriz_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz transposta:\n", matriz_np.T)

# 1️⃣2️⃣ Criar uma matriz 4x4 de zeros usando np.zeros().
matriz_zeros = np.zeros((4, 4))
print("Matriz de zeros:\n", matriz_zeros)

# 1️⃣3️⃣ Criar uma matriz 4x4 de uns usando np.ones().
matriz_uns = np.ones((4, 4))
print("Matriz de uns:\n", matriz_uns)

# 1️⃣4️⃣ Criar uma matriz NumPy 3x3 com valores aleatórios entre 1 e 50.
matriz_rand = np.random.randint(1, 51, (3, 3))
print("Matriz aleatória:\n", matriz_rand)

# 1️⃣5️⃣ Criar duas matrizes 3x3 e somá-las.
matriz_a = np.random.randint(1, 10, (3, 3))
matriz_b = np.random.randint(1, 10, (3, 3))
soma_matrizes = matriz_a + matriz_b
print("Soma das matrizes:\n", soma_matrizes)

# 1️⃣6️⃣ Criar uma matriz 3x3 e multiplicar todos os elementos por um número fixo.
multiplicacao = matriz_np * 2
print("Matriz multiplicada por 2:\n", multiplicacao)

# 1️⃣7️⃣ Criar uma matriz 3x3 e dividir todos os elementos por 2.
divisao = matriz_np / 2
print("Matriz dividida por 2:\n", divisao)

# 1️⃣8️⃣ Criar uma matriz 3x3 e calcular seu determinante.
determinante = np.linalg.det(matriz_np)
print("Determinante da matriz:", determinante)

# 1️⃣9️⃣ Criar uma matriz 4x4 e calcular a soma das colunas.
matriz_4x4 = np.random.randint(1, 10, (4, 4))
soma_colunas = np.sum(matriz_4x4, axis=0)
print("Soma das colunas:\n", soma_colunas)

# 2️⃣0️⃣ Criar uma matriz 4x4 e calcular a soma das linhas.
soma_linhas = np.sum(matriz_4x4, axis=1)
print("Soma das linhas:\n", soma_linhas)