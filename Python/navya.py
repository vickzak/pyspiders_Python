# amstrong number

# a=int(input("enter a number"))
# b=len(str(a))
# temp=a
# sum=0
# while a>0:
#     rem=a%10
#     sum=sum+rem**b
#     a=a//10
# if temp==sum:
#     print("amstrong")
# else:
#     print("not amstrong")


# a=int(input("enter a range"))
# b=len(str(a))
# for i in range(a+1):
#     temp=a
#     sum=0
#     while a>0:
#         rem=a%10
#         sum=sum+rem**b
#         a=a//10
#     if temp==sum:
#         print("amstrong")
#     else:
#         print("not amstrong")




# perfect numbers
 
# a=int(input("enter a number:"))
# sum=0
# for i in range(1,a):
#     if a%i==0:
#         sum+=i
# if sum==a:
#     print("perfect")
# else:
#     print("not")

# factorial
# a=int(input("enter a number:")) 
# fact=1
# for i in range(1,a+1):
#     fact*=i
# print(fact)


# palindrome

a=input("enter a number:")
# if a[::-1]==a:
#     print("palindrome")
b=len(a)-1
while b>=0:
    c=a[b]
    print(c,end='')
    b-=1
if c==a:
    print("palindrome")
else:
    print("not")
 






















