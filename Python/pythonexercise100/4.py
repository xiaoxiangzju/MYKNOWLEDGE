year=int(input('year:\n'))
mouth=int(input('mouth:\n'))
day=int(input('day:\n'))
months1=[0,31,59,90,120,151,181,212,243,273,304,334]
months2=[0,31,60,91,121,152,182,213,244,274,305,335]
if (year%400==0) or ((year%4==0) and (year %100 !=0)):
	sum=months2[mouth-1]+day
else:
	sum=months1[mouth-1]+day
print('it is the %dth day.' %sum)
