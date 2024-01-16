# # # Write a python program print output of below calculation
# # #
# # # Input a number :
# # #
# # # if number is 6 , output should be
# # #
# # # 6^6 + 5^5 - 4^4 + 3^3 - 2^2 + 1^1
# # #
# # # if number is 5, output should be
# # #
# # # 5^5 + 4^4 - 3^3 + 2^2 - 1^1
# #
# #
# # num = int(input("numbr"))
# # def calculate(n):
# #     evenlist=[]
# #     for i in range(1,n+1):
# #         if i % 2 == 0:
# #             r= list(pow(i,i))
# #             evenlist.append(r)
# #     print(evenlist)
# # # for i in range(int(a)):
# # #     l = int(input(" "))
# # #     num.append(l)
# #
# # calculate(num)
# #
#
# num = int(input('Number'))
# # num =6
# l1 = [i for i in range(1,num+1)]
# print(l1)
# #q1 = pow(l1[-1],l1[-1]) + pow(l1[num-2],l1[num-2]) + pow(l1[num-4],l1[num-4]) + 1
# #q2 =pow(l1[num-3],l1[num-3]) + pow(l1[num-5],l1[num-5])
# for i in range(len(l1),0,-1):
#
#     q1 = pow(l1[-1], l1[-1]) + pow(l1[i - 2], l1[i - 2]) + pow(l1[i - 4], l1[i - 4]) + 1
#     q2 = pow(l1[i - 3], l1[i - 3]) + pow(l1[i - 5], l1[i - 5])
#     q3 = q1 - q2
#     break
# # print(l1[num - 4])
# # print(l1[-1])
# # print(l1[num - 2])
# # print(q2)
# print(q3)
#



num = int(input("Enter he number"))
res ,qes =0,0
l1 = [i for i in range(1,num+1)]
l1.reverse()
print(l1)
s1 = pow(l1[0],l1[0])
for i in range (1,len(l1)):
    if num%2 ==0:
        if i % 2 ==0:
            res -= pow(i,i)
        else:
            qes +=pow(i,i)
    else:
        if i % 2 == 0:
            res += pow(i, i)
        else:
            qes -= pow(i, i)
print(res+qes+s1)