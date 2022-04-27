import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Symbol,limit

x = Symbol('x')
y=(8**x-4**x)/(4*x)

limit(y,x,0)
print(limit(y,x,0))
