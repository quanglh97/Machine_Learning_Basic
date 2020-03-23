import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
datafame = pd.read_csv('../Data//data_classification.csv', header=None)
true_x = []
true_y = []
false_x = []
false_y = []
for item in datafame.values:
    if item[2] == 1. :
        true_x.append(item[0])
        true_y.append(item[1])
    else:
        false_x.append(item[0])
        false_y.append(item[1])
# plt.scatter(true_x, true_y, marker='o', c='b')
# plt.scatter(false_x, false_y, marker='s', c='r')
#plt.show()

def sigmoid(z):
    return 1./(1 + np.exp(-z))

def phanchia(p):
    if p >= 0.5:
        return 1
    else:
        return 0

def predict(features, weights):
    z = np.dot(features, weights)
    return sigmoid(z)

def cost_fuction(features, labels, weights):
    '''

    :param features: 100x3
    :param labels: 100x1
    :param weights: 3x1
    :return: chi phi cost
    '''
    n = len(labels)
    predictions = predict(features, weights)

    cost_class1 = -labels*np.log(predictions)
    cost_class2 = -(1-labels)*np.log(1-predictions)
    cost = cost_class1 + cost_class2
    return cost.sum()/n
def update_weight(features, labels, weights, learning_rate):
    '''

    :param features: 100x3
    :param labels: 100x1
    :param weights: 3x1
    :param learning_rate:float
    :return: new weight float
    '''

    n = len(labels)
    predictions = predict(features, weights)
    gd = np.dot(features.T, predictions - labels)
    gd = (gd/n)*learning_rate
    weights = weights - gd
    return weights

def training(features, labels, weights, learning_rate, iter):
    cost_hs = []
    for i in range(iter):
        weights = update_weight(features, labels, weights, learning_rate)
        cost = cost_fuction(features, labels, weights)
        cost_hs.append(cost)
    return weights, cost_hs

features = datafame.values
labels = np.dot(features, np.array([[0], [0], [1]]))

for i in range(len(features)):
    features[i, 2] = 1

weights = [[0.1], [0.1], [0.1]]

weights, cost = training(features, labels, weights, 0.1, 100000)
print('after training: ')
print(weights)

solanlap = [i for i in range(100000)]
plt.plot(solanlap, cost)
plt.show()

a = phanchia(predict([[1.8591124145314097,5.6918675592169166,1]], weights))
print('ket qua:')
print(a)