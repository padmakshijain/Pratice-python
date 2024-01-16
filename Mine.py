# num =12345
# a = str(num)[::-1]
# print(a)

# num = 153
# sum = 0
# temp = num
# while temp > 0:
#     s = temp % 10
#     sum += s ** 3
#     temp //= 10
# if num == sum:
#     print("yes")
# else:
#     print("No")

# num = int(input("enter the number"))
# if num == 1:
#     print("not a prime")
# elif num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("not prime")
#             break
#         else:
#             print("prime")
# else:
#     print("not")

# a =7
# b = 2
# # a = a-b
# # b= a+b
# # a = b-a
# # print(a,b)
# temp =a
# a= b
# b = temp
# print(a,b)

#
# list_sum=[]
# def sum_num(num):
#     if num ==0:
#         return 0
#     return (num%10+ sum_num((int(num/10))))
# n = int(input("enter the number"))
# sum = sum_num(n)
# print(sum)

# num = 6
# l1 = [i for i in range(1,num+1)]
# print(l1)
# for i in range(1,len(l1)):
#     s = i**i
#     print(s)

# def remove_word(list_new, remove_word):
#     return [word for word in list_new if word not in remove_word]
#
#
# print(remove_word(["s", "t", "r", "i", "n", "g", "w"], "string"))
# print(remove_word(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
# print(remove_word(["d", "b", "t", "e", "a", "i"], "edabit"))
#
# string =input("Enter the string to refrese")
# new_string = [i for i in string[::-1] ]
# print("".join(new_string))
#
#
# n = input("Enter the stribg")
# numbers = ''
# for i in n:
#     if i.isdigit():
#         numbers= numbers+i
# print(numbers)


# user_input = input("Enter the date (DD-MM-YYYY): ")
# day, month, year = user_input.split('-')
# month_names = {
#
#     '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
#      '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug'
#     '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
#
# }
#
# formatted_date = f"{year} {month_names[month]} {day}"
#
# print("Formatted Date:", formatted_date)


# s = input("Enter the string")
# s1 = ''
# for i in s:
#     s1 = i+s1
# print(s1)


# def fact(n):
#     if n <=1:
#         return 1
#     else:
#         return (n*fact(n-1))
# num = int(input("Enter the number"))
# res = fact(num)
# print(res)


# def per(s,i=0):
#     if i == len(s):
#         print("".join(s))
#     for j in range(i,len(s)):
#         words = [c for c in s]
#         words[i],words[j]=words[j],words[i]
#         per(words,i+1)

# out=[]
#
# def permute(msg, i, length):
#     if i==length:
#         out.append("".join(msg))
#     else:
#         for j in range(i, length):
#             msg[i], msg[j] = msg[j], msg[i]
#             permute(msg, i+1, length)
#             msg[j], msg[i] = msg[i], msg[j]
#
# msg="abc"
# permute(list(msg), 0, len(msg))
# print(out)


# arr = []
# n = int(input("Enter the number"))
# if n <= 3:
#     print("Please enter numbers more than 3 to get the third largest number")
# else:
#     for i in range(n):
#         y = int(input())
#         arr.append(y)
#     print(arr)
#     temp = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]<arr[j]:
#                 temp=arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=temp
#     print(arr)
#     print("Third Largest number in arr", arr[2])


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
# # indexs = [index for index in range(len(arr)) if arr[index]==value]
# # print(indexs)
#
# for i in range(len(arr)):
#     if arr[i] == value:
#         s = arr.index(value)
# print(s)
#

# num = int(input("Enter the number"))
# res =[]
# for n in range(1,num):
#     for i in range(2,n):
#         if n%i==0:
#             break
#         else:
#             #print(n)
#             res.append(n)
#             break
#
# print(res)
# def reverse(a):
#     b = ""
#     for i in a:
#         b = i + b
#     return b
#
#
# s = input()
# print(reverse(s))


# n = int(input())
# for num in range(n):
#     sum = 0
#     temp = num
#     while temp > 0:
#         s = temp % 10
#         sum += s ** (len(str(num)))
#         temp //= 10
#     if num == sum:
#         print(f'{num} ýes')
#     else:
#         # print("No")
#         pass

# def arm(num):
#     n = int(input())
#     sum = 0
#     temp = num
#     while temp > 0:
#         s = temp % 10
#         sum += s ** (len(str(num)))
#         temp //= 10
#         if num == sum:
#             return num
#         else:
#                 # print("No")
#              pass

# Initialising string
ini_str = 'GeeksForGeeks'

# Printing Initial string
print("Initial String", ini_str)

# Splitting on UpperCase
res = ""
for i in ini_str:
    if (i.isupper()):
        res += "*" + i
    else:
        res += i
x = res.split("*")
x.remove('')
# Printing result
print("Resultant prefix", str(x))

