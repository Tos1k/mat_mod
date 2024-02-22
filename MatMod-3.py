import numpy as np
import matplotlib.pyplot as plt

def analytical_solution(x, y, Lx, Ly, N_terms=50):
    u = 0
    for n in range(1, N_terms + 1):
        for m in range(1, N_terms + 1):
            A_nm = 4 / ((2 * n - 1) * np.pi) * (1 - (-1)**n)
            B_nm = 2 / ((2 * m - 1) * np.pi) * (1 - (-1)**m)
            u += A_nm * B_nm * np.sin((2 * n - 1) * np.pi * x / Lx) * np.sin((2 * m - 1) * np.pi * y / Ly)

    return u

# Размеры области
Lx = 1.0
Ly = 1.0

# Генерация сетки
x = np.linspace(0, Lx, 100)
y = np.linspace(0, Ly, 100)
X, Y = np.meshgrid(x, y)

# Вычисление аналитического решения
analytical_result = analytical_solution(X, Y, Lx, Ly)

np.savetxt('analytical_solution.txt', analytical_result)

# Визуализация
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, analytical_result, cmap='viridis')
plt.colorbar(label='Solution')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Analytical Solution of Laplace Equation')
plt.grid(True)
plt.show()
