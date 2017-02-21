def Numberofwords(s):
 q=''
 x=s.split(' ')
 while q in x:
   for e in x:
       if e is q:
         x.remove(e)
 return(len(x))

print Numberofwords("This is an awsome wonderful day. I love livin life. These moments great. qwerty        coded        string!!!! ha ha ha .....")
