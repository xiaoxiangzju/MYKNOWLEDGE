i=int(input("净利润"))
bonus=0
if i<=10*10000:
	bonus=i*0.1
elif i>10*10000 and i<20*10000:
	bonus=10000*0.1+(i-10*10000)*0.075
elif i>=20*10000 and i<40*10000:
	bonus=10000+7500+(i-200000)*0.05
elif i>=40*10000 and i<60*10000:
	bonus=10000+7500+10000+(i-400000)*0.03
elif i>=60*10000 and i<100*10000:
	bonus=(i-60*10000)*0.015+10000+7500+10000
else:
	bonus=(i-100*10000)*0.01
print("bonus is %d",bonus)
