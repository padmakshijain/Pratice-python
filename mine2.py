# def des(num):
#     if num <= 2:
#         print("Please enter numbers more than 2 to get the third largest number")
#     else:
#         # for i in range(num):
#         #     y = int(input())
#         #     arr.append(y)
#         # arr1 = arr
#         # print(arr1)
#         for i in range(len(arr)):
#             for j in range(i + 1, len(arr)):
#                 if arr[i] < arr[j]:
#                     # temp=0
#                     temp = arr[i]
#                     arr[i] = arr[j]
#                     arr[j] = temp
#     return arr[1]
#                     # arr_1 = arr[1]
#         # print("Second Largest number in arr", arr_1)
#
#
# arr = []
# n = int(input("Enter the number"))
# for i in range(n):
#     y = int(input())
#     arr.append(y)
# arr1 = arr
# print(arr1)
# print("Second largest number",des(n))
# value = des(n)
# # dict1={}
# # index = 0
# # for i in arr:
# #     dict1[i]=index
# #     index+=1
# # print(dict1)
# # for j,k in dict1.items():
# #     if j==value:
# #         print(k)
# for i in range(len(arr)):
#     if value == arr[i]:
#         print(i)


def des(num):
    if num <= 2:
        print("Please enter numbers more than 2 to get the third largest number")
    else:
        # for i in range(num):
        #     y = int(input())
        #     arr.append(y)
        # arr1 = arr
        # print(arr1)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    # temp=0
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
    return arr[1]
    # arr_1 = arr[1]
    # print("Second Largest number in arr", arr_1)


arr = []
n = int(input("Enter the number"))
for i in range(n):
    y = int(input())
    arr.append(y)
arr1 = arr
print(arr1)
dict1 = {}
index = 0
for i in arr:
    dict1[i] = index
    index += 1
print(dict1)

print("Second largest number", des(n))
value = des(n)
for j, k in dict1.items():
    if j == value:
        print(k)
