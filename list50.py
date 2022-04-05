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
#             b.append(i)
#         elif j>=1:
#             b.append(j)
#         j=j+1
#     d.append(b)
#     i=i+1
# if l>=1:
#     print(d)

# a=[50,40,23,70,56,12,5,10,7]
# i=1
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print("max number=",max)
# print("position of max number=",a.index(max))


# list= [12, 67, 98, 34]
# List1= [3, 13, 17, 7]


# # a=[4, 5, 5, 5, 3,8]
# # size=len(a)
# # i=0
# # while i<(size-2):
# #     if a[i]==a[i+1] and a[i+1]==a[i+2]:
# #         print(a[i])
# #     i=i+1


# a=[4,5,5,5,3,8,8,8]
# i=0
# c=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     if c>=3:
#         # print(a[i])
#         b.append(a[i])
#         # break
#     i=i+1
# print(b)


# a=[1,1,1,64,23,64,22,22,22]
# size=len(a)
# i=0
# while i<(size-2):
#     if a[i]==a[i+1] and a[i+1]==a[i+2]:
#         print(a[i],",",end='')
#     i=i+1


# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
    # list1.remove(20)
# print(list1)

    
mark=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(mark):
	j=0
	s=0
	sum=0
	while j<len(mark):
		sum=sum+mark[i][j]
		s=s+mark[i][j]
		j=j+1
	i=i+1
print("row ",sum)
print("cloums",s)

    
# mark=[[5,3,7],[1,8,9],[6,4,2]]
# i=0
# while i<len(mark):
# 	j=0
# 	s=0
# 	sum=0
# 	while j<len(mark):
# 		sum=sum+mark[i][j]
# 		s=s+mark[i][j]
# 		j=j+1
# 	i=i+1
# print('magic square',s)
# print("not magic squar",sum)

# print('Aapka Sawaal hai')
# print('What is the capital of india?')
# a=['chandigarh','Bhopal','Chennai','Delhi']
# i=0
# while i<len(a):
#      print(i+1,a[i])
#      i=i+1
# n=int(input('select your answer'))
# j=0
# c=4
# b=[1,2,3,4]
# while j<len(b):
#      if n==c:
#          print('Congrats! Aapka answer sahi hai')
#          break
#      if n not in b:
#          print('Exit')
#          break
#      else:
#          print('Sadly salla javab galathai')
#          break
#      j=j+1


#p=int(input('you have one more chance'))
#d=['bhopal','delhi']
#k=0
#while k<len(d):
     #print(k+1,d[k])
     #k=k+1
#r=int(input('select your answer'))
#l=0
#m=2
#s=[1,2]
#while l<len(s):
    # if r==m:
         # print('your answer is correct')
          #break
     #if r not in s:
          #print('exit')
          #break
     #else:
         # print('your answer is worng')
     #l=l+1


# a="shivani"
# b="madhu"
# i=0
# while i<5:
#     print(a[5]+b[4],end='')
#     i=i+1