# a=int(input("enter a number"))
# b=str(a)
# r =lambda b: "palindrome" if b==b[::-1] else "not palindrome" 
# print(r(b))


# a=124
# res=0
# while a!=0:
#     r=a%10
#     res=res*10+r
#     a=a//10
# if res==a:
#     print("pal")
# else:
#     print("not pal")



# a=int(input("enter a number"))
# b=str(a)
# r =lambda b: "palindrome" if b==b[::-1] else "not palindrome" 
# print(r(b))


# wap to generate the output in the form of dict where 

# def new(*a):
#     for i in a:
#         yield i
# res=new('abrar','hafeez','adnan')
# # print(next(res))
# d={}
# for j in res:
#     d[j]=len(j)
# print(d)

# abstraction with inheritance

# from ABC  import abc,abstractmethod2
# @abstract
# class A(abc):
#     pass

# class B(A):
#     def __init__(self,name,place):
#         self.name=name
#         self.place=place
# b1=B('abrar','bangalore')
# print(b1.__dict__)


# operator overloading
# print prime number using filter
# a=
# r=lambda a: 


# pass list of strings odd length
# l=[]
# def str(*args):
#     for i in args:
#         if len(i)%2!=0:
#             l.append(i)
#     print(l)

# str("abrar",'aka','adnan','jspiders','pyspiders','a','b')


# using generator 
# def gen(*args):
#     for i in args:
#         yield i
# res=gen(1,22,33,33.0,1+5j,'abrar','aka',True,[1,2,3],(2,3,4),{'a':1,'b':2})
# l2=[]
# for j in res:
#     if isinstance(j,int):
#         l2.append(j)
# print(l2)


# zomato

class Zomato:
    def menu(self,*a):
        print("todays menu ")
        self.a=['idli','vada','masala dosa','anna sambhar','meals']
        print(self.a)
    def order(self,b):
        self.b=b
        d=len(self.a)
        for i in range(d):
            if self.b==i:
                print("your order",self.a[i])
                break
            else:
                print("wrong order")
    def delivery(self):
            print("thank you for your order and your otp is")
a1=Zomato()
a1.menu()
a1.order(1)
a1.delivery()


    


    
