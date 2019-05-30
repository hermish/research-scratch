import numpy as np
import quadprog as qp
from scipy import linalg

import graphs
import algebra

INCLUDED_THRESHOLD = 0.6


def semi_random_planted_clique(adjacency, clique_size, clean=True):
    """
    :param int[][] adjacency: an adjacency matrix of the semi-random planted
        clique graph
    :param int clique_size: the size of the clique
    :param boolean clean: whether to clean the result by making a pass through
        the vertices and including those with a sufficient number of vertices
    :return int[]: a list of integers corresponding to potential vertices
    """
    size = len(adjacency)
    average_matrix = np.full((size, size), 0.5)
    difference = adjacency - average_matrix
    least = linalg.eigh(difference, eigvals=(0, 0), eigvals_only=True)
    shift = np.abs(least) + 1 if least < 0 else 0

    objective = algebra.manual_add_identity(difference, shift)
    linear = np.zeros(size)
    constraints = _build_constraint_matrix(size)
    bounds = _build_bounds_vector(size, clique_size)

    # Minimize 1/2 x^T G x - a^T x
    # Subject to C.T x >= b
    solution, _, _, _, _, _ = qp.solve_qp(
        G=objective, a=linear, C=constraints, b=bounds, meq=1)
    abs_solution = np.abs(solution)
    dominating = algebra.get_largest_indices(abs_solution, clique_size)

    if not clean:
        return dominating
    return _select_connected_vertices(
        adjacency, dominating, INCLUDED_THRESHOLD * clique_size)


def _build_constraint_matrix(size):
    """
    :param int size: the number of vertices in the graph
    :return float[][]: the constraint matrix corresponding to the quadratic
        program
    """
    constraints = np.zeros((size, 2 * size + 1))
    for pos in range(size):
        constraints[pos][0] = 1
    for pos in range(size):
        constraints[pos][pos + 1] = 1
    for pos in range(size):
        constraints[pos][size + pos + 1] = -1
    return constraints


def _build_bounds_vector(size, clique_size):
    """
    :param int size: the number of vertices in the graph
    :param clique_size: the number of vertices in the planted clique
    :return float[]: the bounds vector for the quadratic program
    """
    bounds = np.zeros(2 * size + 1)
    bounds[0] = np.sqrt(clique_size)
    for pos in range(size):
        bounds[size + pos + 1] = - 1 / np.sqrt(clique_size)
    return bounds


def random_planted_clique(adjacency, clique_size, clean=True):
    """
    Attempts to recover the planted clique hidden within a graph.

    :param int[][] adjacency: the adjacency matrix of a random graph with a
        planted clique
    :param int clique_size: the size of the planted clique to be found
    :param boolean clean: whether to clean the result by making a pass through
        the vertices and including those with a sufficient number of vertices
    :return int[]: a list of integers corresponding to potential vertices
    """
    size = len(adjacency)
    average_matrix = np.full((size, size), 0.5)
    difference = adjacency - average_matrix
    _, vectors = linalg.eigh(difference, eigvals=(size - 1, size - 1))
    abs_eigenvector = np.abs(np.reshape(vectors, size))
    dominating = algebra.get_largest_indices(abs_eigenvector, clique_size)

    if not clean:
        return dominating
    return _select_connected_vertices(
        adjacency, dominating, INCLUDED_THRESHOLD * clique_size)


def _select_connected_vertices(adjacency, included, threshold):
    """
    :param int[][] adjacency: the adjacency matrix of a random graph
    :param int[] included: a list corresponding to a subset of the vertices
    :param float threshold: the minimum number of neighbours needed
    :return int[]: a list of all vertices which have at least as many neighbors
        in the included set as specified by the THRESHOLD parameter
    """
    size = len(adjacency)
    sufficiently_connected = []
    for vertex in range(size):
        neighbors = sum(adjacency[vertex][other] for other in included)
        if neighbors >= threshold:
            sufficiently_connected.append(vertex)
    return sufficiently_connected


def _compare_solution(solution, true_solution):
    """
    :param int[] solution: the solution to be compared to the correct answer
    :param true_solution: the correction solution to the clique problem
    :return string: a description of the closeness of the proposed solution,
        including its size compared to the true solution and accuracy
    """
    correct_set = set(true_solution)
    correct, incorrect = 0, 0
    for vertex in solution:
        if vertex in correct_set:
            correct += 1
        else:
            incorrect += 1
    return 'Size: {}/{}, Correct: {}, Incorrect: {}'.format(
        len(solution), len(true_solution), correct, incorrect)


if __name__ == '__main__':
    CLIQUE_SIZE = 30
    SIZE, PARAMETER = 100, 0.5

    clique_vertices = np.random.choice(SIZE, size=CLIQUE_SIZE, replace=False)
    random_graph = graphs.generate_bernoulli_graph(SIZE, PARAMETER)
    clique_graph = graphs.generate_clique_graph(SIZE, clique_vertices)
    planted_graph = graphs.union_graphs(random_graph, clique_graph)

    result = semi_random_planted_clique(planted_graph, CLIQUE_SIZE, clean=False)

    print(clique_vertices)
    print(result)
    print(_compare_solution(result, clique_vertices))
