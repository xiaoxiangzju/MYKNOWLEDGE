Tn=0
Sn=[]
n=(int)(input("n="))
a=(int)(input("a="))
for count in range(n):
	Tn=Tn*10;
	Tn=Tn+a;
	Sn.append(Tn)

print("sum of the total is %ld"%sum(Sn[:]))
