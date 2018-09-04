from math import *

def linear(x):
    return x

def threshold(x):
    if x>0:
        return 1
    else:
        return 0

def ramp(x):
    if x>1:
        return 1
    elif x<0:
        return 0
    else:
        return x

def logsig(x):
    return (1/(1+exp(-x)))

x=[]
w=[]
neti=0

n=int(input("Enter Size of Inputs : "))
for i in range(n):
    x.append(float(input('Enter Input : ')))
    w.append(float(input('Enter Weight: ')))
    neti+=x[i]*w[i]

b = float(input('Enter Value of Bias : '))
neti+=b
print(neti)
while(True):
    ch=int(input('Enter neuron 1>Linear 2>Threshold 3>Ramp 4>Log Sigmoid'))
    if(ch==1):
        out=linear(neti)
    elif ch==2:
        out=threshold(neti)
    elif ch==3:
        out=ramp(neti)
    elif ch==4:
        out=logsig(neti)
    else:
        break
    print(out)

