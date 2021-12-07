import random
import numpy as np

# ADALINE

class Adaline(object):
    def __init__(self, no_of_inputs, learning_rate=0.01, iterations=100, bias=True):
        self.no_of_inputs = no_of_inputs
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = np.random.random(2 * self.no_of_inputs)
        self.bias = bias
        if self.bias:
            self.weights = (np.random.rand(2 * self.no_of_inputs + 1) - 0.5) / 1000
        else:
            self.weights = (np.random.rand(2 * self.no_of_inputs) - 0.5) / 1000
        self.errors = []

    def train(self, training_data_x, training_data_y):
        training_data_x = self.normalize(training_data_x) - 0.5 * 0.01
        training_data_y = self.normalize(training_data_y) - 0.5 * 0.01
        for _ in range(self.iterations):
            e = 0
            array = list(zip(training_data_x, training_data_y))
            random.shuffle(array)
            for x, y in array:  # Zadanie: losowy wybor przykladow uczacych.
                out = self.output(x)
                x = np.concatenate([x, self.fourier_transform(x)])
                if self.bias:
                    x = np.concatenate([x, [1]])
                self.weights += self.learning_rate * (y - out) * x
                e += (y - out) ** 2
            self.errors.append(e)

    def fourier_transform(self, x):
        a = np.abs(np.fft.fft(x))
        a[0] = 0
        return a / np.amax(a)

    def normalize(self, x):
        return (x - np.min(x)) / (np.max(x) - np.min(x))

    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    def output(self, x):
        # print(x)
        inp = np.concatenate([x, self.fourier_transform(x)])
        if self.bias:
            inp = np.concatenate([inp, [1]])
        summation = self.activation(np.dot(self.weights, inp))
        return summation


# ADALINE

