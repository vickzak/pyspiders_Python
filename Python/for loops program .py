# 1.	wap to traverse through a string and print each character. 
# a='abrar'
# for i in a:
#     print(i,end=',')

# d = {'a':"hello", 'b':100, 'c':45.55, 'd':True}
# for rv in d:
#     print(d[rv])


# a='abrar'
# for i in a[::-1]:
#     print(i)
  
# d = {1:100,2:200,3:300,4:400}
# for i,j in enumerate(d):
    # print(j,end = " ")

# for i in d.keys():
#     print(i)


# for i in d.items():
#     print(i)

# for i in d.values():
#     print(i)

# 6.	wap to create a dictionary of characters and its ASCII value pair by taking string as input.
# a='abrar'
# d={}
# for i in a:
#     d[i]=ord(i)
# print(d)

# 7.	wap to create a dictionary of word and its length pair from a string(sentence).
# a = "python is an easiest programming language" 
# b=a.split()
# # print(b)
# d={}
# for i in b:
#     d[i]=len(i)
# print(d)

# 8.	wap to create a dictionary of index and character pairs of a string.
# a='abrar'
# d={}
# for i,j in enumerate(a):
#     d[i]=j
# print(d)
  
# 9.	wap to create a dictionary with word and its count pair from the given sentence. 
# a = "my day is good day or bad day or just a day"
# d={}
# for i in a:
#     d[i]=a.count(i)
# print(d)
 
#  10.	wap to count the number of characters in a string and create a dictionary with character and count pair
# 11.	wap to sort the characters of the string (alphabets followed by digits)
# a='hafeez2354667'
# b=[]
# for i in a:
#     if i in '123456789':
#         b.append(i)
#         i.sort()
#     else:
#         b.append(i)
#         i.sort()
# print(b)
    




# 11.	wap to sort the characters of the string (alphabets followed by digits)

# s = "app*3l@12$e"
# a=[]
# n=[]
# sp=[]
# for i in s:
#     if i.isalpha():
#         a.append(i)
#         a.sort()
#     elif i.isnumeric():
#         n.append(i)
#         n.sort()
#     else:
#         sp.append(i)
#         sp.sort()
# print("".join(a+n+sp))

# 12.	wap to print a character repeatedly as many times as mentioned in consecutive digit( i/p: a4b3c2   
# a='a4b3c2'
# for i in range(len(a)):
#     if i%2==1:
#         print(a[i-1]*int(a[i]) ,end='')


# 14.	wap to remove duplicate characters from the given string.
# a='abrar'
# d=[]
# for i in a:
#     if i not in d:
#         d.append(i)
# print(d)

# 15.	wap to find number of occurrences of each character present in the given string.
# a = "hello all how are you"
# d={}
# for i in a:
#     d[i]=a.count(i)
# print(d)

# 16.	wap to display unique vowels present inside the given string.
# s = "hello all how are you in india"
# d=[]
# for i in s:
#     if i in 'aeiou' and i not in d :
#         d.append(i)

# print(d)

# s = "hello all how are you in india"
# v = set()
# for i in s:
#     if i in "aeiouAEIOU":
#         v.add(i)
# print(v)

# 17.	wap to read a tuple from the user and print its sum and average.
# t = (10,"hi",25,67.7,86,9j,"hello",(1,2,3),[1,2,3])
# l=[]
# sum=0
# for i in t:
#     if isinstance(i,(int,float,complex,bool)):
#         l.append(i)
#         sum+=i


        
#         # print(sum)
# print(sum) 
# print(sum/len(l))  
        
# 19.	wap to read dictionary from user and find the sum of values if they are integer.
# d = {1:100,2:200,3:300,4:"hi",5:(1,2,3)}
# sum=0
# for i in d.values():
#     if isinstance(i,(int)):
#         sum+=i
# print(sum)

# 20.	write a program to create a dictionary to get only the duplicate items and the number of times the item is repeated in the list. 
# a=['apple',  'yahoo' ,'google', 'apple', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail']
# d={}
# l=[]
# for i in a:
#     if i not in l:
#         l.append(i)
#     else:
#         d[i]=a.count(i)

# print(d)

# 21.	wap to print fibonacci series from zero to nth number.
# a=0
# b=1
# n=20
# for i in range(n+1):
#     next=a+b
#     a=b
#     b=next
#     print(next)

# 23.	 wap to print prime numbers from 1 to 10.
# c=0
# for i in range(2,11):
#     for j in range(2,i+1):
#         if i%j==0:
#             c+=1
# if c==2:
#     print(i)

# num = int(input("enter a number"))
# for i in range(2,num+1):
#     if num % i == 0:
#         break
# else:
#     print(i,"its a prime number")


# a=int(input("enter range from 2 to : "))
# for i in range(2,a):
#     if i%2==0:
#         pass
#     else:
#         print(i)


# wap to demonstrate enumerate, reversed, zip and zip_longest with any iterable.
     
# str1 = "hello"
# str2 = "good"
# print(list(enumerate(str1)))
# print(tuple(enumerate(str2)))
# print(list(reversed(str1)))
# print(list(zip(str1,str2)))
# from itertools import zip_longest
# print(list(zip_longest(str1,str2)))
# print(list(zip_longest(str1,str2 ,fillvalue=5)))
# print(list(zip_longest(str1,str2 ,fillvalue='d')))

# 
# 26.	 wap to check the very first integer which is greater than 400 and print it. (demo of break keyword)
# l = [10,50,80,600,400,300,100]
# for i in l:
#     if i>400:
#         print(i)
#         break

# wap to print odd numbers 0 to 9 using continue keyword.(demo of continue keyword)
# for i in range(10):
#     if i%2==0:
#         continue
#     else:
#         print(i)

# 28.wap to demonstrate using of pass keyword.
# 29.wap to check whether the elements of list are lesser than 100 sing nested loops and loops with else block.
# l1 = [1000,20,30,40,50,60]
# for i in l1:
#     if i>=100:
#         print("greater value")
#         print(i)
#         break
       
# else:
#         print("valid values")

# 30.	 wap to print index and character of string in tuples.
# string = "hello world"
# # print(tuple(enumerate(string)))
# # for i,j in enumerate(string):
# #     print(i,j,end='')
# for item in enumerate(string):
#      print(item, end=" ")
 

# n = ("mom", "Komal", "pop", "nayan", "malayalam", "eye")
# d=[]
# for i in n:
#     if i==i[::-1]:
#         d.append(i.upper())
# print(d)

# names = ["gmail", "yahoo", "fb", "google", "gmail", "yahoo", "fb", "google", "yahoo", "fb"]
# res = []
# for i in names:
#     if i not in res:
#         res.append((i,names.count(i)))
# print(set(res))
    

# # wap to create a list of festival which are marked with holiday. i/p:
# h = {"Pongal":"Holiday","Ugadi":"No holiday","Navami":"Doubt","RepublicDay":"Holiday","SRatri":"Fasting"}
# l=[]
# for i in h.items():
#     if i[1]=='Holiday':
#         l.append(i[0])
# print(l)
 
# 44.	wap to create a list if the price if the product is more than 1000 then add the product name to a list.
# p = {"Asian-paint":4000, "Mobile":90000, "Hen":500, "Pen":5, "Watch":2500}
# l=[]
# for  i in p.items():
#     if i[1]>1000:
#         l.append(i[0])
# print(l)


# wap create a list, if a key is a individual DT then add key and data type as its value.
e = {10:"Ind", "hai":"Colle", [10]:"Colction", True:"Inddual", (11,22):"Colltion"} 
# l=[]
# for i in e.keys():
#     if isinstance(i,(int,float,bool,complex)):
#         l.append((i,type(i)))
# print(l)

# res = []
# for key in e:
#     if isinstance(key, (int, float, bool, complex)):
#         res.append((key, type(key)))
# print(res)


