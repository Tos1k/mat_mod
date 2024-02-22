import numpy as np
import matplotlib.pyplot as plt

def laplace_solver(nx, ny, xmax, ymax, num_iterations):
    dx = xmax / (nx - 1)
    dy = ymax / (ny - 1)

    # Инициализация сетки
    u = np.zeros((nx, ny))

    # Установка граничных условий
    u[0, :] = 0  # Нижняя граница
    u[-1, :] = 1  # Верхняя граница
    u[:, 0] = 0  # Левая граница
    u[:, -1] = 1  # Правая граница

    # Итерационное решение уравнения Лапласа
    for iteration in range(num_iterations):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                u[i, j] = 0.25 * (u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1])

    return u

def plot_solution(u, xmax, ymax):
    nx, ny = u.shape
    x = np.linspace(0, xmax, nx)
    y = np.linspace(0, ymax, ny)

    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, u, cmap='viridis', levels=20)
    plt.colorbar(label='Solution')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Numerical Solution of Laplace Equation')
    plt.show()

# Параметры сетки и области
nx = 50
ny = 50
xmax = 1.0
ymax = 1.0

# Количество итераций
num_iterations = 1000

# Решение уравнения Лапласа
solution = laplace_solver(nx, ny, xmax, ymax, num_iterations)

# Визуализация результатов
plot_solution(solution, xmax, ymax)
