# import atexit
#
# @atexit.register
# def goodbye():
#     print('You are now leaving the Python sector.')


# import atexit
#
#
# def func_1(args):
#     print("Executing func_1 with argument - %s" % (args,))
#
#
# def func_2():
#     print("Executing func_2 with no arguments")
#
#
# def func_3(arg1, arg2):
#     print("Executing func_3 with arg1 - %s, arg2 - %s" % (arg1, arg2))
#
#
# print("Hello Educative")
#
# atexit.register(func_1, [1, 2, 3])
# atexit.register(func_2)
# atexit.register(func_3, arg1="hello", arg2="educative")


import atexit


@atexit.register
def func_1():
    print("Executing func_1 with argument - %s" % (args,))


# @atexit.register()
# def func_2():
#     print("Executing func_2 with no arguments")
#
# @atexit.register()
# def func_3(arg1, arg2):
#     print("Executing func_3 with arg1 - %s, arg2 - %s" % (arg1, arg2))


print("Hello Educative")

# atexit.register(func_1, [1, 2, 3])
# atexit.register(func_2)
# atexit.register(func_3, arg1="hello", arg2="educative")
