# my_list = [1, 2, 3, 4, 2, 7, 8, 8, 3]

# for i in range(0,len(my_list)):
#     for j in range(i+1,len(my_list)):
#        if  my_list[i]==my_list[j]:
#            print(my_list[j])
# Write a python Program for input array ["100","101","100"] output ["100"]
# input = ["100", "101", "100"]
# res = int(input[0]) and int(input[1]) and int(input[2])
# # res_b = bin(res)
# # print(''.join(a))
# # print(f"[{res}]")
# print("['"+res+"']")
# input_array = [1,2,3,1,2]
# output = set()
# outPut_1 = set()
# for i in input_array:
#     if i in output:
#         outPut_1.add(i)
#     else:
#         output.add(i)
#
# output_arry = list(outPut_1)
# print(output_arry)
# l1 =[]
# for idx,i in enumerate(input_array):
#     input_array.remove(i)
#     # print(idx)
#     if i in input_array:
#         l1.append(i)
# print(l1)

# input_array = ["100","101","100"]
# for i in range(0,len(input_array)):
#     for j in range(i+1,len(input_array)):
#        if  input_array[i]==input_array[j]:
#            print(input_array[j])

# txt = "Hello, welcome to my world."
#
# print(txt.rfind("q"))
# print(txt.rindex("q"))


# reverse each word of string
# str = 'My Name is Jessa'
# print(str)
# def reverse(s):
#     str_1 =""
#     for i in s:
#         str_1 = i+str_1
#     print(str_1)
# reverse(str)



# Given an array arr[] of n elements, write a function to search a given element x in arr[] using Python.
# Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
# x = 110;
# Output : 6

# def search(arr,x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#               print(i)
#     return -1
#
# search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170],110)

#
# Given two lists a, b. Check if two lists have at least one element common in them.
# Input : a = [1, 2, 3, 4, 5]
#         b = [5, 6, 7, 8, 9]
# Output : True


def comman(a,b):
    res = False
    for i in a:
        for j in b:
            if i == j:
                res = True
    return res

c = [1, 2, 3, 4, 5]
d = [5, 6, 7, 8, 9]
print(comman(c,d))
