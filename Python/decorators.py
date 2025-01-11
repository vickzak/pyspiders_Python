# def deco(func): #func=add()
#     print("in deco")
#     def wrapper(*args,**kwargs):
#         print("addition operator")
#         # func(*args,**kwargs)
#         res=func(*args,**kwargs)
#         print(res)
#     return wrapper
# @deco #deco(add)
# def add(a,b):
#     # print(a+b)
#     return a+b
# add(10,20)

#  write a decorator function  which returns only integers from the given list
# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("filtering the list")
#         res=func(*args,**kwargs)
#         for i in res:
#             if isinstance(i,(int)):
#                 print(i)

#     return wrapper


# @deco
# def filter1(l):
#     return l
# filter1([10.15,5,23,'hi',(1,2,3)])

# write a decorator function  which recieves string from the main function returns dictionary of character and count pair
# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("dictionary with keys and value pairs")
#         res=func(*args,**kwargs)
#         r=lambda a:{ i:res.count(i) for i in res}
#         print(r(res))
#     return wrapper
      

# @deco
# def dict(a):
#     return a
# dict('abrararruui')


# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("dictionary with keys and value pairs")
#         res=func(*args,**kwargs)
#         d={}
#         for i in res:
#             d[i]=res.count(i)
#         print(d)
#     return wrapper
      

# @deco
# def dict(a):
#     return a
# dict('abrararruui')



# 1.	Create a decorator to log a message “welcome all”.

# def deco(func):
#     print("hello all")
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         print(res)
#     return wrapper
# @deco
# def add(a,b):
#     return a+b
# add(1,2)

# 
# 2.	Create a decorator to return only positive output for any subtraction.
# def deco(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         print(res)
#     return wrapper

# @deco
# def pos(a,b):
#     return abs(a-b)
# pos(1,-5)


# 3.	create a decorator that executes a function for 3 times
# def display(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             res = func(*args, **kwargs)
#             print(res)
#     return wrapper
# @display
# def sub1(a,b):
#     return a + b
# sub1(1,2)


# def display(func):
#     def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             print(res)
#             res = func(*args, **kwargs)
#             print(res)
#             res = func(*args, **kwargs)
#             print(res)
#     return wrapper
# @display
# def sub1(a,b):
#     return a + b
# sub1(1,2)


# 4.	create a decorator which counts the no. of function calls
# def display(func):
#     def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             print(res)
#     return wrapper
# @display
# def sub1(a,b):
#     return a + b
# sub1(1,2)


# ..............................multiple decorator................................

# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("recieved message from disp")
#         res=func(*args,**kwargs)
#         print(res)
        
#     return wrapper
# def deco1(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         for i in res:
#             if i in 'aeiou':
#                 print(i) 
#     return wrapper

# @deco
# @deco1
# def disp(msg):
#     return msg
# disp("hello all  how are you")



# .....................multiple main functions.................................
# def deco(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#     return wrapper

# @deco
# def add(a,b):
#     print(a+b)
# @deco
# def sub(a,b):
#     print(a-b)
# @deco
# def mul(a,b):
#     print(a*b)
# @deco
# def div(a,b):
#     print(a/b)


# add(30,6)
# sub(7,8)
# mul(9,8)
# div(8,9)
        



# def deco1(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         for i in res:
#             if i in 'aeiou':
#                 print(i) 
#     return wrapper

# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("recieved message from disp")
#         res=func(*args,**kwargs)
#         print(res)
        
#     return wrapper

# @deco
# @deco1
# def disp(msg):
#     return msg
# disp("hello all  how are you")









# ..........................parameterised decorator...............................

# simple
# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("in wrapper")
#         func(*args,**kwargs)
#     return wrapper


# @deco
# def add(a,b):
#     print(a+b)
# add(10,7)



# .........................parameterised decorator.......................................
# def paradeco(cons):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             print("in wrapper")
#             res=func(*args,**kwargs)
#             print(res,res*cons)
#         return wrapper
#     return deco

# @paradeco(30)
# def add(a,b):
#     return(a+b)
# add(10,7)



# 1.Create a decorator to log a message “welcome all”.
# def log(func):
#     def wrapper(*args,**kwargs):
#         print("welcome all")
#         res=func(*args,**kwargs)
#         print(res)
#     return wrapper
# @log
# def add(a,b):
#     return(a+b)
# add(2,4)


# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("my first")
#         res=func(*args,**kwargs)
#         for i in res:
#             if isinstance(i,(int,float)):
#                 print(i*5)
#     return wrapper

# @deco
# def add(a):
#     return a
# add([10,10.5,'hello',[1,2,3],(2,4,5,6,8),{'a':'abrar','b':20}])

# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("reading message from disp")
#         res=func(*args,**kwargs)
#         for i in res:
#             if i in 'aeiou':
#                 print(i)
        
#     return wrapper
# def deco1(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         print(res)
#     return wrapper
# @deco1
# @deco
# def disp(msg):
#     return msg
# disp("hello all how are you")
# def paradeco(para):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             res=func(*args,**kwargs)
#             for i in res:
#                 if i%2==0:
#                     print(i*para)
#                 else:
#                     print(i)
           
#         return wrapper
#     return deco

# @paradeco(20)

# def add(a):
#     return a
# add([20,30,55,66,70,999,500])

# def deco(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#     return wrapper

# @deco
# def add(a,b):
#     print(a+b)
# @deco
# def mul(a,b):
#     print(a*b)
# @deco
# def sub(a,b):
#     print(a-b )


# add(10,9)
# mul(5,6)
# sub(7,0)


# generators
# def func(a):
#     for i in a:
#         if i in 'aeiou':
#             yield i
# res=func('helloall')
# # print(list(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))


# decorator without arguments harry
# method 1 with @greet
# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("thanks for using it")
#     return mfx


# @greet
# def hello():
#     print('hello')
# hello()


# 2.method without greet and direct call
# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("thanks for using it")
#     return mfx


# # @greet
# def hello():
#     print('hello')
# greet(hello)()


# # with args

# def pro(fx):
#     def mfx(*args,**kwargs):
#         print("hello")
#         res=fx(*args,**kwargs)
#         print(res)
#         print('thanx')
#     return mfx
# # @pro
# def add(a,b):
#    return (a+b)
# pro(add)(2,5)



# multiple decorators with one main function
def deco(fx):
    def mfx(*args,**kwargs):
        print("in first decorator")
        res=fx(*args,**kwargs)
        print(res)
    return mfx
def deco2(fx):
    def mfx(*args,**kwargs):
        print("in second decorator")
        res=fx(*args,**kwargs)
        l=[]
        for i in res.split():
            if i[0] not in 'aeiou':
                l.append(i)
        print(l)
    return mfx


def str(a):
    return a
deco(str)('hey barbie hey max how are you')
deco2(str)('hey barbie hey max how are you')


# # single decorator with multiple main function
# def deco(fx):
#     def mfx(*args,**kwargs):
#         res=fx(*args,**kwargs)
#         # print(res)
#         if res%2==0:
#             print(res,"even")
#         else:
#             print(res,"odd")
#     return mfx
# def add(a,b):
#     return a+b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a%b

# deco(add)(2,3)
# deco(mul)(6,5)
# deco(div)(6,6)


# decorator with paradeco
# def paradeco(para):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             res=func(*args,**kwargs)
#             for i in res:
#                 if i%2==0:
#                     print(i*para)
#                 else:
#                     print(i)
           
#         return wrapper
#     return deco

# @paradeco(20)

# def add(a):
#     return a
# add([20,30,55,66,70,999,500])


# def paradeco(para):
#     def deco(fx):
#         def mfx(*args,**kwargs):
#             print("performing paradeco")
#             res=fx(*args,**kwargs)
#             l=[]
#             for i in res:
#                 if i>=2000:
#                     l.append(i*para)
#             print(l)
                    
#         return mfx
#     return deco


# @paradeco(20)
# def add(e):
#     return e
# add([2200,2000,1500,1000,3500,50000])