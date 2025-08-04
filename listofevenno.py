list=[]
n=int(input("enter the no of values"))
print("enter the values")
for i in range(n):
    a=int(input())
    list.append(a)
print("the original list",list)
newlist=[]
for a in list:
   if(a%2==0):
       newlist.append(a)
print("new list containing even no",newlist)
