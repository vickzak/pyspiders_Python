# #lists

# a=[10,20,30,'cta','dog','mouse','apple','mango']
# # a.insert(5,'hafeez')//inserting at aparticular position
# # a.append('cta')//inserting at last
# # a.remove('cta')//removing a element ,if it has similar values it removes the first occurence
# # a[3]=40//updating a value
# print(a)


# #set
# a={2,3,4,5,'q','red','apple','apple'}
# # print(a)
# a.add('mango')
# # print(a)
# a.remove('apple')
# print(a)
# print(type(a))

# b={}
# print(type(b))

# c=set()
# print(type(c))




#dictionary

# dict={'name':'abrar','age':33}
# print(dict)

# dict={'name':'abrar','age':33,'name':'hafeez'}#dictionary does not accept same key values but it will accept the recent one
# # print(dict)
# dict={'name':'abrar','age1':33,'age2':33}#accepts duplicate values
# print(dict)
# #adding new data
# dict['place']='bengaluru'
# print(dict)
# #updating the data
# dict['name']='hafeez'
# print(dict)
# #deleting the data
# del dict['name']# as keys are not duplicate so its not necesssary to give values as well
# print(dict)

# dict1={'name':'abrar','age':33,'age':45}
# del dict1['age']
# print(dict1)



#typecasting

# a=100
# print(type(a)) done
# print(float(a)) done
# print(bool(a))#for positive number its always true for 0 its false done
# print(complex(a)) done
# print(str(a)) done
# print(list(a)) error
# print(tuple(a))errror
#print(set(a)) error
# print(dict(a)) error



# a=9.9
# print(type(a))done
# print(int(a))done
# print(bool(a))#for positive number its always true for 0 its false done
# print(complex(a)) done
# print(str(a))done
# print(list(a)) error
# print(tuple(a))error
#print(set(a)) error
# print(dict(a))erroe


# a='abrar'
# print(type(a))done
# print(int(a))error
# print(bool(a))#for full string  its always true for 0empty string its false done
# print(complex(a)) #error
# print(list(a)) #done[a,b,r,a,r]
# print(tuple(a)) #done(a,b,r,a,r)
# print(set(a)) # done{b,a,r}
# print(dict(a)) # error


# a=True
# print(type(a)) 
# print(float(a))# 1.0 
# print(int(a)) #1
# print(complex(a))  #(1+0j) done
# print(list(a)) #error
# print(tuple(a)) #error 
# print(set(a)) error
# print(dict(a)) #error


# a=10+5j
# print(type(a)) 
# print(int(a)) #error
# print(float(a)) #error
# print(bool(a)) #true
# print(str(a)) #true 
# print(list(a)) #error
# print(tuple(a)) #error
# print(set(a))
# print(dict(a)) #error


# a=['aa',2,3]
# print(bool(a)) #true
# print(str(a)) # string  happens 
# print(list(a)) 
# print(tuple(a)) #tuple happens
# print(set(a)) #set happens
# print(dict(a)) #error


# a=('aa',3,5)
# print(bool(a)) #true
# print(str(a)) #done 
# print(list(a)) #done
# print(set(a)) # done
# print(dict(a)) #error


# a={'aa',2,3}
# print(bool(a)) #true
# print(str(a)) #done
# print(list(a)) #done
# print(tuple(a)) #done
# print(dict(a)) #error

# a={'name':'anu','age':22,'place':'bangalore'}
# print(len(str(a)))


# control statements

# 1.condtional statements

# a=10
# b=45
# if a==b:
#     print('a is equal to b')
# print('not equal')


# a=10
# b=45
# if a<b:
#     print('a is less than  b')
# print('not less')

# a=67
# b=4
# if a%b==1:
#     print(' a and b is odd',a)
# print(a,b,'are not odd')


# # if -else

# a=int(input('enter first number'))
# b=int(input('enter second number'))
# if a%b==0:
#     print(a,'and',b,'are even')
# else:
#      print(a,'and',b,'are  not even')
# print('operation complete')



# elif

# a=int(input('Enter a number'))
# if a>0:
#     print('number is positive')
# elif a<0:
#     print('number is neagtive')

# else:
#     print(' number is neutral')


# nestedif
# a=input('enter  your city')
# b=input('enter your state')
# if a=='Bangalore':
#     if b=='karnataka':
#          print('Welcome to IT hub of India')
#     else:
#         print(b,'is not the IT hub of india')
# else:
#     print('sorry not the IT capital city')




# for loopa
# a=[1,2,3,4,5,6,7,8,9]
# for i in a:
#     print(i)  


# for a in range(2,11,2):
    # print(a)

# for a in range(5):
#     print(a)

# for a in range(1,101,1):
#     print(a)



# while loop

# n=1
# while n<=5:
#     print(n)
#     n+=1

# transfer statement

# break

# for i in range(5):
#     if i==3:
#         break
#     print(i)


# i=1
# while i<=6:
#     i+=1
#     if i<=5:
#         continue
#     print(i)

 







