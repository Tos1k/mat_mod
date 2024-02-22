from scipy import spatial

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

import random
import array

import numpy as np
import matplotlib.pyplot as plt


class TravelingSalesmanProblem:

    def __init__(self):

        # Инициализация базовых переменных:
        self.locations = []
        self.distances = []
        self.tspSize = 0

        # initialize the data:
        self.__initData()

    def __len__(self):
        return self.tspSize

    def __initData(self):
        if not self.locations or not self.distances:
            self.__createData()

        # set the problem 'size':
        self.tspSize = len(self.locations)

    def __createData(self):

        self.locations = []

        num_points = 10
        self.locations = np.random.rand(num_points, 2)  # генерация рандомных вершин
        self.distances = list(spatial.distance.cdist(self.locations, self.locations, metric='euclidean'))
        self.tspSize = len(self.distances)

    def getTotalDistance(self, indices):

        print(indices)
        # растояние между первым и последним городом
        distance = self.distances[indices[-1]][indices[0]]

        # растояние между каждыми городами
        for i in range(len(indices) - 1):
            distance += self.distances[indices[i]][indices[i + 1]]

        return distance

    def plotData(self, indices):
        plt.scatter(*zip(*self.locations), marker='.', color='red')

        locs = [self.locations[i] for i in indices]
        locs.append(locs[0])

        plt.plot(*zip(*locs), linestyle='-', color='blue')

        return plt


RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# создаем объект класса задачи комивояжера :

tsp = TravelingSalesmanProblem()

# Постоянные ген. алгоритма:
POPULATION_SIZE = 300
MAX_GENERATIONS = 200
HALL_OF_FAME_SIZE = 1
P_CROSSOVER = 0.9  # вероятность скрещивания
P_MUTATION = 0.1  # вероятность мутации

toolbox = base.Toolbox()

# определяем поведение fitness функции:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# create the Individual class based on list of integers:
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

# определяем функцию генерации случайных чисел:
toolbox.register("randomOrder", random.sample, range(len(tsp)), len(tsp))

# определяем функции генерации генома особи
toolbox.register("individualCreator", tools.initIterate, creator.Individual, toolbox.randomOrder)

# определяем функцию генерации нового поколения
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# расчитываем расстояние между городами в генах
def tpsDistance(individual):
    return tsp.getTotalDistance(individual),  # return a tuple


toolbox.register("evaluate", tpsDistance)

# Операции ген. алгоритма:
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0 / len(tsp))


def main():
    # Создаем первое поколение:
    population = toolbox.populationCreator(n=POPULATION_SIZE)

    # Подготавливаем данные для статистики:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)

    # Определяем кол-во лучших особей:
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    population, logbook = algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=False)

    # Показываем лучшее решение:
    best = hof.items[0]
    plt.figure(1)
    tsp.plotData(best)

    # Показываем статистику:
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")
    plt.figure(2)
    # sns.set_style("whitegrid")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Поколение')
    plt.ylabel('Минимальное и среднее')
    plt.title('Минимальное и среднее значение fitness функции поколений')

    plt.show()


if __name__ == "__main__":
    main()
