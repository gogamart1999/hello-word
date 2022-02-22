# def my_function():
# 	return"hello word"
# print(my_function())

# def my_dif():
# 	lst=[1,1,2,5]
# print(my_dif())

# def square_value(num):
# 	return num**2
# print(square_value(2))
# print(square_value(-4))
# # print(square_value(6))

# def my_function(name):
# 	print("my name is",name)
# # print(my_function("Jon"))
# my_function("Jane")

# def add(a,b):#paramet
# 	return a+b
# print(add(5,4))#argument

# def my_function(fname,lname):
# 	print(fname+""+lname)
# my_function("mail")
# error

# def myfunction():
# 	# global x
# 	x="hello"
# myfunction()
# print(x)

# def myfunc():
# 	x=300
# 	# print(x)
# myfunc()
# # print(x)

# def myfunc1():
# 	x="john"
# 	def myfunc2():
# 		nonlocal x
# 		x="hello"
# 	myfunc2()
# 	return x
# print(myfunc1())
# Write a python function to sum all the numbers in a list.
# 1
# def my_function():
# 	mylist=[8,2,3,0,7]
# 	s=0
# 	for i in mylist:
# 		s+=i
# 	return s
# print(my_function())

# #1-2
# def summary(lst):
# 	n=0
# 	for i in lst:
# 		n+=i
# 	return n
# print(summary([8,2,3,0,7]))

 # 2 Write a pyhton function to check whether a number is in a given range

# def my_function(a,b,num):
# 	if num>a and num>b:
# 		print("yes")
# 	else:
# 		print("no")
# my_function(80,5,9)

# 3 write a python function that accepts a string and calculate the number of upper case letters and lower case letters
# def my_function(my_string):
# 	srt1=0
# 	srt2=0
# 	for i in my_string:
# 		if i.isupper():
# 			srt1+=1
# 		elif i.islower():
# 			srt2+=1
# 	return srt1,srt2
# print(my_function("The quick Brown Fox"))

# 4 write a python function that takes a list and returns a new list writh unique elements of the first list.

# def my_function(my_list):
# 	n=[]
# 	for i in my_list:
# 		if i not in n:
# 			n.append(i)
# 	return n
# print(my_function([1,5,5,6,7,7]))

#5 write a python program to print the even numbers from a given list. sample list:[1,2,3,4,5,6,7,8,9]

# def my_function(my_list):
# 	for i in my_list:
# 		if  i % 2 == 0:  
# 			print(i)
# my_function([1,2,3,4,5,6,7,8,9])


# def students(*args):
# 	print(args)
# students("GO","OG","le")
# def my_sum(*args):
# 	result=0
# 	for x in args:
# 		result+=x
#     return result
# print()

# def concatenate(**kwargs):
#  	result=""
#  	for arg in kwargs.values():
#  		result+=arg
#  	return result
# print(concatenate(a="A",b="B",c="C"))

