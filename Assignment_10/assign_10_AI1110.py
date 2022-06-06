import math
n=int(input("enter total no. of newborns:"))
m=int(input("enter no. of males:"))
z=float(input("enter z_u:"))

x=m/n
p1=x-z*math.sqrt(x*(1-x)/n)
p2=x+z*math.sqrt(x*(1-x)/n)

print(p1,"<p<",p2)