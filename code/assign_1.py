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