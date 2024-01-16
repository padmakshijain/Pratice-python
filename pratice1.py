# # Write a function to Return a string which has common letters between any 2 given strings s1 and s2.
# #
# # For example:
# #
# # s1= "I am writing this sample test"
# #
# # s2= "my python skills"
# #
# # output = “i mnthspl”
# #
# # Note: the output string order can be ignored
#
#
# # # s1 = input("Enter 1st string")
# # # s2 = input("Enter 2nd string")
# # s3 = ""
# # common_letter = list(set(s1) & set(s2))
# # print("The common letters are:")
# # for i in common_letter:
# #     # print(set(i))
# #     s3 = s3+i
# #
# # print(s3)
#
# s1 = "I am writing this sample test"
# s2 = "my python skills"
# s= ""
# a = list(s1)
# b = list(s2)
# for i in a:
#     for j in b:
#         if i == j:
#             s = s+i
# print(s)
#
# # s3 = ''
# # for i in set(s1):
# #     if i in s2:
# #         s3 += i
# # print(s3)
# # result = ""
# # if (len(s1) > len(s2)):
# #     for i in s1:
# #         if i in s2:
# #             result = result+i
# # else:
# #     for i in s2:
# #         if i in s1:
# #             result = result+i
# # print(result)
#
# def common(s1,s2):
#     s3 =""
#     for i in s1:
#         for j in s2:
#             if i ==j:
#                 s3 = s3+i
#     return s3
#
# common_word = common("I am writing this sample test","my python skills")
# print(common_word)




s1 = "I am writing this sample test"
s2 = "my python skills"
s3 = ''
for i in set(s1):
    if i in s2:
        s3 += i
print(s3)
# for i in list(s1):
#     for j in s2:
#         if i == j:
#             s3+=i
# print(s3)