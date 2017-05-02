n=(int)(input("please input a integer"))
total=0
for i in range(1,int(n/2+1)):
	if n%i==0:
		total+=i
if total==n:
	print("it is a wanshu")
else:
	print("it is not a wanshu")
