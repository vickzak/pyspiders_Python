# .................Specific Exception handling............................
# try:
#     a=int(input("enter"))
#     b=int(input("enter"))
#     # b=input("enter")
#     # print(a+b)
#     print(a/b)
# except ValueError:
#     print("enter only integer value")
# except TypeError:
#     print("cant concatinate different type of value ")
# except ZeroDivisionError:
#     print("enter other than 0")




# ........................Generic Exception handling....................................
# try:
#     a=int(input("enter:"))
#     b=input("enter")
#     print(a+b)
#     i=1
#     while i>0:
#         print(i)
#         i+=1
# except Exception:
#     print("exception handles succesfully")


# # .......................Default Exception hnadling...................
try:
    i=1
    while i>0:
        print(i)
        i+=1
except:
    print("keyboard interrupt handled")



# Error creation
# 1.coustom error
# 2.userdefined error
# 3.assertion error


# 1.coustom error
# in this we need to pass inbuilt error only,liketypeerror,valueerror etc................

# x=int(input("enter "))
# if x%2==0:
#     print(x**2)
# else:
#     raise TypeError('not even')

# wap to chech whether the string is palindrome or not without using slicing if not a palindrome raise error
# a=input("Enter a string...")
# b=len(a)-1
# c=[]
# while b>=0:
#     c.append(a[b])
#     b-=1
# # print(''.join(c))
# if c==a:
#     print("palindrome")
# else:
#     raise NameError('NOT PALINDROME')


# using for
# a='abrar'
# l=''
# for i in a:
#     # l+=i l=l+i
#     l=i+l
# # print(l)
# if l==a:
#     print("palindrome")
# else:
#     raise NameError('not palindrome')



# a= ['amazon.com','file.py','web.html','file2.py']

# d={}
# for i in a:
#     b=i.split('.')
#     # print(b)
#     if b[1] not in d:
#         d[b[1]]=[b[0]]
#     else:
#         d[b[1]].append(b[0])
# print(d)




# Userdefined error


# class manju (Exception):
#     pass
# a=input("enter:")
# if len(a)%2==0:
#     print("equal")
# else:
#     raise manju('not equal')

# wap to check whether the number is prime or not if not raise error using userdefined error
# a=int(input("enter"))
# class PrimeError (Exception):
#     pass
# for i in range(2,a):
#     if a%i==0:
#         raise PrimeError('not prime')
    
# else:
#     print("prime")


# wap to reverse a int value
# a=1234
# r=0
# while a!=0:
#     d=a%10
#     r=r*10+d
#     a=a//10
# print(r)


# ASSERTION ERROR
#   wap to create assertion errror if the value is less than 10
# a=int(input("enter"))
# assert a>10,'less than 10'
# print('not less than 10')



a='always keep smiling'
b=a.split()
print(b)
d={}
for i in b:
    # print(i)
    for j in i:
        # print(j)
        if j in 'aeiou':
            e=''
            e=j+j
        # print(e)
    d[i]=[ len(i),i[::-1],e]
print(d)


# {1,2}*2
# {1,2}+{3,4}
# a='rar'
# e=''
# b=len(a)-1
# while b>=0:
#     e=e+a[b]
#     b-=1
# if e==a:
#     print("palindrome")
# else:
#     print("no")


# a=4089
# d=0
# while a!=0:
#     rem=a%10
#     d=d*10+rem
#     a=a//10
# print(d)
# a=121
# count=len(str(a))
# temp=a
# sum=0
# while a!=0:
#     rem=a%10
#     sum=sum+rem**count
#     a=a//10
# if sum==temp:
#     print("amstrong")
# else:
#     print("not")


 

# interview question
# l=[100,45,60,45,45,68,88,56,49,50,49]
# a=int(input("enter marks"))
# l1=[]
# for i in l:
#     if i not in l1:
#             l1.append(i)
# l1.append(a)
# for j in range(1,len(l1)):
#     for k in range(1,len(l1)):
#          if l1[k]>l1[k-1]:
#               l1[k],l1[k-1]=l1[k-1],l1[k]          
# for m in range(len(l1)):
#      if l1[m]==a:
#           print("rank :",m+1)
# print(l1)


# # leetcode
# l1=[5,4,3,2]
# l2=[7,5,4,3]
# a=zip(l1,l2)
# print(list(a))
# b=list(a)
# print(b[1])
         

# a='abrarulhaq' 
# b=''
# for i in range(len(a)):
#     if i%2==0:
#         b=b+a[i].upper()
#     else:
#         b=b+a[i]
# print(b)
        


         
         
      
       





    


       



        

    

    
    




