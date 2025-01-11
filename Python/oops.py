# creating static class
# class Employee:
#     ename='andy'
#     eid=123
#     print('iam in class')
#     def display():
#         print(Employee.ename,Employee.eid)
# Employee.display()



# creating dynamic  class
# class Employee:
#     print("in class employee")
#     def display(self,ename,eid):      #self=e1 ,ename=ram ,eid=123
#         self.ename=ename               #e1.ename=ram
#         self.eid=eid                   #e1.eid=123
#         print(self.ename,self.eid)

# e1=Employee()     #creating object  to employee class
# e1.display("ram",123)   #calling display method for e1


# # printing in the form of ductionary
# print(e1.__dict__)    #checking information  of object e1 by acccessing dictionary of object

# # creating another object 
# e2=Employee()
# # e2.display("harry",689)


# # # deleting object e1

# # # del e1
# # # e1.display('gi',77)    got deleted


# # # modifying property of e1
# # e1.ename="abrar"
# # print(e1.__dict__)



# # creating student class
# class Student:
#     print('iam in class')
#     def personal_Details(self,sname,sage):
#         self.sname=sname
#         self.sage=sage
#         print(self.sname,self.sage)
#     def Course_Details(self,Cname,Cid,Ccredits):
#         self.Cname=Cname
#         self.Cid=Cid
#         self.Ccredits=Ccredits
#         print(self.Cname,self.Cid,self.Ccredits)

# s1=Student()
# s1.personal_Details('ram',22)
# print(s1.__dict__)

# s1.Course_Details("CSE",233,3)
# print(s1.__dict__)


# # s2=Student()
# print(Student.__dict__)  # self is nothing but referring object i.e e1,e2,e3...etc



# constructors

# class Student:
#     def __init__(self,sname,sid,scno):
#         self.sname=sname
#         self.sid=sid
# #         self.scno=scno
# #         print(self.sname,self.sid,self.scno)
# #         print(sname,sid,scno)
# #     def display(self):
# #         print(self.sname,self.sid,self.scno)
# #         # print(sname,sid,scno)
# # s1=Student('abc',123,678779880)
# # s2=Student('red',767,888979880)
# # print(s1.sname) # instance in inside class we use self but in outside we object.name
# # s1.display()




# # instance
# class Employee:
#     def __init__(self,ename,eid):
#         self.ename=ename
#         self.eid=eid

#     def display(self,esal,edob):
#         self.esal=esal
#         self.edob=edob
#         print(f"{self.ename} with employee id {self.eid} have salary of {self.esal}")
# e1=Employee('alex',123)
# e1.display(25000,'01/02/2000')
# e1.ename='harry'
# Employee.eid=678
# print(e1.__dict__)
# print(Employee.__dict__)
# print(e1.ename)
# # print(self.ename)



# # class method
# class bank:
#     def __init__(self,aname,anum):
#         self.aname=aname
#         self.anum=anum

#     @classmethod
#     def bank_info(cls,bname,reg_no):
#         cls.bname=bname
#         cls.reg_no=reg_no
#     @staticmethod
#     def info(logo):
#         bank.rbino=4559775757
#         bank.logo=logo# prints in the form of dict
#         print(logo)#prints normal


# b1=bank('ram',4565678896)
# b1.bank_info('sbi',566768767)
# print(b1.__dict__)# prints only constructor method output 
# print(bank.__dict__)# print bank info,if you wanna see claasmethod output use classname .__dict__
# bank.bname='Canara'# gets relected in 
# print(b1.__dict__)
# print(bank.__dict__)
# b1.info("sbi(r)")
# print(b1.__dict__)
# print(bank.__dict__)



# Nested class

# class A:
# #     def display(self,a):
# #         self.a=a
# #         print(self.a)
# #     class B:
# #         def func(self,b):
# #             self.b=b
# #             print(self.b)
# # a1=A()
# # a1.display(100)

# # b1=a1.B() #object of class A with class B
# # b1.func(200)


# #calling one class properties within another class
# class A:
#     def display(self,a):
#         self.a=a
#         print(self.a)
# class B:
#         a1=A()
#         # a1.display(10)
#         # print(a1.a)
#         def func(self,b):
#             self.b=b
#             print(self.b)
# b1=B()
# b1.a1.display(100)



# create a class which return even numbers from given range

# class even_numbers:
#     def __init__(self,a,b):
#           l=[]
#           self.a=a
#           self.b=b
#           for i in range(self.a,self.b+1):
#              if i%2==0:
#                 l.append(i)
#           print(l)  as constructor returns none so we need to print if we need to return use instance method as below

# e1=even_numbers(0,100)



# class even_numbers:
#     def eve(self,a,b):
#           l=[]
#           self.a=a
#           self.b=b
#           for i in range(self.a,self.b+1):
#              if i%2==0:
#                 l.append(i)
#           return l 

# e1=even_numbers()
# print(e1.eve(2,40))




# create a class which accepts any iterbales but returns a list only

# class iterables:
#     def iter(self ,a):
#         self.a=a
#         return list(a)
# a1=iterables()
# print(a1.iter({6,5,6,7}))


# create a class which accepts all iterables and returns even length list only

# class iterables:
#     def iter(self ,a):
#         self.a=a
#         if len(self.a)%2==0:
#             return list(a)
# a1=iterables()
# print(a1.iter((45,6,7,8)))




# class even_length:
#     def __init__(self,a):
#         self.a=a
#         self.b=list(self.a)
#         if len(self.b)%2==0:
#             print(self.b)
#         else:
#             self.b.append("None")
#             print(self.b)

# e1=even_length((3,4,5,6,7))


# wap to create a class which takes integers and returns roman form of that number

# wap to create a class which takes roman number and returns integers form of that number
            


# Inheritance
# single level
# class A:
#     def disp(self,a,b):
#         self.a=a
#         self.b=b
#         return self.a+self.b
# class B(A):
#     def add(self,c,d):
#         self.c=c
#         self.d=d
#         return self.c+self.d

# b1=B()
# print(b1.disp(2,3))
# print(b1.add(4,6))

# multilevel inheritance

# class A:
#     def disp(self,a,b):
#         self.a=a
#         self.b=b
    
# class B(A):
#     def add(self,c,d):
#         self.c=c
#         self.d=d
# class C(B):
#     def func(self):
#         return self.a+self.b+self.c+self.d
      

# c1=C()
# c1.disp(1,2)
# c1.add(3,4)
# print(c1.func())


# example on multilevel inheritance


    


# class Bank:
#     def bank_info(self,bname,bid):
#         self.bname=bname
#         self.bid=bid
#     def emp_benefits(self,rewards,others):
#         self.rewards=rewards
#         self.others=others
# class Employee(Bank):
#     def emp_details(self,ename,eid):
#         self.ename=ename
#         self.eid=eid
#     def emp(self,msal,doj):
#         self.msal=msal
#         self.doj=doj
# class Calci(Employee):
#      def exp(self,cdate):
#         self.cdate=cdate
#         y=(self.cdate[1]-self.doj[1]-1)*12
#         no_of_exp=(12-self.doj[0]+self.cdate[0]+y)
#         return f"{self.ename} worked for {no_of_exp} Months"
        
#      def annual(self):
#         ann=12*self.msal
#         t_rewards=((self.rewards+self.others)*ann)/100
#         net_sal=t_rewards+ann
#         return f"net salary of {self.ename}  is {net_sal} and yearly award he won is {t_rewards}"
        
# c1= Calci()  
# c1.bank_info("canara",223)
# c1.emp_benefits(10,5)
# c1.emp_details("ashwin",3433)
# c1.emp(30000,(3,2022))
# print(c1.exp((5,2024)))
# print(c1.annual())


# # single dispatch()
# from functools import singledispatch
# @singledispatch
# def add(a):
#     print(a)
# @add.register(int)
# def _(a):
#     print(a)
# @add.register(float)
# def _(a):
#     print(a)
# @add.register(str)
# def _(a):
#     print(a)
# add(8j)


# # using  single dispatch method in class 
# from functools import singledispatchmethod
# class A:
#     @singledispatchmethod
#     def add(self,a):
#         self.a=a
#         print(self.a)
#     @add.register(int)
#     def _(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a,self.b)
#     @add.register(float)
#     def _(self,a):
#          self.a=a
#          print(self.a)
#     @add.register(str)
#     def _(self,a):
#          self.a=a
#          print(self.a)
# a=A()
# a.add(10,2)



# # multipledispatch
# from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a,self.b)
#     @dispatch(int,float,bool)
#     def add(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#         print(self.a,self.b,self.c)
    

# a=A()
# a.add(10,20)
# # a.add(10,10.6)
# a.add(10,20.4,True)



# # abstraction
# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def disp(self,msg):
#         pass
#     def info(self,a):
#         pass
# class B(A):
#     def disp(self,msg):
#         self.msg=msg
#         print(self.msg)
#     def info(self,a):
#         self.a=a
#         print(self.a)
# # b1=B()
# # b1.disp("hello")
# # b1.info(10)


# #encapsulation









# # generators

# def vowels(s):
#     for i in s:
#         if i in 'aeiouAEIOU':
#             yield i
# res=vowels("hello all")
# # print(list(res))
# # for i in res:
# #     print(i)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))



# wap to create a function which generates leap years from given range
# def leap(s):
#     for i in range(20,s+1):
#         if i%4==0:
#             yield i
# res=leap(24)
# print(list(res))


# wa function which yields all perfect square numbers from the given range
# def ps(s):
#     for i in range(1,s+1):
#         root=round(i**0.5)
#         if root**2==i:
#             yield i
            
# res=ps(42)
# print(list(res))


# wagf which yields perfect cubes from the given range of numbers
# def pc(s):
#     for i in range(1,s+1):
#       root=round(i**0.33)
#       if root**3==i:
#         yield i

# res=pc(33)
# print(list(res))
 

# wagf which yields prime numbers from the given range
# def pn(s):
#     for i in range(1,s+1):
#         if i%2==0 or i%i==0:
#             yield i
# res=pn(25)



# # wagf which yields all words starting with vowel and have even length
# def vowel(s):
#     for i in s.split():
#         if i[0] in 'aeiouAEIOU' and len(i)%2==0:  
#             yield i
# res=vowel("hello all how are you outn")
# print(list(res))

        
# wagf which yields all numeric types from a iterable

# def iterable(list):
#     for i in list:
#         if isinstance(i,(int,float,complex,bool)):
#             yield i

# res=iterable([1.1,4,'True',8j,'rr',5444])
# print(list(res))




# # wagf which checks for muatbility  and immutability of elements  of an iterable if mutable add elements if not yield as it is
# def m_check(l):
#     for i in l:
#         if isinstance(i,(int,float,bool,tuple,str,complex)):
#             yield i
#         elif  isinstance(i,list):
#             i.append(20)
#             yield i
#         elif isinstance(i,set):
#             i.add(45)
#             yield i
#         else :
#             i.update({'name':'abrar'})
#             yield i
# res=m_check([12,22.3,7j,'true',[22,34,'hi'],{34,56,34,'bye'},{1:100,4:500}])
# print(list(res))
        

# l=[1,2,3,4]
# l[0]=10
# print(l)

# l.extend("hi iam good")
# print(l)

# from itertools import zip_longest
# l=[1,2,3,4,[5,6,6,4],3,4,4]
# l2=['a','b','c','e',10,30]
# l3=[True,8j]
# print(list(zip_longest(l,l2,l3)))


# l=[1,2,3,4]
# l.pop(2)
# print(l)
# l.remove(1)
# print(l)









# # wap to generate  leap years from the given range using while /for/isleap

# y1=int(input())
# y2=int(input())
# from calendar import isleap
# for i in range(y1,y2+1):
#     # if isleap(i)==True:
#      if isleap(i):
#         print(i)


# # using while
# y1=int(input())
# y2=int(input())
# from calendar import isleap
# while y1<=y2:
#    if isleap(y1)==True:
#        print(y1)
#        y1+=1



# d={}
# d.update({1:100})
# d.update(a=100)
# d.update([(1,100),(2,200),(3,300)])  # iterable of iterable tis enumerate
# print(d)
    

# # wap to create dictionary of index and character pair using normal method
# s='hello all'
# d={}
# for i in s:
#     d[s.index(i)]=i  # if we use index than it returns first occurence to avoid this we moved to range
# print(d)


# wap to create dictionary of index and character pair using range method
# s='hello all'
# d={}
# for i in range(len(s)):
#     d[i]=s[i]
# print(d)

# wap to create dictionary of index and character pair using enumerate method
#enumerate method returns enumerate object
# anything that returns object  to see we use list(enumerate)
# enumerate contains tuples with index and cahra/value
# s='hello all'
# d={}
# # for i in range(len(s)):
# #     d[i]=s[i]
# # print(d)
# # print(list(enumerate(s))) # its in form of tuple to acces in the of dict use directly dict(enumerate(s))
# print(dict(enumerate(s)))



# to access index and values individually using for
# for  i,j in enumerate(s):
#     d[i]=j  # here i=index j=char/value
# print(d)




# wap  to create a dictionary of word and its length pair if word is at even position keep it as it is or else reverse it

# s="an apple a day keeps doctor away"
# d={}
# for i,j in enumerate(s.split()):
#     if i%2==0:
#         d[j]=len(j)
#     else:
#         # d[j[::-1]]=len(j)
#         d["".join(reversed(j))]=len(j)
# print(d)  
# reversed  method   =  applicable to all datatypes as string is immuatbale we us reversed
# reverse method is  for only mutable datatype


# in string
# if no slicing how to reverse  we can by reversed 
# s='hello'
# print(list(reversed(s)))
# print("".join(reversed(s)))



# zip()
# s="happy"
# s1="apple"
# l=[1,2,3]
# print(list(zip(s,s1,l)))# if length is not same it considers shortest length which results in loss of data
    
# zip_longest()
from itertools import zip_longest
# s="happy"
# s1="apple"
# l=[1,2,3]
# print(list(zip_longest(s,s1,l,fillvalue='')))# for remaining length it gives none if you want to change the value than yse the fillvalue




# # wap to add the elements  of same position of the given iterables
# l=[10,25.55,True,8j,65]
# l1=['hi',18,45.65,False]
# l2=(1,2,3,4j,"app",True,8,11)
# for i,j,k in zip_longest(l,l1,l2,fillvalue=0):
#     if isinstance(i,(int,float,complex,bool)) and isinstance(j,(int,float,complex,bool)) and isinstance(k,(int,float,complex,bool)):
#                 #  print(i,j,k)
#                  print(i+j+k)
#     else:
#             print("not supportive")



# wap to raise elements of an iterable  to its indices
# l=[10,25.55,'hi',65,8j,(1,2),[10,20],True]
# for i ,j in zip(l,range(len(l))):
#     if isinstance(i,(int,float,complex,bool)):
#         print(i**j)
#         # print(i,j)
#     else:
#         print(f"{i} is not supportive for **")


# using enumerate
# l=[10,25.55,'hi',65,8j,(1,2),[10,20],True]
# # print(list(enumerate(l)))
# for i ,j in enumerate(l):
#     # print(i,j)
#     if isinstance(j,(int,float,bool,complex)):
#         print(j**i)
#     else:
#         print(f"{j} is not supportive to ** ")


# # wap to add the elements  of same position of the given iterables using for loop
# l=[10,25.55,True,8j,65]
# l1=['hi',18,45.65,False]
# l2=(1,2,3,4j,"app",True,8,11)
# for i in range(len(l)):
#     if isinstance(l[i],(int,float,complex,bool)) :
#         print(l)

    # print(i)

    
# wap to check  the list contains  integer below 500 and find the sum
# l=['hi',1,50,655,481,500,320,380,700,221]
# sum=0
# for i in l:
#     if   isinstance(i,(int)) and i<=500:
#         sum+=i
#         continue
# print(sum)
        
    
        




























