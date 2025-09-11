import numpy as np
import matplotlib.pyplot as plt


# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def tanh(x):
    return np.tanh(x)


def relu(x):
    return np.maximum(0, x)


def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)


def softmax(x):
    e_x = np.exp(x - np.max(x))  # stability improvement
    return e_x / e_x.sum()


# Input values
x = np.linspace(-10, 10, 1000)
x_softmax = np.linspace(-2, 2, 10)

# Function outputs
y_sigmoid = sigmoid(x)
y_tanh = tanh(x)
y_relu = relu(x)
y_leaky_relu = leaky_relu(x)
y_softmax = softmax(x_softmax)

# Plotting
plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.plot(x, y_sigmoid, label="Sigmoid", color='blue')
plt.title("Sigmoid Function")
plt.grid(True)

plt.subplot(3, 2, 2)
plt.plot(x, y_tanh, label="Tanh", color='orange')
plt.title("Tanh Activation Function")
plt.grid(True)

plt.subplot(3, 2, 3)
plt.plot(x, y_relu, label="ReLU", color='green')
plt.title("ReLU Activation Function")
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(x, y_leaky_relu, label="Leaky ReLU", color='red')
plt.title("Leaky ReLU Activation Function")
plt.grid(True)

plt.subplot(3, 2, 5)
plt.stem(x_softmax, y_softmax, basefmt=" ", linefmt='purple', markerfmt='o')
plt.title("Softmax Activation Function")
plt.grid(True)

plt.tight_layout()
plt.show()
