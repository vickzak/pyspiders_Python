# a=int(input("enter"))
# b=input("enter")
# print(a+b)


# specific
# try:
#     a=int(input("enter"))
#     b=input("enter")
#     print(a+b)
# except TypeError:
#     print("you cannot add string and int")

# generic
# try:
#     a=int(input("enter"))
#     b=int(input("enter"))
#     print(a/b)
# except Exception:
#     print("you cannot add string and int")

# default
# try:
#     i=1
#     while i>0:
#         print(i)
#         i+=1
# except:
#     print("stopiterationerror handled successfully")



# .........................................errro creation
# coustom error
# x=int(input("enter "))
# if x%2==0:
#     print(x**2)
# else:
#     raise ValueError('not even')

#..................................... userdefined error
# class manju(Exception):
#     pass
# a=input("enter")
# if len(a)%2==0:
#     print("even")
# else:
#     raise manju("not even")

# ......................assertion error
a=input("enter")
assert a==a[::-1],'not a pal'
print('pal')




