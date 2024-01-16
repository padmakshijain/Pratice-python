# import os
# path = input()
# res = os.path.exists(path)
# print(res)


# file_1 = open("my_Files.txt", "a")
# l = ["HIIi \n","Me padmakshi"]
# file_1.writelines(l)
# file_1.write("Hellooo")
# # file_1.close()
# file_1 = open("my_Files.txt", "r+")
# file_1.seek(0)
# print(file_1.read())
# file_1.close()

l, u, p, d = 0, 0, 0, 0
s = "1LoveMyIndia123"
if (len(s) >= 8):
    for i in s:

        # counting lowercase alphabets
        if (i.islower()):
            l += 1

        # counting uppercase alphabets
        if (i.isupper()):
            u += 1

        # counting digits
        if (i.isdigit()):
            d += 1

        # counting the mentioned special characters
        if (i == '@' or i == '$' or i == '_'):
            p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
    print("Valid Password")
else:
    print("Invalid Password")

# data = [1,2,3,4]
# res = lambda x,data:x*2,data
# print(res)
#
# result1 = list(map(lambda x: x * 2, data))
# print(result1)
#
# result2 = list(filter(lambda x:x%2==0,data))
# print(result2)

# s = input()
# s1 = input()
# count =0
# for i in s:
#     if i == s1:
#         count+=1
#
# print(count)

# def reverse(s):
#     s1 =""
#     for i in s:
#         s1= i+s1
#     return s1
#
# print(reverse('padmakshi'))

#
# def reverse(s):
#     r = 0
#     while s != 0:
#         digit = s % 10
#         r = r * 10 + digit
#         s //= 10
#     return r
# print(reverse(987654321))


# string = "This is a string."
# string_list = string.split(' ') #delimiter is ‘space’ character or ‘ ‘
# print(string_list) #output: ['This', 'is', 'a', 'string.']
# print('+ '.join(string_list)) #output: This is a string
