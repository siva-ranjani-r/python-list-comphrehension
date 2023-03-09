l1=[1,2,3,4,5,6,7,8,9,10]
l2=[11,12,13,14,15,16,17,18,19,20]
l3=[]
for i in range(len(l1)):
    if i%2!=0:
        l3.append(l1[i]+l2[i])
print(l3)

arr=[l1[i]+l2[i] for i in range(len(l1)) if i%2==0]
print(arr)
