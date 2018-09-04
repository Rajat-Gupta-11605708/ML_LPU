from math import *
from numpy import *
from matplotlib.pyplot import *

x = linspace(-10,10,100)#create 100 points betwnn -10 to 10
print(x)

y=x                         #linear
figure(1)
subplot(221)
plot(x,y)
title("Linear Activation Function")
xlabel('x')
ylabel('y')

#Threshold @ 0

subplot(222)
y=[]
i=0
while(i<len(x)):
    if(x[i]<0):
        y.append(0)
    else:
        y.append(1)
    i+=1

plot(x,y)
title("Threahold Function at 0")
xlabel('x')
ylabel('y')

#Ramp Function

subplot(223)
y=[]
i=0
while(i<len(x)):
    if x[i]<0:
        y.append(0)
    elif x[i]>1:
        y.append(1)
    else:
        y.append(x[i])
    i+=1
plot(x,y)
title('Ramp Function Threshold at 1')
xlabel('x')
ylabel('y')

#Log Sigmoid

subplot(224)
y=[]
i=0
while i<len(x):
    y.append(1/(1+exp(-x[i])))
    i+=1
plot(x,y)
title('Log Sigmoid Func.')
xlabel('x')
ylabel('y')
show()

