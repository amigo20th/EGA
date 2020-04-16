import numpy as np

def ecuacion_prueba(x, y):
    ecua1 = (2*x) + (3*y)
    ecua2 = (-4*x) + (5*y)
    return([ecua1, ecua2])

def MSE(e1, e2):
    mse = (np.power(10 - e1, 2) + np.power(30 -  e2, 2))/2
    return mse

def fitness(x, y):
    print("x= ", x)
    print("y= ", y)