# def large_num(n1,n2,n3):
#     if(n1 >= n2) and (n1>= n3):
#         large = n1
#     elif(n2 >= n1) and (n2>= n3):
#         large = n2
#     else:
#         large = n3
#     return large
# num1 = int(input("num1"))
# num2 =int(input("num2"))
# num3 = int(input("num3"))
#
# print("largest number",large_num(num1,num2,num3))


# def count_s():
#     s1 = input()
#     s2 = input()
#     count = 0
#     for i in s1:
#         if i == s2:
#             count += 1
#     return count
#
#
# print("count ", count_s())


# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95]
# print(arr)
# arr_1 = []
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             #print(arr[j])
#             arr_1.append(arr[j])
# print(arr_1)

# num1 = int(input("num1"))
# num2 = int(input("num2"))
# num3 = int(input("num3"))
#
#
# def sum_num():
#     sum = num1 + num2 + num3
#     if num1 == num2 == num3:
#         sum = sum*3
#     return sum
#
# print(sum_num())

num = int(input())
data = []
for i in range(0, num):
    ele = int(input())
    data.append(ele)
print(data)
num_1 = int(input("search"))


def find_num(data, n):
    for i in data:
        if i == n:
            return True
    return False
print(find_num(data, num_1))
