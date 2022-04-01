list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
c=0
max=[]
while i<len(list):
    if list[i]>max:
        max=list[i]
        c=c+1
    i=i+1
j=0
min=[]
c2=0
while j<len(list):
    if list[j]>max:
        min=list[j]
        c2=c2+1
    j=j+1
print(len(max),max)
print(len(min),min)