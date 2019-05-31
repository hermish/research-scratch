import numpy as np
from scipy.stats import ortho_group


def sum_of_fourth_powers(matrix):
    """
    :param matrix: (numpy.ndarray) A numpy array.
    :return: The fourth power of the four-norm of the matrix. In other words,
        the sum of the fourth power of all of its entries.
    """
    return np.sum(matrix * matrix * matrix * matrix)


def get_random_orthogonal(size):
    """
    :param size: (int) The dimension of the matrix.
    :return: (numpy.ndarray) Returns a random orthogonal matrix from O(SIZE),
        the orthogonal group of dimension SIZE, drawn from the Haar
        distribution. The matrix has size (SIZE, SIZE).
    """
    return ortho_group.rvs(size)


def get_bernoulli_gaussian(theta, size):
    """
    :param theta: (float) The probability a particular entry is non-zero: must
        be between 0 and 1 inclusive. The smaller THETA is, the more sparse the
        output will be in expectation.
    :param size: (int or tuple) The shape of the output.
    :return: (numpy.ndarray) A random numpy array where each entry is from
        independently and identically distributed according  to a bernoulli-
        gaussian
    """
    bernoulli = np.random.binomial(1, theta, size)
    gaussian = np.random.standard_normal(size)
    result = bernoulli * gaussian
    return result


def random_dictionary_learning_instance(features, samples, theta):
    """
    :param features: (int) The number of features for each sample, equivalently
        the length of the signal.
    :param samples: (int) The number of samples or signals.
    :param theta: (float) The probability a particular entry in the decoded
        samples is non-zero. The smaller THETA is, the sparser the signals
        are in the optimal, intended, basis.
    :return: (tuple)
    """
    dictionary = get_random_orthogonal(features)
    samples = get_bernoulli_gaussian(theta, (features, samples))
    observations = dictionary @ samples
    return observations, dictionary, samples
