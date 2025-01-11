# functions
# 1.built in
# 2.user defined



# arguments
# 1.positional args
# 2.keywords arguments


# heirarachy
# 1.postional args
# 2.default positional args
# 3.kw args

# 1.positinal arguments
# .positional only
# .combination pf positional and keyword args
# .default positional arguments
# .varibale length

# 1.positinal arguments

# def add(a,b,c,d):
#     return a+b+c+d
# print(add(10,20,30,40))

# 1.a positional only
# def add(a,b,c,d,/):
#     return a+b+c+d
# print(add(10,20,30,40))

# 1.b combination of positional and keywords arguments
# def add(a,b,/,*,c,d):
#     return a+b+c+d
# print(add(10,20,c=30,d=40))

# 1.c default positional arguments
# def add(a,b=0,/,*,c=0,d,):
#     return a+b+c+d
# print(add(10,20,c=30,d=40))

# 1.d vraiable length args
# def add(*args):
#     for i in args:
#         print(i)
# add(10,2.3,True,[1,2,3])

# or

# def add(*a):
#     for i in a:
#         print(i)
# add(10,2.3,True,[1,2,3])






# keywords arguments

# 1.a keywords only

# def add(*,a,b,c,d):
#     return a+b+c+d
# print(add(b=5,c=10,a=20,d=15))


# 1.b combiantion of pos and kwargs

# def add(a,b,/,*,c,d):
#     return a+b+c+d
# print(add(10,20,c=30,d=40))


# 1.c default kwargs

# def add(*,a=0,b,c=0,d):
#     return a+b+c+d
# print(add(a=10,b=5,c=20,d=15))

# Note :here it does not follow any heirarchy as default positinal args follows


# 1.d varibale length kwargs

# def disp(**a):
#     # print(**args) # disctionary cannot be unpacked
#     print(a)
# disp(a=1,b=20,c=30,d=40)






# waf to check a number is even or not

# def even(a):
#     if a%2==0:
#         print(f"{a} is even")
#     else:
#         print(f"{a} is  not even")
# even(18)

# waf to check a number is odd or not

# def even(a):
#     if a%2!=0:
#         print(f"{a} is odd")
#     else:
#         print(f"{a} is  not odd")
# even(19)


# # waf which checks datatype of objects and returns object with its type
# def datatype(d):
#     if isinstance(d,(int,float,bool,complex,list,tuple,str,set,dict)):
#         print(d,type(d))

# datatype(5.66)


# waf which takes two inputs and perform all arithamatic operations and return a dictionary ---->{'sum':o/p of sum,'sub':o/p of sub......}
# a=int(input("Enter first  number: "))
# b=int(input("Enter second number :"))
# add=a+b
# sub=a-b
# mul=a*b
# div=a/b
# mod=a%b 
# dm=divmod(a,b)   
# def op(**a):
#         print(a)

# op(sum=add ,sub=sub,mul=mul,div=div,mod=mod,divmod=dm)

# waf to check  the given string is anagram or not


# def isanagram(w1,w2):
#     l1=list(w1)
#     l2=list(w2)
#     l1.sort()
#     l2.sort()
#     if l1==l2:
#         return True
#     else:
#         return False
# print(isanagram('listen','silent'))

# def anangram(a,b):
#     if 



# waf to check the given string is starting with vowel 

# def vowel(a):
#         if a[0] in 'aeiouAEIOU':
#             print("starting with vowel")
#         else:
#             print("not starting with vowel")
# vowel('hafeez')
# vowel('abrar')

# waf to check the given string is starting with consonant

# def cons(a):
#         if a[0]  not in 'aeiouAEIOU':
#             print("starting with consonant")
#         else:
#             print("not starting with consonant")
# cons('hafeez')
# cons('abrar')

 
# waf to check the given string is starting with digit 

# def digit(a):
#         if a[0] in '0123456789':
#             print("starts with numbers")
#         else:
#             print("not starts with numbers")
# digit('1hafeez')
# digit('5abrar')


# waf to check the given string is starting with special character 


# def sc(a):
#         if a[0] in '!@#$%^&*()+~':
#             print("starts with special character")
#         else:
#             print("not starts with special character")
# sc('%hafeez')
# sc('&abrar')

# # waf which checks given iterable is even length or odd length
# def iter(l):
#     if len(l)%2==0:
#         print("Even length")
#     else:
#         print("Not even length")   
    
# iter({'a':1,'b':20})

# l=[1,2,3,45,5]
# print(len(l))