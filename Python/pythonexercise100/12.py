count=0
from math import sqrt
from sys import stdout
for i in range(101,201):
	k=int(sqrt(i+1))
	flag=0
	for j in range(2,k+1):
		if i%j ==0:
			flag=1
			break
	if flag==0:
		print(i)
		count+=1

print('The total is %d'%count)
