# It's a demo for the back propagation of multi-class MLP with one hidden layer.
import numpy as np


def ReLU(x):
    x[x <= 0] = 0
    return x


def Softmax(x):
    y = np.zeros(len(x))
    sum_x = np.sum(x)
    for i in range(len(x)):
        y[i] = np.exp(x[i]) / np.exp(sum_x)
    return y


class Layer:
    def __init__(self, input_size, output_size, activation_fuc):
        self.weights = np.random.rand(input_size, output_size)
        self.activation_fuc = activation_fuc

    def propagate(self, x):
        return self.activation_fuc(np.dot(self.weights.T, x))


class MLP:
    def __init__(self, layer_list):
        self.layers = layer_list

    def propagate(self, x):
        y = x
        print("Input layer: ", y)
        for i in self.layers:
            y = i.propagate(y)
            if i == self.layers[-1]:
                print("Output layer: ", y)
            else:
                print("Middle layer: ", y)
        return y

    def back_propagate(self,label):
        pass


if __name__ == '__main__':
    input_layer = Layer(2, 4, ReLU)
    hidden_layer = Layer(4, 2, Softmax)
    mlp = MLP([input_layer, hidden_layer])
    mlp.propagate(np.array([1, 2]))
