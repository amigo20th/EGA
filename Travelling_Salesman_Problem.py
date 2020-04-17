import numpy as np
import pandas as pd
from collections import Counter

np.random.seed(10)
#index = [str(x)+str(y)+str(z) for x in [0,1] for y in [0,1] for z in [0,1]]
#data = [(np.random.randint(0,100), np.random.randint(0,100)) for x in index]
#df = pd.DataFrame(data, index = index, columns=['x', 'y'])

def eucli_dins(p1, p2):
    return np.sqrt ((np.power(p1[0]-p2[0], 2)) + (np.power(p1[1]-p2[1], 2)))


def bit2Points(df, array_points):
    list_points = []
    for ind in array_points:
        list_points.append(df.loc[ind])
    return (np.array(list_points))

def punisher(list_points):
    pun = 0
    for ind in range(len(list_points)-1):
        if(list_points[ind] in list_points[ind+1:]):
            pun = 5000000000
    return pun
def fitness(arr_points):
    index = [str(x) + str(y) + str(z) for x in [0, 1] for y in [0, 1] for z in [0, 1]]
    data = [(np.random.randint(0, 100), np.random.randint(0, 100)) for x in index]
    df = pd.DataFrame(data, index=index, columns=['x', 'y'])
    list_points = [] #bit2Points(df, arr_points)
    for ind in arr_points:
        list_points.append(df.loc[ind])
    list_points = np.array(list_points)
    pun = punisher(list_points)
    list_dist = []
    for p in range(list_points.shape[0]-1):
        list_dist.append(eucli_dins(list_points[p], list_points[p+1]))
    return (sum(list_dist) + pun)




