# swap 2 numbers without third varibale
# a=5
# b=7
# a=a+b
# b=a-b
# a=a-b
# print('a',a)
# print('b',b)

# swap 2 numbers with 3rd variable
# a=9
# b=8
# c=a
# a=b
# b=c
# print('a',a)
# print('b',b)

# sum of given range
# sum=0
# for i in range(12):
#     sum+=i
# print(sum)

# factorial of given number
# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#     fact*=i
# print(fact)

# # factorial of given using recursseion
# def fact(a):
#     if a==0 or a==1:
#         return 1
#     else :
#         return a*fact(a-1)
# print(fact(7))

# fibonaaci series

# a=int(input("enter a number"))
# num1=0
# num2=1
# next=num1+num2
# count=0
# while count<=a:
#     print(next,end=',')
#     count+=1
#     num1,num2=num2,next
#     next=num1+num2

# or

# a=int(input("enter a number"))
# n0=0
# n1=1
# for i in range(a):
#     n2=n0+n1
#     n0=n1
#     n1=n2
    # print(n2)


# fibonacci using recurssion
# def fib(a):
#     if a==0:
#         return 0
#     elif a==1 or a==2:
#         return 1
#     else:
#         return fib(a-1)+fib(a-2)
# print(fib(10))

# to check the given number is prime or not
# a=int(input("enter a number"))
# for i in range(2,a):
#     if a%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

# to print in a range
# a=int(input("enter a number"))
# for i in range(1,a):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# to reverse a given number
# a=12345
# res=0
# while a!=0:
#     rem=a%10
#     res=res*10+rem
#     a=a//10
# print(res)


# given number is palindrome or not
# a=12345
# res=0
# while a!=0:
#     rem=a%10
#     res=res*10+rem
#     a=a//10
# if res==a:
#     print("pal")
# else:
#     print("not pal")

# strong number
# a=145
# t=a
# sum=0
# while a!=0:
#     rem=a%10
#     fact=1
#     for i in range(1,rem+1):
#         fact=fact*i
#     sum=sum+fact
#     a=a//10
# if sum==t:
#     print('strong')
# else:
#     print("not strong")



# amstrong number
# a=153
# b=len(str(a))
# s=0
# t=a
# while a!=0:
#     r=a%10
#     s=s+r**b
#     a=a//10
# if s==t:
#     print(t,s,"amstrong")
# else:
#     print(t,s,"not amstrong")


# amstrong in given range
# a=int(input("enter first"))
# b=int(input("enter first"))
# for i in range(a,b+1):
#     c=len(str(i))
#     t=i
#     s=0
#     while i!=0:
#         r=i%10
#         s=s+r**c
#         i=i//10
#     if s==t:
#         print(s,"amstrong")
  

# perfect numbers
# a=int(input("enter a number"))
# s=0
# for i in range(1,a):
#     if a%i==0:
#         s=s+i
# if s==a:
#     print("perfect number")
# else:
#     print("not a perfect number")

# happy number
# a=int(input("enter a number"))
# while a!=1 and a!=4:
#     s=0
#     while a!=0:
#         r=a%10
#         s=s+r**2 #82
#         a=a//10
#     a=s
# if a==1:
#     print("happy")
# else:
#     print("not happy")

# perfect square
# a=int(input("enter a number"))
# for i in range(a):
#     if i*i==a:
#         print("perfect square")


# neon number
# a=int(input("enter a number"))
# b=a**2
# s=0
# while b!=0:
#     rem=b%10
#     s=s+rem
#     b=b//10
# if s==a:
#     print("neon number")
# else:
#     print("non neon")

# # sunny number
# a=int(input("enter a number"))
# b=a+1
# for i in range(b):
#     if i*i==b:
#         print(a,'sunny number')

# l=[4,5,7,6,4,66,4,5334,23,11,23,60]
# for i in range(1,len(l)):
#     for j in range(1,len(l)):
#         if l[i]<l[j-1]:
#             l[i],l[j-1]=l[j-1],l[i]
# print(l)

# two sum
# l=[5,4,3,2,1]
# n=7
# d={}
# for i,j in enumerate(l):
#     diff=n-j
#     if diff in d:
#         print(l[d[diff]],l[i])
#     else:
#         d[j]=i #5:0,3:1,4:2,
# # print(d)
        
# patterns

# for i in range(5):
#     for j in range(5):
#         if i==j:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
    
# for i in range(6):
#     for j in range(6):
#         if i>j:
#             print(5-j,end='')
#         else:
#             print(' ',end='')
#     print()


# for i in range(6):
#     for j in range(6):
#         if i>j:
#             print(chr(j+97),end='')
#         else:
#             print(' ',end='')
#     print()



# for i in range(6):
#     for j in range(6):
#         if i>j:
#             print(chr(j+65),end='')
#         else:
#             print(' ',end='')
#     print()

# for i in range(6):
#     for j in range(6):
#         if i<j:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# n=7
# for i in range(n):
#     for j in range(n):
#         if i+j==n+1:
#             print('*',end='')
#         else:
#             print('  ',end='')
#     print()

# n=6
# for i in range(n+1):
#     for j in range(n+1):
#         if i+j>n+1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j<n+1:
#             print(j,end='')
#         else:
#             print(' ',end='')
#     print()

# triangle seedha
# n=6
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(1,2*i):
#         print("*",end='')
#     print()


# ulta traingle
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(2*i-1):
#         print("*",end='')
#     print()

# diamond cut 

# n=6
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(1,2*i):
#         print("*",end='')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(2*i-1):
#         print("*",end='')
#     print()


# n=6
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(1,2*i):
#         if k%2==0:
#             print(' ',end='')
#         print(k,end=' ') 
#     print()

# import math
# a=math.trunc(4.67)
# print(a)

# def add(a,b,/):
#     return a+b
# print(add(10,30))

# def add(a,b,/,*,c,d):
#     return a+b+c+d
# print(add(10,30,c=44,d=55))

# def add(a,b=20,/):
#     return a+b
# print(add(10,30))


# def add(*args):
#     l=[]
#     for i in args:
#         l.append(i)
#     print(l)
# add(1,2,34,'hello',1+3j)



# def add(*,a,b):
#     return a+b
# print(add(a=33,b=1))

# def add(c,d,/,*,a,b):
#     return a+b+c+d
# print(add(11,44,a=33,b=1))


# def add(*,a,b=10):
#     return a+b
# print(add(a=33,b=1))

# def add(**kwargs):
#     # for i in kwargs:
#         # print(i)
#         # print(**kwargs)
#         # print(kwargs)
   
# add(a=33,b=1,c='bye')


# a='abbcbaa'
# d={}
# for i in a:
#     d[i]=a.count(i)
# print(d)
    
    

# s=input("enter  a string... ")
# d={}
# for i in s:
#   if i not in d:
#     d[i]=1
#   else:
#     d[i]+=1
# print(d)




# .........................Polymorphism and its 4 types

# # duck typing
# class Duck:
#     def swim(self):
#         print("Iam a Duck ,i can swim")
#     def speaks(self):
#         print("quack quack")
# class Dog:
#       def swim(self):
#         print("Iam a Dog ,i can swim")
#       def speaks(self):
#         print("wooof wooof")
# class Person:
#       def speaks(self):
#         print("blah blah blah")
        
# class Demo:
#     def display(self,obj):
#         obj.swim


# # operator overloading
# class ComplexNumber:
#     def _init_(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def _add_(self,other):# syntax we created to add 2 complex numbers here self = c1 object(2,3) and other is c2 object(8,9)
#     #   return f" {self.real+other.real} + { self.imaginary+other.imaginary} i" using fsring format
#         return str(self.real+other.real)+ "+" + str(self.imaginary+other.imaginary) + "i"  # using string format
       
# c1=ComplexNumber(2,3)
# c2=ComplexNumber(8,9)
# print(c1+c2) # here we get error because + happens with integr and string as well how is this as we give 1+3 behind the scene is int._add(1,3),similarly for '1'+'2' it is str.add_('1'+'3') ,but here now for complex its not defined so we need to defined it ,i.e whenever it sees + i'll create a add function above it navigates there as above
# # here this + operator performs beyond its capability
# # + calls above add method not that int or str class

# # operator overloading assignment
# class Person:
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def _gt_(self,other):
#         #here self = obj1 = p1 and other = obj2 =p2
#         if self.age>other.age:
#             return True
#         else:
#             return False
# p1=Person('abrar',44)
# p2=Person('hafeez',77)
# if p1>p2:
#     print(f"{p1.name} is elder and will pay the bill")
# else:
#     print(f"{p2.name} is elder and will pay the bill")
# # int.gt when we call >  behind the scens int._gt_(self,x) invokes
# # simlilary < = int._lt(self,y)
# # ?similarly <= = int._le_(self,x)



# method overloading
# #  multpile methods with same name but with different number of args
# # pyhton doesn't support this but we can overcome this
# # note: if you want to utilize  the parameters like a,b  within the class make sure to give self.a ......or similrly to others if not u can normally use it for your purposes



# # class Demo:
# #     def add(self,a,b):
# #         return a+b
# #     def add(self,a,b,c):
# #         return a+b+c
# # d=Demo()
# # # d.add(2,3)
# # print(d.add(2,4,5)) # here the ineterpretor considers add with 3 args coz its line  y line to over come we have 2 stpes below

# # 1
# # class Demo:
# #     def add(self,a,b,c=0):
# #         return a+b+c
# # d=Demo()
# # print(d.add(2,3))
# # print(d.add(2,4,5))
    
        
# # 2
# class Demo:
#     def add(self,*args):
#         s=0
#         for i in args:
#             s+=i
#         return s
            
# d=Demo()
# print(d.add(2,3))
# print(d.add(2,4,5))
# print(d.add(2,3,33,4,55,7,8,9))


#method overriding
#it basically works on inheritance 
# # Scenario 1
# # class Father:
# #     def sleeps(self):
# #         print("sleeps from 10pm to 5am")
# #     def eats(self):
# #         print("eats normally")
# # class Son(Father):
# #     pass
# # s=Son()
# # s.sleeps()
# # s.eats()

# # scenario2
# # here it takes sons sleep method
# # class Father:
# #     def sleeps(self):
# #         print("sleeps from 10pm to 5am")
# #     def eats(self):
# #         print("eats normally")
# # class Son(Father):
# #     def sleeps(self):
# #         print('sleeps as usaul as father sleeps')
# # s=Son()
# # s.sleeps()
# # # s.eats()

# # scenario 3 to overcome this we use super()
# class Father:
#     def sleeps(self):
#         print("sleeps from 10pm to 5am")
#     def eats(self):
#         print("eats normally")
# class Son(Father):
#     def sleeps(self):
#         print('sleeps as usaul as father sleeps')
#         super().sleeps()
# s=Son()
# s.sleeps()
# # s.eats()


# generators
# def gen(s):
#     for i in s:
#         if i in 'aeiou':
#             yield i
# r=gen('abrar')
# print(next(r))
# print(next(r))
# # print(next(r))


# def gen(*args):
#     for i in args:
#         yield i
# r=gen('abrar','hafeez','adnan','shoaib','rahman','fahad')
# d={}
# for j in r:
#     d[j]=len(j)
# print(d)