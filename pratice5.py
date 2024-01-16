# def common(s1, s2):
#     common_char = ""
#     for i in s1:
#         if i not in common_char:
#             i_in_s1 = s1.count(i)
#             i_in_s2 = s2.count(i)
#             comm_num = []
#             comm_num.append(i_in_s1)
#             comm_num.append(i_in_s2)
#             comm_i = min(comm_num)
#             new_char = i * comm_i
#             common_char += new_char
#
#     return common_char
#
#
# common_word = common("my python skills", "I am writing this sample test")
# print(common_word)


s1 = "I am writing this sample test"
s2 = "my python skills"
#s = ""
s = list((lambda x: x in set(s1), set(s2)))
# for i in s:
#     print(i)
print(s)