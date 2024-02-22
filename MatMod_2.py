import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

def laplace_solver_triangular(nx, ny, num_iterations):
    dx = 1.0 / (nx - 1)
    dy = 1.0 / (ny - 1)

    # Инициализация сетки
    u = np.zeros((nx * ny,))

    # Установка граничных условий
    for i in range(nx):  # Нижняя граница
        u[i] = 0

    for i in range(nx * (ny - 1), nx * ny):  # Верхняя граница
        u[i] = 1

    for i in range(0, nx * ny, nx):  # Левая граница
        u[i] = 0

    for i in range(nx - 1, nx * ny, nx):  # Правая граница
        u[i] = 1

    # Итерационное решение уравнения Лапласа на треугольной сетке
    for iteration in range(num_iterations):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                if i + j <= ny - 1:  # Условие треугольной сетки
                    index = i + j * nx
                    u[index] = 0.25 * (u[index + 1] + u[index - 1] + u[index + nx] + u[index - nx])

    return u

def plot_solution_triangular(u, nx, ny):
    # Создаем треугольную сетку
    triang = tri.Triangulation(np.repeat(np.arange(nx), ny), np.tile(np.arange(ny), nx))

    plt.figure(figsize=(8, 6))

    # Рисуем контурное представление
    plt.triplot(triang, color='black', linewidth=0.5)

    # Заполняем цветом в зависимости от уровня
    plt.tripcolor(triang, u, cmap='viridis', shading='flat', edgecolors='k')

    plt.colorbar(label='Solution')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Numerical Solution of Laplace Equation on Triangular Grid')
    plt.grid(True)  # Включение отображения сетки
    plt.show()

# Параметры сетки и области
nx = 50
ny = 50
num_iterations = 1000

# Решение уравнения Лапласа на треугольной сетке
solution_triangular = laplace_solver_triangular(nx, ny, num_iterations)

# Визуализация результатов
plot_solution_triangular(solution_triangular, nx, ny)
