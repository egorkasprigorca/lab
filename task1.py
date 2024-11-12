# Функция для красивого отображения матрицы с коэффициентом
def print_matrix(matrix, name="Матрица", coefficient=1):
    # Печать заголовка и коэффициента
    print(f"{name} = {coefficient} * ⎡", end="")
    # Определение ширины для выравнивания
    max_len = max(len(f"{elem:6.2f}") for row in matrix for elem in row) + 2
    for i, row in enumerate(matrix):
        if i > 0:
            print(" " * (len(name) + 4), end="")  # Выравнивание строк для красивого вывода
        print("   ".join(f"{elem:{max_len}.2f}" for elem in row), end=" ")
        if i == len(matrix) - 1:
            print("⎤")  # Закрытие матрицы для последней строки
        else:
            print("⎥")  # Вертикальные линии для промежуточных строк
    print("\n")

# Функция для красивого отображения вектора
def print_vector(vector, name="Вектор", coefficient=1):
    # Печать заголовка и коэффициента
    print(f"{name} = {coefficient} * [", "  ".join(f"{elem:.2f}" for elem in vector), "]\n")

# Универсальное умножение матриц с коэффициентами
def matrix_multiplication(A, B, coef_A=1, coef_B=1):
    if len(A[0]) != len(B):
        raise ValueError("Число столбцов матрицы A должно быть равно числу строк матрицы B.")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += coef_A * A[i][k] * coef_B * B[k][j]
    return result

# Универсальное умножение матрицы на вектор с коэффициентом
def matrix_vector_multiplication(A, v, coef_A=1, coef_v=1):
    if len(A[0]) != len(v):
        raise ValueError("Число столбцов матрицы должно быть равно размеру вектора.")
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(v)):
            result[i] += coef_A * A[i][j] * coef_v * v[j]
    return result

# Универсальное тензорное произведение матриц с коэффициентами
def tensor_product_matrices(A, B, coef_A=1, coef_B=1):
    result = []
    for i in range(len(A)):
        for j in range(len(B)):
            row = []
            for k in range(len(A[0])):
                for l in range(len(B[0])):
                    row.append(coef_A * A[i][k] * coef_B * B[j][l])
            result.append(row)
    return result

# Универсальное тензорное произведение векторов с коэффициентами
def tensor_product_vectors(v, w, coef_v=1, coef_w=1):
    result = []
    for i in range(len(v)):
        for j in range(len(w)):
            result.append(coef_v * v[i] * coef_w * w[j])
    return result

# Функция перевода вектора в скобочную нотацию для произвольного числа состояний с коэффициентом
def vector_to_bracket_notation(v, coef=1):
    n = len(v)
    num_qubits = (n - 1).bit_length()  # Определяем количество кубитов
    notation = " + ".join(f"{coef * coef_v:.2f}|{format(i, f'0{num_qubits}b')}⟩" for i, coef_v in enumerate(v) if coef * coef_v != 0)
    return notation

# Функция перевода из скобочной нотации в вектор (принимает список коэффициентов)
def bracket_to_vector_notation(*coefficients):
    return list(coefficients)

# Примеры использования функций с реалистичными матрицами и коэффициентами

# Матрицы, моделирующие, например, квантовые операторы или состояния
A = [[0.707, -0.707], [0.707, 0.707]]  # Матрица поворота на 45 градусов
B = [[0.5, 0.5], [0.5, -0.5]]          # Гейтовая матрица Адамара (Hadamard)
v = [1, 0]                             # Базисное состояние |0⟩
w = [0, 1]                             # Базисное состояние |1⟩
vector = [0.6, 0.8]                    # Состояние суперпозиции

coef_A = 2   # Коэффициент для матрицы A
coef_B = 1.5 # Коэффициент для матрицы B
coef_v = 0.9 # Коэффициент для вектора v
coef_w = 1.2 # Коэффициент для вектора w

# Примеры вычислений с коэффициентами
print("=== Примеры вычислений с матрицами и векторами ===")

C = matrix_multiplication(A, B, coef_A, coef_B)
print_matrix(A, "Матрица A", coef_A)
print_matrix(B, "Матрица B", coef_B)
print_matrix(C, "Результат умножения A и B с коэффициентами")

Av = matrix_vector_multiplication(A, v, coef_A, coef_v)
print_matrix(A, "Матрица A", coef_A)
print_vector(v, "Вектор v", coef_v)
print_vector(Av, "Результат умножения матрицы A на вектор v с коэффициентами")

tensor_AB = tensor_product_matrices(A, B, coef_A, coef_B)
print_matrix(tensor_AB, "Тензорное произведение матриц A и B с коэффициентами")

tensor_vw = tensor_product_vectors(v, w, coef_v, coef_w)
print_vector(v, "Вектор v", coef_v)
print_vector(w, "Вектор w", coef_w)
print_vector(tensor_vw, "Результат тензорного произведения векторов v и w с коэффициентами")

# Печать в скобочной нотации
print("Вектор в скобочной нотации : ", vector_to_bracket_notation(vector, coef_v))

coef_tensor_vw = 1
# Печать в скобочной нотации
print("Вектор в скобочной нотации : ", vector_to_bracket_notation(tensor_vw, coef_tensor_vw))