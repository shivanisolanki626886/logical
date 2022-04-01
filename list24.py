a = [1, 2, 3, 1, 2, 2]
i=0
d=[]
while i<len(a):
	j=0
	c=0
	while j<len(a):
		if a[i]==a[i]:
			c=c+1
		j=j+1
	if a[i] not in d:
		d.append(a[i])
		print(a[i]),c
	i=i+1