# if condition
# if condition: stmt1,stm2.......

# s=input("Enter a char")
# if s in 'aeiouAEIOU':print("vowel"),print("single char"),print("hello")


# if else condition:
# True stmt if condition else false stmt
# print('vowel','hii') if s in 'aeiouAEIUO' else print("consonant",'bye')


# print("hi"),print("vowel") if s in 'aeiouAEIOU' else print("consonant"),print("bye")
# the above statement executes all statement except true statement so put in one print stmt as above



# loop comprehension
# while is not possible as it needs incre or decr so assignment or incr or decr is not possible in comprehension



# for list comprehension

# s='hello all'
# for i in s:print(i)  #normal  for 
# res=[i for i in s if i in 'aeiou'] #   with if condition
# res=[i if i in 'aeiou' else None for i in s]  # with if condition and else
# print(res)



# dictionary comprehensions

# wap to create a dictionary of char and count pair
# s='hello'
# res={i:s.count(i) for i in s}
# print(res)


# wap to create a dictionary of charcarter with their index

# s='helloall'
# res={i:s[i] for i in range(len(s))}
# print(res)

# wap to create a dictionary  by reading a list check whether the list elemnents are even and numeric if yes assign position with value else reverse the value
# l=[10,55.5,6j,True,78,95,'hai',(1,2)]
# res={i:l[i] if isinstance(l[i],(int,float,bool)) and l[i]%2==0 else str(l[i])[::-1] if isinstance(l[i],(int,float,complex,bool)) else list(reversed(l[i]))  for i in range(len(l))}
# print(res)





# lambda or anonymus function
# by default expressions will return treu,false none

# wap to add 2 numbers
# r=lambda a,b:[a+b,a-b,a*b,a/b]
# print(r(5,10))


# wap to check a number is even or odd
# r=lambda a: a%2==0 
# print(r(4))

# r=lambda a: "even" if a%2==0 else "odd"
# print(r(4))


# wap to check char is vowel
# r=lambda a: "VOWEL" if a in 'aeiouAEIOU' else "consonant"
# print(r('a'))

# wap to check a number is perfect square or not
# r=lambda a:(round(a**0.5))**2==a
# print(r(9))


# wap to check a number is perfect cube
# r=lambda a:(round(a**0.33))**3==a
# print(r(27))

# wap to check whether te given word is palindrome if yes return word else return reverswed word
# r=lambda a:  a if a==a[::-1]  else  a[::-1]
# print(r('levela'))




#  using loops
# wap  to fetch all even number from 1 to 100
# r=lambda a:  [i for i in a if i%2==0]
# print(r(range(1,101)))



# wap  to fetch all odd number from 1 to 100
# r=lambda a:  [i for i in a if i%2!=0]
# print(r(range(1,101)))


# wap to fetch all vowels from given string
# r=lambda a:[ i for i in a if i in 'aeiou']
# print(r('abrarulhaq'))

# wap to fetch all even length words from a string
# r=lambda a:[ i for i in a.split() if len(i)%2==0 ]
# print(r('hi how are you'))







# wap to iter into a list check whether the elements are individual or collection if individual find first multiple else return as it is
# a=[10,'hi',(1,2,3),25.55,8j,[1,2,3],True,{1,2}]
# r=lambda a:[i*2 if isinstance(i,(int,float,complex,bool)) else i for i in a]
# print(r(a))
# note if first multiple given=i*2
# if self=i*1
# second multiple=i*3


# l1=[10,'hi',(1,2,3),25.55,8j,[1,2,3],True,{1,2}]
# l=[]
# for i in l1:
#     if isinstance(i,(int,float,complex,bool)):
#         l.append(i*2)
#         # print(i*2)
#     else:
#         l.append(i)
# print(l)





# wap to iter a string and create a dictionary of character and count pair
# r=lambda a:{ i:a.count(i) for i in a}
# print(r('abrar'))



# normal dict
# s="hello all"
# d={}
# for i in s:
#     d[i]=s.count(i)
# print(d)





# .....................Map function..........................

# a='hello'
# for i in a:
#     print(i)

# r=lambda a:[ i for i in a]
# print(r(a))

# # ..................same above using map............
# r=lambda i:i
# # print(map(r,a))#returns object
# print(list(map(r,a)))

# #..................map using normal function...............
# def r(i):
#     return i
# print(list(map(r,a)))




# example on using map lambda or normal

# wap to iter into a list check whether the elements are individual or collection if individual find first multiple else return as it is
# a=[10,'hi',(1,2,3),25.55,8j,[1,2,3],True,{1,2}]
# r=lambda i:i*2 if isinstance(i,(int,float,complex,bool)) else i
# print(list(map(r,a)))

# r=lambda a:[i*2 if isinstance(a,(int,float,complex,bool)) else a]
# print(r(a))



# normal form

# a=[10,'hi',(1,2,3),25.55,8j,[1,2,3],True,{1,2}]
# def r(i):
#     if isinstance(i,(int,float,complex,bool)):
#         return i*2
#     else:
#         return i
# print(list(map(r,a)))




# # # wap to iter into a list check whether the elements are individual or collection if individual find first multiple else return as it is
# # using map and filter
a=[10,'hi',(1,2,3),25.55,8j,[1,2,3],True,{1,2}]
r=lambda i: i*2 if isinstance(i,(int,float,complex,bool)) else i 
# r=lambda i:  isinstance(i,(int,float,complex,bool)) 
print(list(filter(r,a)))
# b=list(filter(r,a))
# c=lambda i:i*2
# # print(list(map(c,b)))
# # or
# print(list(map(lambda i:i*2,list(filter(r,a)))))



# wap to sort the list elements based on length

# names = ["steve", "eve", "adani", "bob", "birla", "ambani"]
# res = sorted(names, key=len)
# print(res)


#wap to return the key of a dictionary

# a = lambda key1 : key1.keys()
# print(list(a({1:"abc",2:"xyz",'b':"PQR"})))


# a = lambda key1 : key1.values()
# print(list(a({1:"abc"})))            


# names = ["steve", "ram", "tata", "shyam"]
# res = lambda item: [(names[item], len(names[item])) for item in range (0,len(names))]
# print(res(names))


# a=[10,5,6,7,1,8,2]

# def add(a):
#     for i in a:
#         for j in a:
#             if i+j==10 and i!=j:
#                 l=[]
#                 l.append(i)
#                 l.append(j) 
#                 print(l)           
# print(add(a))


# # wap to sort given list without using sort method
# l=[3,1,2,0,6,7,2]
# m=[]
# while(len(l)!=0):
#     min=l[0]
#     for i in range(1,len(l)):
#         if l[i]<min:
#             min=l[i]
#     for i in range(l.count(min)):
#         m.append(min)
#         l.remove(min)
# print(m)

# write a program to print which elements consecutive sum is 9 in list consecutive numbers
# a=[5,5,7,7,8,9]
# for i in range(len(a)-1):
#     if a[i]+a[i+1]==10:
#         print(a[i],a[i+1])


# wap to reverse a name
# def rev(a):
#     print(a[::-1])
#     print(list(reversed(a)))
# rev('abrar')

# def rev(a):
#     b=(len(a)-1)
#     while b>=0:
#         print(a[b])
#         b-=1  
# rev('abrarulhaq')



# # wap to print perfect square from given range
# a=int(input("enter a number"))
# for i in range(1,a+1):
#     if (round(i**0.5)**2)==i:
#         print(i,"prime")
#     else:
#         print(i,"none")

# wap to print  prime numbers
# num=int(input("Enter a number"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"{num} is  not prime")
#         break
# else:
#     print(f"{num} is prime")

# num=int(input("Enter a number"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"{num} is  not prime")
#         break
        
# else:
# #     print(f"{num} is prime")
# n=10
# c=0
# for i in range(1,n+1):
#      for j in range(1,n+1):
#           if i%j==0:
#                c+=1
# if c==2:
#        print(i)


    

# #wap to find square or cube of given number
# sq=lambda n1 :(n1**2,n1**3)
# print(sq(4))

# wap to check the given number is palindrome or not
# r=lambda a : a==a[::-1] 
# print(r('121'))

#wap to convert negative number to positive number
# r=lambda a:abs(a)
# print(r(-2))

# #wap to return the key of a dictionary
# r=lambda a:{ i:a.count(i) for i in a}
# print(r('anrarr'))
# r=lambda a:a.keys()
# print(r({'a':1,'b':2}))

# l = ["nayana", "kayak", "mom", "school", "bag", "dad"]
# r=lambda a:[ i for i in l  if i==i[::-1]]
# print(r(l))

#wap to fetch list element and return it with its length pair

# l = ["steve", "ram", "tata", "shyam"]
# r=lambda a:[  len(i) for i in l]
# print(r(l))

#wap to print the numbers present in a list with their corresponding indices pair

# l = [100,200,300,400,500,600]
# r=lambda a:[ (l[i],i) for i in range(len(l))]
# print(r(l))

# using map and lambda
# #wap to check list elements are palindrome or not
# l = ["nayana", "kayak", "mom", "school", "bag", "dad"]
# r=lambda i:  i==i[::-1] 
# print(list(map(r,l)))

# #wap to return a list of even numbers
# l = [1, 2, 3, 4, 5, 6]
# r =lambda a: a%2==0 
# print(list(map(r,l)))

# #wap to find the replica of each character from the given string.
# ss = "hello all"
# a= "hello"
# r=lambda i:i+i
# print(list(map(r,a)))


# # #wap to return only list with positive integers.
# l =[25,-87,-75,99,45.5,-34, -67.77]
# r=lambda i: abs(i) if isinstance(i,(int)) else abs(int(i))
# print(list(map(r,l)))


#wap to add 2 lists( need to add corresponding values of elements with similar index value)
# l1 = [34,67,44,99,10]
# l2 = [10,20,30,40]

# r =lambda a,b: []
# print(list(map(r,(l1,l2))))
# l1 = [34,67,44,99,10]
# l2 = [10,20,30,40]
# l3 = [10,30,50,70]
# add = map(lambda l,s1_l,s2_l : l+ s1_l+s2_l, l1, l2, l3)
# print(list(add))
