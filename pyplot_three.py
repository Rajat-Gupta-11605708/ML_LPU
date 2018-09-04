from numpy import *
from matplotlib.pyplot import *

t = arange(0, 5, 0.2)
ylim(0, 10)
plot(t, t, 'r--', t, t**2, 'bo', t, t**4, 'g^')
show()