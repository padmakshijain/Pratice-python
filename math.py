# n = int(input("Enter the number"))
# sum = 0
#
# for i in range(n+1):
#
#     # num = int(input())
#     sum = sum + i
# print(sum)
#

# def sum_num():
#     sum = 0
#     num = int(input("Enter the number"))
#     for i in range(num + 1):
#         sum = sum + i
#     return sum
#
# print(sum_num())


def multiple(n):
    for i in range(n):
        if i % 3 ==0 and i % 5 ==0:
            print(i)

print(multiple(100))
