from numpy import *
from matplotlib.pyplot import *

x = subplot(111)

t = arange(0.0,5.0,0.01)
s = cos(2*pi*t)
line, = plot(t,s, lw=2)         #tuple and lw is width of graph

annotate('Local Maxima', xy=(2,1), xytext=(3,1.5), arrowprops=dict(facecolor='black',shrink=0.05))

ylim(-2,2)
show()