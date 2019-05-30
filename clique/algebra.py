import numpy as np


def manual_add_identity(matrix, scale):
    """
    :param int[][] matrix: a square matrix
    :param scale: the multiple of the identity to add
    :return: the matrix equivalent to performing MATRIX + SCALE * I
    """
    size = len(matrix)
    duplicate = np.copy(matrix)
    for pos in range(size):
        duplicate[pos][pos] += scale
    return duplicate


def get_largest_indices(array, number):
    """
    :param float[] array: the array to partition
    :param int number: the number of largest entries to extract
    :return float[] : the index of the NUMBER largest entries of ARRAY
    """
    partitioned = np.argpartition(array, number)
    return partitioned[-number:]
