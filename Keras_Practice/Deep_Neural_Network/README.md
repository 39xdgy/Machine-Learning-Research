# Creating A Denser, Deeper Neural Network

![Deep Neural Network](http://neuralnetworksanddeeplearning.com/images/tikz41.png)

## Creating Our Own Deep Neural Networks in Keras

This time, we used Keras to train our own deep neural networks to identify different datasets that we chose. In this one, we didn't follow a tutorial, but instead used the knowledge that we gained while learning the basics to build one by ourself.

## Datasets

Keras provides various datasets that can be loaded for beginners to try their hand at creating a neural network. They can be loaded like such: 

```Python

from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
```
All of us used datasets from the [Keras's datasets](https://keras.io/datasets/) within the library.

## The Example Programs

* For STOzaki's program, he trained his deep neural network using the [IMDB Dataset](https://keras.io/datasets/#imdb-movie-reviews-sentiment-classification).

* For pdemange's program, he trained his deep neural network using the [MNIST Dataset](https://keras.io/datasets/#mnist-database-of-handwritten-digits)

* For 39xdgy's program, he trained his deep neural network also using the [MNIST Dataset](https://keras.io/datasets/#mnist-database-of-handwritten-digits)


