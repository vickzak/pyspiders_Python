# scope of variable
# 1.global scope
# 2.local scope
# 3.non local

# 1.global scope

# a=10
# def disp():
#     global a
#     a+=10
#     print(a)
#     def disp1():
#         global a
#         a+=10
#         print(a)
#     disp1()
# disp()


# 2.Local scope

# def disp():
#     global a
#     a=10
#     def disp1():
#         global a
#         a+=10
#         print(a)
#     disp1()
# disp()
# a+=10
# print(a)

# 3.non local
# def disp():
#     def disp1():
#         global a
#         a=10
#     disp1()
#     # a+=10
# disp()
# a+=10
# print(a)
