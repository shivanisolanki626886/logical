# a=[4,6,4,3,3,4,3,4,3,8]
# i=0
# b=[]
# k=4
# c=0
# while i<len(a):
#     c=a.count(a[i])
#     if c==k:
#         if a[i] not in b:
#             b.append(a[i])
#     i=i+1
# print("frequoncy",b)

a=[4,6,4,3,3,4,3,6,6]
i=0
b=[]
k=3
c=0
while i<len(a):
    c=a.count(a[i])
    if c==k:
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print("frequoncy",b)
