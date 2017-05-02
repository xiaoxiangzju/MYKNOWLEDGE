d=[]
count=0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j and j!=k and i!=k):
				print(i,j,k)
				d.append((i,j,k))
				count+=1
				
print(len(d))
print(count)
list_num=[1,2,3,4]
list=[i*100 +j*10 +k for i in list_num for j in list_num for k in list_num if i!=j and j!=k and i!=k]
print(list)


