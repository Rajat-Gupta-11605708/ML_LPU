from math import *
from numpy import *
from matplotlib.pyplot import *

def linear(x):
    return x
def threshold(x):
    y=[]
    i=0
    while(i<len(x)):
        if x[i]<0:
            y.append(0)
        else:
            y.append(1)
        i+=1
    return y

def ramp(x):
    y=[]
    i=0
    while (i < len(x)):
        if x[i] < 0:
            y.append(0)
        elif x[i]>1:
            y.append(1)
        else:
            y.append(x[i])
        i += 1
    return y

def logsig(x):
    y=[]
    i=0
    while(i<len(x)):
        y.append(1/(1+exp(-x[i])))
        i+=1
    return y

x=linspace(-10,10,100)
y=threshold(x)
figure(1)
plot(x,y)
title("Linear Activation Function")
xlabel("x")
ylabel("y")
show()