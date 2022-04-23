#Himanshu Kumar Gupta
#AI21BTECH11012

import numpy as np
import matplotlib.pyplot as plt

P=np.array([[3],[2]])
#we have equation 5*P=3*M+2*N
#so we let an variable vector/matrix x where x=np.array([[p],[q]]) where p,q are variables in question and we need to find p,q thats why I change it into a variable matrix
#so for getting expression 3*M+2*N  we have to multiply x with matrix A as stated below and then we equate it to 5*P and solve equation using python function np.linalg.solve to get matrix x i.e. value of p and q which we want

A=np.array([[3,0],[0,2]])

x=np.linalg.solve(A,5*P)

print('p=',x[0])
print('q=',x[1])
print('\n')
print('M=',np.array([x[0],[0]]))
print('N=',np.array([[0],x[1]]))

plt.grid()
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