# Write a program to find the biggest of two numbers

# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# if a>b :
#     print(a,"is the biggest")
# elif b>a:
#     print(b,"is the biggest")
# else:
#     print(a,"and",b," are equal")


# # WAP to find the biggest of 3 numbers
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# c=int(input("Enter the second number"))
# if a>c and a>b:
#     print(a,"is the bigeest of three")
# elif b>c and b>a:
#     print(b,"is the bigeest of three")
# else:
#     print(c,"is the bigeest of three")


# # WAP  to swap the values without using third variable
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# print("the numbers before swapping are",a,b)
# a=a+b
# b=a-b
# a=a-b
# print("the numbers after swapping are ",a,b)

# # WAP TO SWAP THE VALUES WITH THIRD VARIABLE
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# print("the numbers before swapping are",a,b)
# c=a
# a=b
# b=c
# print("the numbers after swapping are ",a,b)


# # WAP to check even or odd
# a=int(input("Enter the number"))
# if a%2==0:
#     print(a,'is even no')
# else:
#     print(a,'is odd')

# WAP to print the numbers in a given  rangee
# for i in range(1,11):
#     print(i)

# i=1
# while i<11:
#     print(i)
#     i+=1



# WAP tp print only even numbers  in the given range

# for i in range(1,11):
#     if i%2==0:
#         print(i)


# Wap to print the numbers in given range in reverse order


# i=11
# while i>1:
#     print(i)
#     i-=1

# for i in range(11,1,-1):
#     print(i)


# WAP to print sum of the numbers in a a given range from 1 to n
# sum=0
# for i in range(1,12):
#     sum=sum+i
#     print(sum)


# s=0
# i=1
# while i<=12:
#     s=s+i
#     print(s)
#     i+=1



# WAP  to print only the sum of even numbers in a given range

# sum=0
# for i in range(1,12):
#     if(i%2==0):
#         sum=sum+i
#         print(sum)
#     else:
#         print(i,"its odd so no sum")4


  # factorial program

# a=int(input("Enter the number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)



# write a program  to find factors of given number

# b=10
# for i in range(1,b+1):
#   if b%i==0:
#     print(i)


# WAP to find product of first four natural number

# a=1
# for i in range(1,5):
#   a=a*i
#   print(a)



# WAP to check whether the given number is prime number or not

# a=int(input("Enter a number"))
# if(a%2!=0 and a%3!=0):
#   print(a,'is prime number')
# else:
#     print(a,'is  not prime number')

# WAP to check the given number is amstrong number
# a=int(input("enter a   number ")) 153
# count=len(str(a))
# temp=a
# sum=0
# while a!=0:
#   rem=a%10
#   sum=sum+rem**count
#   a=a//10

# if temp==sum:
#   print("its an amstrong number")
# else:
#   print("not a amstrong number")



  #     print(a,'is  not prime number')

# WAP to check the given number is amstrong number in a range


# a=int(input("enter a   number "))
# for i in range(1,a+1):

#   a=i

#   count=len(str(a))
#   temp=a
#   sum=0
#   while a!=0:
#     rem=a%10
#     sum=sum+rem**count
#     a=a//10

#   if temp==sum:
#     print("its an amstrong number",sum)


# WAP  to check if the number is perfect number

# a=int(input("Enter a number"))
# sum=0
# for i in range(1,a):
#   if a%i==0:
#     sum+=i
#   print(sum)
# if(sum==a):
#   print("the given number is perfect number")
# else:
#    print("the given number is  not perfect number")


# # happy number
# a=int(input('enter a number'))

# while a!=1 and a!=4:
#   sum=0
#   while a!=0:
#       rem=a%10
#       sum=sum+rem**2
#       a=a//10
#   a=sum
# if a==1:
#   print(" a happy number")
# else:
#   print("not a happy number")



# #  print prime no from  a given range
# a=int(input('enter a range from 1 to '))

# for i in range(1,a+1):
#           if i%2!=0 and i%3!=0:
#             print(i)
# # if count==2:
# #   print()




# a=int(input('enter a number'))
# for i in range(1,a+1):
#   c=0
#   for j in range(1,i+1):
#     if i%j==0:
#          c+=1
#   if c==2:
#         print(i)



# program to arrange the number in ascending order using bubble sort

# a=[3,6,677,33,6,7,900]

# for i in range(1,len(a)):
#   for j in range(1,len(a)):
#     if a[j-1]>a[j]:
#       a[j-1],a[j]=a[j],a[j-1]
# print("after sorting",a)




# # wap to count the no  of digits in a given number
# a=int(input('enter a no'))
# c=0
# while a!=0:
#   a=a//10
# #   c+=1
# # print(c)

# # # wap to check whether the given number is a perfect square or not
# # a=int(input('enter a no'))
# # for i in range(1,a+1):
# #   if(i*i==a):
# #     print(a,'is a perfect square')
# #     break


# # wap to check whether the given number is neon or not

# a=int(input('enter a no'))
# sum=0
# sq=a*a
# while sq!=0:
#   rem=sq%10
#   sum=sum+rem
#   sq=sq//10
# if(sum==a):
#   print(a,'is neon')
# else:
#   print(a,'not neon')


# # wap to check to check th given  no is sunny

# a=int(input('enter a no'))
# num=a+1
# for i in range(1,a+1):
#   if(i*i==num):
#     print(a,'is sunny no')
#     break

# wap to reverse a list using while loop

# r=[]
# a=[1,2,3,4]
# i=len(a)-1
# while i>=0:
#   r+=[a[i]]
#   i-=1
# print(r)

# wap to reverse a list using for loop

# r=[]
# a=[1,2,3,4]
# i=len(a)-1
# for a[i] in  a:
#   r=r+[a[i]]
#   i-=1
# print(r)

# # using range n for
# a=[1,2,3,4]
# li=[]
# for i in range(len(a)-1,-1,-1):
#      li+=[a[i]]
# print(li)

# using another method
# l=[1,2,3,4]
# l1=[]
# for i in l:
#   l1=[i]+l1
# print(l1)


# WAP to find maximum number from a given list 

# a=[1,10,4,5,4]
# print(max(a))


# a=[1,10,4,5,4]
# m=0
# for i in a:
#  if  m<i:
#      m=i
# print(m)

# WAP to find min number from a given list 
# a=[1,10,4,5,4]
# m=1
# for i in a:
#  if  m>i:
#      m=i
# print(m)

# WAP to find second max number from a given list 
# a=[1,10,4,5,4]
# m=0
# m1=0
# for i in a:
#  if  m<i:
#      m=i
# for i in a:
#  if  m1<i and i!=m:
#     m1=i
# print(m1)



# waf  which returns only positive number


# def positive(*a):
#    for i in (a):
#     print(abs(i))
# positive(-3,-6,8,6,3,2,-7,0,-6,-4)


# # def pos_num(num):
# #   if num<0:
# #     return num*-1
# #   else:
# #     return num
# # a=pos_num(-3)
# # print(a)



# # wa   function which returns a word  which starts with vowel and have even length from given string



# def words(s):
#   res=[]
#   for i in s.split():
#     if i[0] in 'aeiouAEIOU' and len(i)%2==0:
#       res.append(i)
#   return res
# print(words('abrar ul haq hello how aree you'))



# wa function which returns perfect square number
# def sqr(num):
#   root=round(num**0.5)
#   if num==root**2:
#     return num
# print(sqr(9))


# wa function which returns perfect cube number
# def sqr(num):
#   root=round(num**0.33)
#   if num==root**3:
#     return num
# print(sqr(9))


# write a lambda function which  checks for palindrome present in a string

# palindrome=lambda s:[ (i,'is palindrome') for i in s.split() if i==i[::-1]]
# print(palindrome('madam'))

# a=input('entemamr a word')
# b=("".join(list(reversed(a))))
# if a==b:
#   print(a,'is palindrome')
# else:
#   print(a,'is not a palindrome')



# wap using lambda function that returns even
# even=lambda s: s%2==0 
# print(even(8))



# wap using lambda function which checks for palindrome if not reverse the string

# palindrome=lambda s:   s   if s==s[::-1] else s[::-1]
# print(palindrome('madam'))



# wap using lambda function which returns perfect square

# perfect_square=lambda num:  num  if round(num**0.5)**2==num else None
# print(perfect_square(9))




# wap using lambda function which filters all the word of a string which starts with vowel

# vowel=lambda s: [i for i in s.split() if i[0] in 'aeiouAEIOU']
# print(vowel('ambrella'))


# wap to iter into a string and create dictionary of character and  and count pair

# s=input("enter  a string... ")
# d={}
# for i in s:
#   if i not in d:
#     d[i]=1
#   else:
#     d[i]+=1
# print(d)



# using function
# def dict(s):
#       d={}
#       for i in s:
#           if i not in d:
#             d[i]=1
#           else:
#               d[i]+=1
#       return d # print(d) 
# print(dict('hi hello comeback'))


# using lambda

# ch_count=lambda s: { i:s.count(i) for i in s}   
# print(ch_count('hi all'))



  

# wap to reverse a integer
# a=423
# r=0
# while a!=0:
#     digit=a%10
#     r=r*10+digit
#     a=a//10
# print(r)



# # ...........................normal fibonacci
# a=int(input("enter a arnage"))
# num1=0
# num2=1
# next_num=num2
# count=0
# while count <a:
#   print(next_num,end=',')
#   count+=1
#   num1,num2=num2,next_num
#   next_num=num1+num2

# ................................fibonacci with recurssion
# def fibonacci(n):
#   if n<0:
#     return 'invalid input'
#   elif n==0:
#     return 0
#   elif n==1 or n==2:
#     return 1
#   else:
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(8))
    

# ...................................recurssion of factorial

# def factorial(n):
#   if (n==0 or n==1):
#     return 1
#   else:
#     return n * factorial(n-1)
# print(factorial(7))
# 7*factorial(6)
# 7*6*factorial(5)






  











    

 


















