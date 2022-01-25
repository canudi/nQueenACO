import numpy as np


class Problem:

    def __init__(self, n: int, alpha: float, beta: float):
        """

        :param n: the dimension of the problem
        """
        self.n = n
        self.alpha = alpha
        self.beta = beta
        self.__board = np.array(np.zeros((self.n, self.n)), dtype=bool)
        self.__pheromones = np.zeros((self.n ** 2, self.n))  # each square on the board, has n edges

    def print(self):
        print(self.__board)

    def getPheromones(self, x, y):
        """ returns the pheromones vector for a specific square x, y """
        return self.__pheromones[x * self.n + y]


class Ant:

    def __init__(self, problem: Problem):
        self.__p = problem
        # self.__board = np.array(np.zeros((self.__p.n, self.__p.n)), dtype=bool)
        x, y = 0, np.random.randint(8)     # an ants tour starts in a random square in row 0
        # self.__board[x, y] = 1
        self.__currSquare = x, y
        self.__tour = [y]

    def step(self):
        """ the ant chooses the next queen to apply on the board using roulette """
        x, y = self.__currSquare
        pr = np.cumsum(self.__p.getPheromones(x, y))
        r = np.random.rand()
        y = 0
        while pr[y]/pr[-1] < r:         # pr[-1] is the sum of pheromones
            y += 1
        x += 1
        # self.__board[x, y] = 1
        self.__tour.append(y)
        self.__currSquare = x, y

    def placePheromones(self, fitnessFunc):
        """ TODO """
        pass


