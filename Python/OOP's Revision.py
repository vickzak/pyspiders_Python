# static class
# class Employee:
#     ename='abrar'
#     id=124433
#     def display():
#         print(Employee.ename,Employee.id)
# Employee.display()


# methods
# first 3 are class level method
# 1.constructor method
# 2.static method
# 3.class method
# 4.instance method   #object level method




# constructor class
# class Employee():
#     def __init__(self,ename,eid): # constructor method
#         self.ename=ename
#         self.eid=eid
#     def info(self,eadd,ecno):   # instance method object level
#         self.eadd=eadd
#         self.acno=ecno
#     @classmethod
#     def cinfo(cls,cname,cid):   #class method class level use decorartor 
#         cls.cname=cname
#         Employee.cid=cid
#     @staticmethod
#     def sta(gst):
#         Employee.reg=778888
#         # gst=gst
#         print(gst)
       
        


# e1=Employee("ram",3456677)
# e1.info("bng",856756668)
# Employee.cinfo("amazon",4566)
# # Employee.sta(77777)
# print(e1.__dict__)
# print(Employee.__dict__)






# create a class calculator which can take 2 numbers and preform all arithmatic operations
# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print( "addition = ",self.a+self.b)
#     def sub(self):
#         print("subtraction = ",self.a-self.b)
#     def mul(self):
#         print( "multiplication = ",self.a*self.b)
#     def div(self):
#         print( "division = ",self.a/self.b)
# c1=Calculator(10,8)
# c1.add()
# c1.sub()
# c1.mul()
# c1.div()
    








# create a class which can read a string  and returns repeated character of the string

# class Strings:
#     def __init__(self,a):
#         self.a=a
#     def rep(self):
#         b=''
#         for i in self.a:
#             if i not in b:
#                 b+=i
#             else:
#                 yield i #returns list of values from
       
# d=Strings('abrar')
# print(list(d.rep()))
# # d.rep()



# # modification  of object _attributes

# class A:
#     def __init__(self,a):
#         self.a=a
#     def disp(self,b):
#         self.b=b
#     @classmethod
#     def disp1(cls,c):
#         cls.c=c
#     @staticmethod
#     def disp2(d):
#         e=123
#         A.d=d
# a1=A(10)
# # a1.a=100
# # print(A.a) #instance  variable cannot be invoked using
# # A.a=1000
# a1.disp(20)
# # a1.b=200
# a1.disp1(30)
# # a1.c=3000 no need aas it is class level use class level 
# A.c=300
# a1.disp2(40)
# print(a1.__dict__)
# print(A.__dict__)



# nested classes or innner classes


#1. #accessing inner class member witin outer class and accessing innner class memenber outside outer class

# a1=A(10)
# class A:
#     def __init__(self,a):
#         self.a=a
#     class B:
#         def __init__(self,b):
#             self.b=b
#     b1=B(20)
#     print(b1.b) #accessing inner class member witin outer class
# a1=A(10)
# print(A.b1.b) # accessing innner class memenber outside outer class
# print(A.B.b)


# 2.# accessing   inner class member outside the outer class without creating object  for  inner class inside outer class

# class A:
#     def __init__(self,a):
#         self.a=a
#     class B:
#         def __init__(self,b):
#             self.b=b

# a1=A(10)
# b1=A.B(200) accessing   inner class member outside the outer class without creating object  for  inner class inside outer class
# print(b1.b)


# sharing a data  within 2 independent class

# 1.has a relation/composition /temporary reltion
# 2.is a relation/Aggregation/inheritance


# 1.has a relation/composition /temporary reltion
# class A:
#     def __init__(self,a):
#         self.a=a
# class B:
#     a1=A(10)
#     def __init__(self,b):
#         self.b=b
# b1=B(20)
# print(b1.b)
# print(b1.a1.a)

# inheritance

# class Company:
#     def __init__(self,cname,cid):
#         self.cname=cname
#         self.cid=cid
# class Employee(Company):
#     def info(self,ename,eid):
#         self.ename=ename
#         self.eid=eid
# e1=Employee("Infosys",123)
# e1.info("abrar",456)
# print(e1.__dict__)

# overriding and super()
# class Company:
#     def __init__(self,cname,cid):
#         print("parent class constructor")
#         self.cname=cname
#         self.cid=cid
# class Employee(Company):
#     def __init__(self,ename,eid):
#          print("child most constructor")
#          self.ename=ename
#          self.eid=eid
#          super().__init__("infosys",433)
# e1=Employee("abrar",3433)
# print(e1.__dict__)


# with two childs
# class Company:
#     def __init__(self,cname,cid):
#         print("parent class constructor")
#         self.cname=cname
#         self.cid=cid
# class Company1(Company):
#     def __init__(self,cadd):
#         print("parent class constructor c1 ")
#         self.cadd=cadd
#         super().__init__("infosys",433)
# class Employee(Company1):
#     def __init__(self,ename,eid):
#          print("child most constructor")
#          self.ename=ename
#          self.eid=eid
#          super().__init__("banglore")

# e1=Employee("abrar",3433)
# print(e1.__dict__)


# abstraction
# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def m1(self,a,b):
#         pass
#     @abstractmethod
#     def m2(self,c,d):
#         pass
#     @abstractmethod
#     def m3(self,e,f):
#         pass
# class B(A):
#     def m1(self,a,b):
#         self.a=a
#         self.b=b
#         return self.a,self.b
#     def m2(self,c,d):
#         self.c=c
#         self.d=d
#         return self.c,self.d
#     def m3(self,e,f):
#         self.e=e
#         self.f=f
#         return self.e,self.f
# b1=B()
# print(b1.m1(10,20))
# print(b1.m2(30,40))
# print(b1.m3(50,60))






# wap to create a bank class  which can read a account holder  information and returns statement of his account(deposit,withdraw,min balance,transaction)

# class B:
#     def __init__(self,cname,cid,pin):
#         self.balance=1000
#         self.cname=cname
#         self.cid=cid
#         self.pin=pin
#     def deposit(self,dep):
#           self.dep=dep
#           self.balance=self.balance+self.dep
#           print("total balance after depositing",self.balance)
#     def withdraw(self,withd):
#          self.withd=withd
#          if self.withd>1000:
#               print("Insufficinet amount to withdraw")
#          else:
#               self.balance=self.balance-self.withd
#               print("amount after withdrawn ",self.balance)
# b1=B('abrar',1234,4567)
# print(b1.deposit(5000))
# print(b1.withdraw(2000))
# print(b1.__dict__)

              
              

         



        

        # if self.cname=='abrar' and  self.cid==123456 and self.pin==2345:
        #     print("Welcome",self.cname)
        #     print("1.deposit","2.withdraw","3.balance")
        #     self.take=int(input("enter a choice"))
        #     if self.take==1:
        #         self.deposit=int(input("Enter a amount to be deposited"))
        #         self.balance=self.balance+self.take
        #         print("total balance after depositing",self.balance)
        #     elif self.take==2:
        #         self.withdraw=int(input("enter amount to be withdrawn"))
        #         print("withdrawn successfully")
        #         self.balance=self.balance-self.withdraw
        #         print("total balance after withdrawing ",self.balance)
# b1=B('hafeez',1233,355)
            
          


        

class A:
    def __init__(self,a):
        self.a=a
    class B:
        def __init__(self,b):
            self.b=b
    b1=B(20)
a1=A(30)
print(a1.b1.b)
print(a1.a)


        

# class A:
#     def __init__(self,a):
#         self.a=a
#     class B:
#         def __init__(self,b):
#             self.b=b
# b1=A.B(10)
# print(b1.b)
        


# class A:
#     def __init__(self,a):
#         self.a=a
# class B:
#      a1=A(10)
#      def __init__(self,b):
#           self.b=b
# b1=B(20)   
# print(b1.b)
# print(b1.a1.a)


# class A:
#     def m1(self,a):
#         self.a=a
# class B(A):
#       def m1(self,b):
#         self.b=b
#         super().m1('abrar')
# b1=B()
# b1.m1('hafeez')
# print(b1.__dict__)


class A:
    def m1(self,name):
        self.name=name
    def m2(self,dob):
        self.dob=dob
class B:
      def m2(self,place):
        self.place=place
class C(A,B):
     def m3(self,c):
        self.c=c
c1=C()
c1.m1('abrar')
c1.m2('6788')
c1.m3('hii')
print(c1.__dict__)