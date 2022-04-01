# list=[[10,20],[30,40],[50,60],[30,20,80]]
# list1=[[61],[12,14,15],[12,13,19,20],[12]]
# i=0
# a=[]
# while i<len(list):
#     a.append(list[i]+list1[i])
#     i+=1
# print(a)

# list=[['a','b'],['b','c','d'],['e','f']]
# list1=[['p','q'],['p','s','t'],['u','v','w']]
# i=0
# d=[]
# while i<len(list):
#     d.append(list[i]+list1[i])
#     i=i+1
# print(d)

n=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
end=15
i=0
bl=[]
while i<5:
    ii=0
    b=[]
    while ii<len(n):
        if n[i]+n[ii]==end:
            b.append(n[i]),b.append(n[ii])
            bl.append(b)
        ii+=1
    i+=1
print(bl)