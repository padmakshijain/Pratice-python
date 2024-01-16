# def long_string(s):
#     max_len = 0
#     long_string =""
#     for i in range(len(s)):
#         sub_s = ""
#         for j in range(i,len(s)):
#             if s[j] not in sub_s:
#                 sub_s +=s[j]
#                 sub_len =max_len
#                 max_len= max(max_len,len(sub_s))
#                 if max_len>sub_len:
#                     long_string = sub_s
#             else:
#                 break
#     print(f'The longest substring: {long_string}')
#
# long_string("ABDEFGABEF")

# def multi(y):
#     return y*3
#
# def func1(y, x):
#     return y + x(y)
#
#
# print(func1(1, multi))  # print 4
#
# print(func1(2, multi))  # print 8
#
# print(func1(3, multi))  # print 12

