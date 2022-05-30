import sympy as sy
import math
n=sy.Symbol("n")
lmda=sy.Symbol("lmda")
r=sy.Symbol("r")
n=5
def f(n,r):
	fu=1
	k=sy.Symbol("k")
	for i in range(1,n+1):
		fu=fu*(1+(n-k)/r)
	return fu
	

f=(lmda**n*(1-lmda/r)**r*f(n,r))/math.factorial(n)


lim=sy.limit(f,r,math.inf)
print(lim)

