n=int(input("no. of prints:"))
m=int(input("no. of integers:"))
X=float(input("enter value of X:"))
lst=[]
print("enter no. of times m integers print one by one:")
for i in range(0,m):
	ele=int(input())
	lst.append(ele)
q=0	
for i in range(0,m):
	q=q+(lst[i]-n/m)**2/(n/m)
#l=0
#for i in range(0,m):
#	l=l+lst[i]*i/n
#t=0
#for i in range(0,m):
#	t=t+(i-l)**2*lst[i]/n

print("q:",q)
if(q>=X):
	print("not uniformly distributed")

