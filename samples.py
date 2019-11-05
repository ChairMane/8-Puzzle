from queue import PriorityQueue
import numpy as np
import copy
import time


class samples:
    def __init__(self):
        self.list_of_samples = []

    def fill_list(self):
        trivial = ('trivial', [np.array([[1, 2, 3],
                                        [4, 5, 6]],
                                        [7, 8, 0])])

        very_easy = ('very easy', [np.array([[1, 2, 3],
                                             [4, 5, 0],
                                             [7, 8, 6]]),
                                   np.array([[1, 2, 3],
                                             [4, 5, 6],
                                             [7, 0, 8]])])

        easy = ('easy', [np.array([[1, 2, 0],
                                   [4, 5, 3],
                                   [7, 8, 6]]),
                         np.array([[1, 2, 3],
                                   [4, 5, 6],
                                   [0, 7, 8]]),
                         np.array([[1, 2, 3],
                                   [4, 0, 5],
                                   [7, 8, 6]]),
                         np.array([[1, 2, 3],
                                   [0, 5, 6],
                                   [4, 7, 8]]),
                         np.array([[1, 0, 2],
                                   [4, 5, 3],
                                   [7, 8, 6]])])

        doable = ('doable', [np.array([[0, 1, 2],
                                       [4, 5, 3],
                                       [7, 8, 6]]),
                             np.array([[0, 2, 3],
                                       [1, 5, 6],
                                       [4, 7, 8]]),
                             np.array([[1, 3, 0],
                                       [4, 2, 6],
                                       [7, 5, 8]]),
                             np.array([[1, 2, 3],
                                       [5, 0, 6],
                                       [4, 7, 8]]),
                             np.array([[1, 5, 2],
                                       [4, 0, 3],
                                       [7, 8, 6]])])

        oh_boy = ('oh boy', [np.array([[8, 7, 1],
                                       [6, 0, 2],
                                       [5, 4, 3]]),
                             np.array([[1, 7, 3],
                                       [8, 0, 5],
                                       [4, 6, 2]]),
                             np.array([[6, 4, 7],
                                       [8, 5, 0],
                                       [3, 2, 1]]),
                             np.array([[8, 6, 7],
                                       [2, 5, 4],
                                       [3, 0, 1]]),
                             np.array([[3, 0, 1],
                                       [4, 6, 5],
                                       [7, 8, 2]])])

        self.list_of_samples.append(trivial)
        self.list_of_samples.append(very_easy)
        self.list_of_samples.append(easy)
        self.list_of_samples.append(doable)
        self.list_of_samples.append(oh_boy)

        return self.list_of_samples