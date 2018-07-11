import numpy as np
import matplotlib.pyplot as plt


def function_example(n):
    # define whatever function you want
    n = n * 2
def visualize_function(function):
    """function -> None
    function visualizes on inputs 1 to 1000. Make sure you have numpy and matplot"""
    x, y = [], []
    for i in range(1000):
        x.append(function(i)[0])
        y.append(function(i)[1])
    plt.scatter(x, y)
    plt.show()

if __name__ == '__main__':
	visualize_function(function_example)
