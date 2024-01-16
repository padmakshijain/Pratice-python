
num = int(input("Enter he number"))
res =0
qes=0
l1 = [i for i in range(1,num+1)]
l1.reverse()
print(l1)
#print(l1[0])
s1 = pow(l1[0],l1[0])
if num%2 ==0:
    for i in range (1,len(l1)):
        if i % 2 ==0:
            res -= pow(i,i)
           #print(i)
            # print(res)
    for i in range(1,len(l1)):
        if i % 2 != 0:
            qes +=pow(i,i)
            #rint(i)
else:
    for i in range(1, len(l1)):
        if i % 2 == 0:
            res += pow(i, i)
            #print(i)
            # print(res)
    for i in range(1, len(l1)):
        if i % 2 != 0:
            qes -= pow(i, i)
            #print(i)

print(res+qes+s1)