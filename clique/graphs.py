import numpy as np


def generate_bernoulli_graph(size, parameter):
    """
    :param int size: the number of vertices in the graph
    :param float parameter: the probability each edge is independently included
    :return int[][]: the adjacency matrix of a random bernoulli graph
    """
    matrix = np.zeros((size, size), dtype=np.int16)
    for row in range(size):
        for col in range(row):
            value = np.random.uniform()
            if value < parameter:
                matrix[row][col] = 1
                matrix[col][row] = 1
    return matrix


def generate_clique_graph(size, vertices):
    """
    :param int size: number of vertices in the graph
    :param int[] vertices: a list of indices corresponding to clique vertices
    :return: the adjacency matrix of a graph consisting solely of a clique with
        the specified vertices, consisting of exactly len(VERTICES) ** 2 / 2
        edges
    """
    matrix = np.zeros((size, size), dtype=np.int16)
    for first in vertices:
        for second in vertices:
            matrix[first][second] = 1
    for first in vertices:
        matrix[first][first] = 0
    return matrix


def union_graphs(first_matrix, second_matrix):
    """
    :param int[][] first_matrix: an adjacency matrix
    :param int[][] second_matrix: an adjacency matrix
    :return int[][]: a union of both graphs, namely a graph where each edge
        occurs if it was in either of the input graphs
    :raises AssertionError: either matrix is not a valid adjacency matrix
        for a simple undirected graph
    """
    # tests.graphs.validate_simple_undirected(first_matrix)
    # tests.graphs.validate_simple_undirected(second_matrix)
    combined = np.bitwise_or(first_matrix, second_matrix)
    return combined


def get_laplacian_matrix(adjacency):
    """
    :param int[][] adjacency: an adjacency matrix
    :return: computes the Laplacian matrix for the graph, equivalent to
        computing the degree matrix and subtracting the adjacency matrix
    """
    size = len(adjacency)
    flipped = -adjacency
    for pos in range(size):
        flipped[pos][pos] = adjacency[pos].sum()
    return flipped


if __name__ == '__main__':
    one = generate_bernoulli_graph(5, 0.5)
    two = generate_bernoulli_graph(5, 0.5)
    print(one, '\n', two)
    print(union_graphs(one, two))


def validate_simple_undirected(matrix):
    """
    :param float[][] matrix: an adjacency matrix
    :return None: no return value
    :raises AssertionError: raises an error if the matrix is not a valid
        adjacency matrix for a simple undirected graph
    """
    size = len(matrix)
    for row in range(size):
        for col in range(row):
            assert matrix[row][col] == matrix[col][row]
    for pos in range(size):
        assert not matrix[pos][pos]
