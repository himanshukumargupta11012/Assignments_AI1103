import numpy as np
import matplotlib.pyplot as plt

plt.plot(5,0,'o')
plt.annotate('M(5,0)',xy=(5,0),xytext=(5.1,0.2))

plt.plot(0,5,'o')
plt.annotate('N(0,5)',xy=(0,5),xytext=(0.1,5))

plt.plot(3,2,'o')
plt.annotate('P(3,2)',xy=(3,2),xytext=(3.1,2))

plt.annotate('3',[1.3,3.3])
plt.annotate('2',[3.8,.8])
plt.annotate(':',[2.8,1.8])
plt.annotate('45\N{DEGREE SIGN}',[4.3,0.1])

plt.plot([0,5],[5,0])


plt.ylim(0,6)
plt.xlim(0,6)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()