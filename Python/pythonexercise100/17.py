s=input('input a string:\n')
letters=[]
spaces=[]
digits=[]
others=[]
for i in iter(s):
	if i.isalpha()==True:
		letters.append(i)
	elif i.isspace()==True:
		spaces.append(i)
	elif i.isdigit()==True:
		digits.append(i)
	else:
		others.append(i)
print("char:%d,spaces:%d,digits:%d,others:%d"%(len(letters),len(spaces),len(digits),len(others)))

		
