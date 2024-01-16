# def longest_substring(s):
#     maxlen = 1
#     if s == "":
#         return 0
#     else:
#         for i in range(len(s)):
#             substring = s[i]
#             for j in range(i+1,len(s)):
#                 if s[j] not in  substring:
#                     substring +=s[j]
#                     maxlen = max(maxlen,len(substring))
#         return maxlen
#
#
# print(longest_substring("pwwkew"))

# def des():
#     num = int(input())
#     arr = []
#     for i in range(num):
#         ele = int(input())
#         arr.append(ele)
#     print(arr)
#
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]>=arr[j]:
#                 temp = arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=temp
#     print(arr[2])
#
#     return arr
#
# des()


# def fact(n):
#     if n == 0:
#         return 0
#     elif n== 1:
#         return 1
#     else :
#         n = n* fact(n-1)
#         return n
#
# print(fact(6))


# def per(s,step =0):
#     #count = 0
#     if step == len(s):
#         print("".join(s))
#         #count+=1
#     for i in range(step,len(s)):
#         sc=[c for c in s]
#         sc[step],sc[i]=sc[i],sc[step]
#         per(sc,step+1)
#
# print(per('ABC'))


# def remove_word(list_new, remove_word):
#     return [word for word in list_new if word not in remove_word]
#
#
# print(remove_word(["s", "t", "r", "i", "n", "g", "w"], "string"))
# print(remove_word(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
# print(remove_word(["d", "b", "t", "e", "a", "i"], "edabit"))

# num = int(input("Enter he number"))
# res ,qes =0,0
# l1 = [i for i in range(1,num+1)]
# l1.reverse()
# print(l1)
# s1 = pow(l1[0],l1[0])
# for i in range (1,len(l1)):
#     if num%2 ==0:
#         if i % 2 ==0:
#             res -= pow(i,i)
#         else:
#             qes +=pow(i,i)
#     else:
#         if i % 2 == 0:
#             res += pow(i, i)
#         else:
#             qes -= pow(i, i)
# print(res+qes+s1)


# str = "aabbccddeffh"
# while str != " ":
#     str_len = len(str)
#     ch = str[0]
#     str = str.replace(ch, "")
#     str_len1 = len(str)
#     if str_len1 == str_len - 1:
#         print("string is", ch)
#         break

# n = int(input())
# for i in range(n,0):
#         print(i)


# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]
print(id(li1))

# using copy for shallow copy
li2 = copy.copy(li1)
print("li2 ID: ", id(li2), "Value: ", li2)
# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)