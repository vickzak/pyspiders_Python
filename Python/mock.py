# wap to reverse a list
# a=[3,2,10,12,7,4]
# i=len(a)-1
# rev=[]
# while i>=0:
#     rev+=[a[i]]
#     i-=1
# print(rev)
     

# # wap to arrange element in descending order
a=[3,2,10,12,7,4]
for i in range(1,len(a)):
    for j in range(1,len(a)):
       if a[j-1]<a[j]:
            a[j-1],a[j]=a[j],a[j-1]
print(a)
         
         

        


       




# # wap to print a amstrong number in the given range
a=[3,2,10,12,7,4]
temp=a
sum=0
count=len(a)
for i in range(1,a):
    while i!=0:
        rem=i%10
        sum=sum+rem**count
        i=i//10
if temp==sum:
    print('am')
else:
    print('not')

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




     

