import numpy as np


def linear_ecu(x, y):
    # The linear equation
    ecua1 = (-5.*x) + (16.*y)
    ecua2 = -x - (22.*y)
    return(ecua1, ecua2)

def MSE(e1, e2):
    mse = (np.power(-58. - e1, 2) + np.power(64. - e2, 2))/2.
    return (mse)

def fitness(x, y):
    x_f = bin2float(x)
    y_f = bin2float(y)
    ec1, ec2 = linear_ecu(x_f, y_f)
    return MSE(ec1, ec2)
def bin2float(str_bin):
    # This function turn a binary string into a float with 3 digits of significance
    bin = 0
    if (str_bin[0] == '1'):
        sig = 1
    else:
        sig = -1
    for i in range(1, len(str_bin)):
        tmp = int(str_bin[i:i+1])
        bin = bin * 2 + tmp
    return(sig* (bin/1000))