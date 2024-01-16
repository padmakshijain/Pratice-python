


# python code for given a string s, find the first non-repeating character in it and return its index. if it does not exist, return -1 string s= aabbccddeffh
str = "aabbccddeffh"
while str != " ":
    str_len = len(str)
    ch = str[0]
    str = str.replace(ch, "")
    str_len1 = len(str)
    if str_len1 == str_len - 1:
        print("string is", ch)
        break
    # else:
    #     print(-1)

