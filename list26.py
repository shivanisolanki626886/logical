a=[4,5,5,5,3,8]
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    if c>=3:
        print(a[i])
        break
    i=i+1