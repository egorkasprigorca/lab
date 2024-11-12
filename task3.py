import numpy as np

# Функция для моделирования измерения квантового регистра
def measure_quantum_register(state):
    # Вычисление вероятностей для каждого состояния (квадрат модуля амплитуды)
    probabilities = [round(abs(amplitude)**2, 2) for amplitude in state]
    
    # Нормализация вероятностей до 1, если сумма не равна 1
    probabilities = [p / sum(probabilities) for p in probabilities]
    
    # Выполнение измерения с выбором состояния на основе вероятностей
    result = np.random.choice(range(len(state)), p=probabilities)
    return result, probabilities

# Пример состояния регистра
# Пусть регистр содержит 4 состояния с амплитудами, моделирующими суперпозицию:
# |Ψ⟩ = 0.5|00⟩ + 0.5|01⟩ + 0.5|10⟩ + 0.5|11⟩
state = np.array([0.5, 0.5, 0.5, 0.5])

# Функция перевода вектора в скобочную нотацию
def vector_to_bracket_notation(v):
    return f"{v[0]:.2f}|00⟩ + {v[1]:.2f}|01⟩ + {v[2]:.2f}|10⟩ + {v[3]:.2f}|11⟩"

print("Вектор в скобочной нотации:", vector_to_bracket_notation(state))

# Измерение квантового регистра
result, probabilities = measure_quantum_register(state)
print("Измерение квантового регистра:")
print(f"Результат: |{result:2b}⟩, Вероятности: {probabilities}")
