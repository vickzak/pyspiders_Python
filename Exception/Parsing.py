
# json technique 1.dumps,2.loads
# import json
# data=eval(input('enter'))
# print('before',type(data))
# enc=json.dumps(data)
# print('after',type(enc))
# with open('file2.txt','w') as a:
#     a.write(enc)
# with open('file2.txt','r') as a:
#     b=a.read()
#     print(b,type(b))
#     dec=json.loads(b)
#     print(dec,type(dec))


# pickle technique 1.dumps ,2.loads wb(write binary),rb(read binary)
# import pickle
# data=eval(input('enter'))
# print('before',type(data))
# enc=pickle.dumps(data)
# print('after',type(enc))
# with open('file3.txt','wb') as a:
#     a.write(enc)
# with open('file3.txt','rb') as a:
#     b=a.read()
#     print(b,type(b))
#     dec=pickle.loads(b)
#     print(dec,type(dec))

# note 
# in pickle 4 m3thods
# 1.a load:pkl obj -> py obj
# 1.b dump: py obj -> pkl obj
# 2.a loads
# 2.b dumps


# if we want serilized data we use dumps

# dumps->python file to pickle file



# 2



# # to convert python object to binary use pickle
# from pickle import *
# l=[10,2.3,2+8j,True,[1,2,3,3],(3,4,5,6),{4,6,6,},'hello all',{'a':10,'b':20}]
# for i in l:
#     j=dumps(i)
#     print(j) # converts to binary 
#     print(loads(j))



# # # for python object conversion use dumps,loads
# import os
# p=r"C:\Users\abrar ul haq\Desktop\Grooming"
# os.chdir(p)
# with open('data.txt','r') as obj:
#     robj=obj.read()
#     b=dumps(robj)
# #     # print(robj)
#     print(loads(b))

# # converting whole file to byte using dump,load
# # note for file converion use dump
# with open('d1.pkl','wb') as obj:
#     dump(robj,obj)
# with open('d1.pkl','rb') as obj:
#     load(obj)






# complete pickle check here
# from pickle import *
# # python objects
# l=[10,15.5,8j,True,'hello',(1,2,3),[1,3,4],{66,77,88,77},{'a':100,'b':200}]
# pkl=[]
# for i in l:
#     pkl.append(dumps(i))
# print(pkl)

# # for i in pkl:
# #     print(loads(i))



# # 1.from text to python  and python to pkl
# import os
# p=r'C:\Users\abrar ul haq\Desktop\Grooming'
# os .chdir(p)
# with open('haf.txt','r') as obj:
#     # print(obj.read())
#     pobj=obj.read() #python object

# # creating pickle file
# with open("h1.pkl",'wb') as obj:
#     dump(pobj,obj)




# # form pickle to python and python to text
# with open('h1.pkl','rb') as obj:
#     pobj=load(obj)

# with open('result.txt','w') as obj:
#     obj.write(pobj)





# json format
# from json import *
# l=[10,15.5,8j,True,'hello',(1,2,3),[1,3,4],{66,77,88,77},{'a':100,'b':200}]
# json=[]
# for i in l:
#     json.append(dumps(i)) #here in json it does not support set and complex so first conver it  to string 
# print(json)



# python objects to json

# l=[10,15.5,8j,True,'hello',(1,2,3),[1,3,4],{66,77,88,77},{'a':100,'b':200}]
# json=[]
# for i in l:
#     if isinstance(i,(set,complex)):
#         json.append(dumps(str(i)))
#     else:
#         json.append(dumps(i))
# print(json)

# json to python obj
# for i in json:
#     print(loads(i))



# json file form text to python and python to json
# with open('haf.txt','r') as obj:
#     pobj=obj.read() #python object
#     # print(pobj)
# with open('j1.json','w') as obj:
#     dump(pobj,obj)

# # from json to python and python to text
# with open('j1.json','r') as obj:
#     # print(obj.read())
#     jsonres=load(obj) #python obj
# with open('jsonres.txt','w') as obj:
#     obj.write(jsonres)


   










