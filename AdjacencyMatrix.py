import numpy as np
import random


def createMatrix(vertices,P):
    matrix = np.zeros([vertices, vertices], dtype=int)
    for i in range(0, vertices):
        for j in range(i+1, vertices):
            x = random.random()
            if (x>=0 and x<=P):
                matrix[i][j] = 1
                matrix[j][i] = 1
        matrix[i][i] = 1
    return matrix
