# a="bhavya is not related background" 
# i=0
# c=0
# b=""
# while i<len(a):
#     if a[i]==" ":
#         c+=1
#     i=i+1
# print("number of spaces",c)

# a=[[ 2,"bhavya",0.9],[3,6.0,"shivani"],["sholanki",10,0.5]]
# i=0
# il=[]
# sl=[]
# fl=[]
# bl=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if type(a[i][j])==int:
#             il.append(a[i][j])
#         elif type(a[i][j])==float:
#             fl.append(a[i][j])
#         elif type(a[i][j])==str:
#             sl.append(a[i][j])
#         j=j+1
#     i=i+1
# bl.append(il),bl.append(fl),bl.append(sl)
# print(bl)
    

# a=['puja','lina','ruchu','marina','liasa']
# i=0
# while i<len(a):
#     if i%2!=0:
#         print(a[i])
#     i+=1

# list=[1,2,3,8,9,10]
# i=0
# c=0
# while list[c:]:
#     c+=1
#     i+=1
# print(c)

# list=[[1,2,3],[4,5,6],[7,8,9,10]]
# i=0
# d=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         d.append(list[i][j])
#         j=j+1
#     i+=1
# print(d)


# list=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
# i=0
# d=[]
# ni=
# bl=[]
# while i<5:
#     ii=0
#     b=[]
#     while ii<len(n):
#         if n[i]+n[ii]==num:
#             b.append(n[i]),b.append(n[ii])
#             bl.append(b)
#         ii+=1
#     i+=1
# print(bl)

# list='navgurukul@gmail.com'
# a=input("enter symbole-: ")
# i=0
# c=0
# while i<len(list):
#     if a in list[i]:
#         c+=1
#     i=i+1
# if c>=1:
#     print("this is here")
# else:
#     print("this is not here")


# a=[1,2,3,4,5,6,7,8,10]
# b=len(a)
# c=a[0]
# a[0]=a[b-1]
# a[b-1]=c
# print("last after swapping",a)




# l=[1,2,3,4,5,6,7,8,9,10]
# l=int(input('num'))
# i=1
# d=[]
# while i<=l:
#     j=1
#     b=[]
#     while j<=i:
#         if l==1:
#             print(d)
#         elif i>1:
#             b.append(j)
#         j=j+1
#     d.append(b)
#     i=i+1
# if l>1:
#     print(d)

# a=[50,40,23,70,56,12,5,10,7]
# i=1
# #i=-1
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print("max number=",max)
# print("position of max number=",a.index(max))


# list= [12, 67, 98, 34]
# List1= [3, 13, 17, 7]


# a=[4, 5, 5, 5, 3,8]
# size=len(a)
# i=0
# while i<(size-2):
#     if a[i]==a[i+1] and a[i+1]==a[i+2]:
#         print(a[i])
#     i=i+1


# a=[4,5,5,5,3,8]
# i=0
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     if c>=3:
#         print(a[i])
#         break
#     i=i+1


# a=[1,1,1,64,23,64,22,22,22]
# size=len(a)
# i=0
# while i<(size-2):
#     if a[i]==a[i+1] and a[i+1]==a[i+2]:
#         print(a[i],",",end='')
#     i=i+1


list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)

