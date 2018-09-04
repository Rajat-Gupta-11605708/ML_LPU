from numpy import *
from matplotlib.pyplot import *

def f(t):
    return exp(-t)*cos(2*pi*t)

t1 = arange(0.0,5.0,0.1)
t2 = arange(0.0,5.0,0.02)

figure(1)
subplot(212)
plot(t1,f(t1), 'bo', t2, f(t2), 'r')

subplot(211)
plot(t2, cos(2*pi*t2), 'g-')
show()

#play with bo, k and r--