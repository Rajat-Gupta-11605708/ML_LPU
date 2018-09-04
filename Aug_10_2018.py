import numpy as np

#sigmoid function ( maps data b/w 0 to 1 ) is a nonlinear func.
def nonlin(x, deriv=False):
    if(deriv == True):
        return (x*(1-x))
    return 1/(1+np.exp(-x))


# input dataset

x = np.array([ [0,0,1],
               [0,1,1],
               [1,0,1],
               [1,1,1] ])

#output dataset
y = np.array([[0,0,1,1]]).T

#seed random numbers to make calculations
#deterministic (just a good practice)

np.random.seed(1)

#init weights randomly with mean 0

syn0 = 2*np.random.random((3,1)) - 1

for iter in range(100000):
    #forward propogation
    l0 = x
    l1 = nonlin(np.dot(l0,syn0))

    #how did we missed
    l1_error = y-l1

    #multiply how much we missed by the slope op the sigmod at values in l1
    l1_delta = l1_error*nonlin(l1,True)

    #update weights
    syn0 += np.dot(l0.T, l1_delta)

print("Output after Training")
print(l1)