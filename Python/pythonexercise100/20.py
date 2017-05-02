sum=0
height=100
for i in range(1,11):
	if i==1:
		sum+=height
	else:
		sum+=2*height
	height=height/2
print("the sum of route is %lf"%sum)
