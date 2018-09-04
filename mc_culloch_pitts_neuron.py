from numpy import *
#from matplotlib.pyplot import *

def threshold(x):
    if x>0:
        return 1
    else:
        return 0

x=[]
neti=0
w=[]
n = int(input("Size of the Inputs : "))
for i in range (n):
    x.append(float(input("Enter Inputs : ")))
    w.append(float(input("Enter Weight : ")))
    neti+=x[i]*w[i]

b = float(input("Enter value of Bias : "))
neti+=b
out=threshold(neti)
print("Output for Mc Culloch Pitt Neuron : ",out)
