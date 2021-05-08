from operator import itemgetter

l=[[1,3],[2,8],[2,5],[3,7],[4,8],[4,6],[6,12],[7,10]]
l.sort(key=itemgetter(1),reverse=False)
latest_finishing_time=l[0][1]
a=[l[0]]
for i in range(1,len(l)):
	if(l[i][0]>=latest_finishing_time):
		a.append(l[i])
		latest_finishing_time=l[i][1]

print(a)

