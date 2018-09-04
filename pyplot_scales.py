from numpy import *
from matplotlib.pyplot import *
from  matplotlib.ticker import NullFormatter

#fixing random state for reproductibility
random.seed(19690501)

#make up some data in interval ]0,1[

y = random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y>0) & (y<1)]
y.sort()
x = arange(len(y))

figure(1)

#linear
subplot(221) #(level,quadrant,no.of graph)
plot(x,y)
yscale('linear')
title('linear')
grid(True)

#log
subplot(222)
plot(x,y)
yscale('log')
title('log')
grid(True)

#symmetric log
subplot(223)
plot(x, y - y.mean())
yscale('symlog', linthreshy=0.01)
title('symlog')
grid(True)

#logit
subplot(224)
plot(x, y)
yscale('logit')
title('logit')
grid(True)

gca().yaxis.set_minor_formatter(NullFormatter())
subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
show()