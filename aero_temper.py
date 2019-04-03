with open('temp.txt','r') as file:
     l = list(map(float, file))
print(max(l))
print(min(l))
k=0
for w in l :
     k+=w
print(k/len(l))
p=0
for i in l:
     k = l.count(i)
     if k==1 :
          p=p+1
print(p)
