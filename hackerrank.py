def flip(n):
   t = bin(n).split('b')[1]
   x=bytearray(t)
   l=len(x) 
   for i in range(l,32):
     x='0'+x
   #print x
   l=len(x)
   for i in range(0,l):
     if x[i] == 49:
       x[i] = 48
     else: 
       x[i] = 49
   #print x
   print int(str(x),2)

size = input()
list=[]
for i in range(0,size):
    list.append(input())
for e in list:
    flip(e)

flip(10)
