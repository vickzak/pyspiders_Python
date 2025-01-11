
# a='always keep smiling'
# b=a.split()
# d={}
# for i in b:
#     for j in i:
#         if j in 'aeiou':
#             e=''
#             e=j+j
#         # print(e)
#     d[i]=[ len(i),i[::-1],e]
# print(d)


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

# primenumber
# a=11
# for i in range(2,a):
#     if a%i==0:
#         print("not prime")
#         break
# else:
#     print("prime number")

# amstrong number
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



# or

# a=int(input("enter a number"))
# count=len(str(a))
# sum=0
# for i in str(a):
#     sum=sum+int(i)**count

# if sum==a:
#     print("pal")
# else:
#     print("not pal")



# factorial number
# n=int(input("enter a number"))
# fact=1
# # sum=0
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


# strong number
# n=int(input("enter a number"))
# sum=0
# for i in str(n):
#     fact=1
#     for j in range(1,int(i)+1):
#         fact=fact*j
#     sum=sum+fact
# if sum==n:
#     print("strong number")
# else:
#     print("not strong")


# perfect number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a):
#     if a%i==0:
#         sum+=i
# if sum==a:
#     print("perfect number")

# wap to extract all the string values present in a list
# l=[1,2,3,'start','hi',45.5]
# for i in

# l=eval(input("enter a list"))
# nl=[]
# for i in l:
#     if isinstance(i,(str)):
#         nl.append(i)
# print(nl)

# using while
# l=eval(input("enter a list"))
# # print(l)
# nl=[]
# i=0i
# while i<len(l):
#     if isinstance(l[i],str):
#         nl.append(l[i])
#     i+=1
# print(nl)

# using recurrsion
# def extract(l,i=0,nl=[]):
#     if i>=len(l):
#         return nl
#     if isinstance(l[i],str):
#         nl.append(l[i])
#     return extract(l,i+1,nl)
# print(extract(eval(input("enter"))))



#  patternd for 5 * 5 rows and cols
# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end='')
#     print()


# pattern for diagonal and its 3 parts
# for i in range(1,6):
#     for j in range(1,6):
#         if i==j:
#          print('*',end='')
#         else:
#            print(' ',end=' ')
#     print()

# pattern for lower traingle

# for i in range(6):
#     for j in range(6):
#         if i>j:
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()

# pattern for upper triangle
# for i in range(6):
#     for j in range(6):
#         if i<=j:
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()




# .....................................
# secondary diagonal
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()

# secondary diagonal for uppertraingle
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j<=n+1:uy
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()


# secondary diagonal for lowertraingle
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j>=n+1:
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()




# for i in range(1,5):
#     for j in range(1,9):
#         if i+j>=n+1:
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()

# a=10
# for i in range(1,a+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print(i)


# a=[2,4,5,6,7,8,2,3,5]
# for i in range(1,len(a)):
#     for j in range(1,len(a)):
#         if a[j-1]>a[j]:
#             a[j-1],a[j]=a[j],a[j-1]
# print(a)

# a=[1,2,6,4,8,9]
# d=[]
# for i in a:
#     for j in a:
#         if i>j:
#             d.append(i-j)
# print(d)
# print(max(d))

# a=4
# b=[1,2,5,4]
# c=9
# d=0
# for i in b:
#     for j in b:
#         if i+j==c:
#             d+=1
#     if d==1:
#         print("yes")

            
        
# a='dumadu'  
# b=9
# for i in range(b):
#     for j in range(len(a)):
#         if i==round(b/2):
#             for k in a:
#                 print(k,end=' ')
#             break
#         else:
#             print('*',end=' ') 
#     print()

       
# n=5
# for i in range(n+1):
#     for j in range(n+1):
#         if  i==n :
#             print('*',end=' ')
#         else:
#             print('',end='')
#     print()

# l=[10,49,67,9,45,33,10]
# for i in range(1,len(l)):
#     for j in range(1,len(l)):
#         if l[j]>l[j-1]:
#             l[j],l[j-1]=l[j-1],l[j]
# print(l)

# v='''{
#         windows:[1,2,3,4,5,5,5,]
#         mac:[67,7,8,9,8,8,7]
#     }'''
# # print(type(v))
# b=v.split()
# # print(b[1])
# # print(type(b[1]))
# new=b[1].split(':')
# # print(new)
# d={}
# l=new[1]
# c=0
# for i in l:
#     if isinstance(i,int):
#         c+=1
# print(c)


#  to print lower traingle in 5 54 543 5432 54321

# for i in range(6):
#     c=5
#     for j in range(6):
#         if i>j:
#          print(c,end=' ')
#          c-=1
#         else:
#            print(' ',end=' ')
#     print()
   
#  to print lower traingle in 1 12 123 1234 12345
# for i in range(6):
#     c=1
#     for j in range(6):
#         if i>j:
#          print(c,end=' ')
#          c+=1
#         else:
#            print(' ',end=' ')
#     print()

    







