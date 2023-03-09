alph=list("abcdefghijklmnopqrstuvwxyz")
l1=[]
for i in range(len(alph)):
    if i%2==0:
        l1.append(alph[i])
print(l1)

l2=[alph[i] for i in range(len(alph)) if i%2==0]
print(l2)