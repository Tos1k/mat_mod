import random


def generate_individual():
    return [random.randint(0, 30) for _ in range(4)]


def fitness(individual):
    a, b, c, d = individual
    return abs(a + 2 * b + 3 * c + 4 * d - 30)


def crossover(parent1, parent2):
    crossover_point = random.randint(1, 3)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(individual):
    index = random.randint(0, 3)
    individual[index] = random.randint(0, 30)
    return individual


def genetic_algorithm():
    population_size = 100
    generations = 1000
    population = [generate_individual() for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            break

        next_generation = []

        for _ in range(population_size // 2):
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            next_generation.extend([child1, child2])

        population = next_generation

    return population[0]


solution = genetic_algorithm()
print("Решение диофантова уравнения a + 2b + 3c + 4d = 30, найденное с использованием генетического алгоритма:")
print(solution)
