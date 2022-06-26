
class MLP:
    def __init__(self, train_data, target, lr=0.1, num_epochs=100, num_input=2, num_hidden=2, num_output=1):
        self.train_data = train_data
        self.target = target
        self.lr = lr
        self.num_epochs = num_epochs

        self.weights_01 = np.random.uniform(size=(num_input, num_hidden)) #(2, 2)
        self.b01 = np.random.uniform(size=(1, num_hidden)) #(1, 2)

        self.weights_12 = np.random.uniform(size=(num_hidden, num_output)) #(2, 1)
        self.b12 = np.random.uniform(size=(1, num_output)) #(1, 1)

        self.losses = []
    
    def forward(self, batch):

        self.hidden_ = np.dot(batch, self.weights_01) + self.b01 #batch(4, 2), weight(2, 2), b01(1, 2), hidden(4, 2)
        #self.hidden_out = self._sigmoid(self.hidden_) #hidden(4, 2)
        self.hidden_out = self._tanh(self.hidden_) #hidden(4, 2)
        
        self.output_ = np.dot(self.hidden_out, self.weights_12) + self.b12 #hidden(4, 2), weight12(2, 1), b12(1, 1), output(4, 1)
        #self.output_final = self._sigmoid(self.output_) #output(4, 1)
        self.output_final = self._tanh(self.output_) #output(4, 1)
        return self.output_final

    def update_weight(self):

        loss = 0.5 * (self.target - self.output_final) ** 2
        self.losses.append(np.sum(loss))

        error_term = (self.output_final - self.target) #derivation of error with respect to the last layer

        # the gradient for the output layer weights
        #grad12 = error_term * self._delsigmoid(self.output_final)
        grad12 = error_term * self._deltanh(self.output_final)

        #the gradient for the hidden layer weight
        #grad01 = np.dot(grad12, self.weights_12.T) * self._delsigmoid(self.hidden_out)
        grad01 = np.dot(grad12, self.weights_12.T) * self._deltanh(self.hidden_out)

        #updating weights
        self.weights_12 -= self.lr * np.dot(self.hidden_out.T, grad12)
        self.weights_01 -= self.lr * np.dot(self.train_data.T, grad01)

        #update the biases
        self.b12 -= self.lr * np.sum(grad12, axis=0)
        self.b01 -= self.lr * np.sum(grad01, axis=0)

    def _sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def _delsigmoid(self, x):
        return x * (1-x)

    def _tanh(self, x):
        return np.tanh(x)
    
    def _deltanh(self, x):
        return 1 - x*x

    def classify(self, datapoint):
        if self.forward(datapoint) >= 0.5:
            return 1
        return 0
    
    def plot(self, h=0.01):
        """
        Generate plot of input data and decision boundary.
        """
        # setting plot properties like size, theme and axis limits
        sns.set_style('darkgrid')
        plt.figure(figsize=(10, 10))

        plt.axis('scaled')
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)

        colors = {
            0: "ro",
            1: "go"
        }

        # plotting the four datapoints
        for i in range(len(self.train_data)):
            plt.plot([self.train_data[i][0]],
                     [self.train_data[i][1]],
                     colors[self.target[i][0]],
                     markersize=20)

        x_range = np.arange(-0.1, 1.1, h)
        y_range = np.arange(-0.1, 1.1, h)

        # creating a mesh to plot decision boundary
        xx, yy = np.meshgrid(x_range, y_range, indexing='ij')
        Z = np.array([[self.classify([x, y]) for x in x_range] for y in y_range])

        # using the contourf function to create the plot
        plt.contourf(xx, yy, Z, colors=['red', 'green', 'green', 'blue'], alpha=0.4)

    def train(self):
        for epoch in range(self.num_epochs):

            self.forward(self.train_data)
            self.update_weight()

            if epoch % 500 == 0:
                print("Loss: ", self.losses[epoch])

from itertools import cycle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

train_data = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]])

target_xor = np.array([
    [0],
    [1],
    [1],
    [0]])

target_or = np.array([
    [0],
    [1],
    [1],
    [1]])

target_nand = np.array([
    [1],
    [1],
    [1],
    [0]])

target_and = np.array([
    [0],
    [0],
    [0],
    [1]])

mlp = MLP(train_data, target_xor, 0.2, 8000)
mlp.train()

print(np.shape(mlp.b01))
print("Weight 01:")
print(mlp.weights_01)
print("Bias 01:")
print(mlp.b01)
print("Weight 12:")
print(mlp.weights_12)
print("Bias 12:")
print(mlp.b12)
print("Output:")
print(mlp.output_final)
mlp.classify([1,1])

_ = plt.plot(mlp.losses)

mlp.plot()
plt.show()