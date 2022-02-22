# # import random
# # def my_function():
# # 	n=random.randint(1,10)
# # 	i=0
# # 	while True:
# # 		s=int(input())
# # 		if s>n:
# # 			print("too high")
# # 		elif s<n:
# # 			print("too low")
# # 		else:
# # 			print("you win")
# # 			break
# # my_function()

# def my_function():
# 	n=6
# 	for i in range(1,n+1):
# 		if n%i==0:
# 			print(i)
# my_function()

# def my_function(my_list):
# 	maximum=my_list[0]
# 	for i in my_list:
# 		if i>maximum:
# 			maximum=1
# 	return maximum
# print(my_function([1,5,6,8]))

# my_func=lambda a:a+10
# print(my_func(5))


# my_func=lambda a,b:a*b
# print(my_func(5,6))
# print(type(x))

# def testfunc(num):
# 	return lambda x:x*num
# resulf=testfunc(10)
# print(resulf(9))

# map(function,iterable)
# def square(n):
# 	return n*n 
# numbers=(1,2,3,4,5)
# result=map(square,numbers)
# print(list(result))

# numbers=(1,2,3,4,5)
# result=map(lambda x:x*x,numbers)
# print(list(result))

# def is_even(n):
# 	return n%2==0
# nums=[2,5,6,8,7]
# evens=list(filter(is_even,nums))
# print(evens)

# def is_even(n):
# 	return n%2==0
# nums=[2,5,6,8,7]
# evens=list(map(is_even,nums))
# print(evens)

# my_list=[12,65,54,39]
# result=list(filter(lambda x:x%2==0,my_list))
# print(result)

# y=filter(lambda x: x%3==0,[1,2,3,4,12,9])
# print(list(y))

# 1 Write a python program to create a lambda  that adds 15 to a given number passed in as an argument,also create a lambda function that multipplies argument x with argument x with argument y and print the result/

# n=lambda x:x+15
# print(n(10))
# n=lambda x,y:x*y
# print(n(10,15))

# 2 write a python program to square and cube every number in a given list of in a given list of integers usin Lambda.

# numbers=(1,2,3,4,5)
# result1=map(lambda x:x*x,numbers)
# print(list(result1))
# result2=map(lambda x:x**3,numbers)
# print(list(result2))

# 3 write a python program to find if a given string start with a uppercase character using Lambda.
# n="Go oG LE"
## s=list(filter(lambda x:x.isupper(),n))
## print(s)
# str=lambda x:x if x[0].istitle() else False
# print(str('Python goo'))
# 4 write a python program to count the even,odd numbers in a given array of intergers using lambda
## a=[1,5,6,8,11,2,15]
##b=len(list(filter(lambda x:x%2 !=0,a)))
## c=len(list(filter(lambda x:x%2 ==0,a)))
## print(b)
##print(c)

# l1=[2,4,8,9,7]
# even=filter(lambda x:x if x%2==0 else False,l1 )
# even1=filter(lambda x:x if x%2!=0 else False,l1 )
# print(list(even))
# print(list(even1))

# 5 Write a python program to find intersection of two given arrays using lambda.
# original arrays:
# [1,2,3,4,5,6,7,8,9,10]
# [1,2,4,8,9]
# intersection of the said a [1,2,8,9]

# list1=[1,2,3,5,6,7,8,9,10]
# list2=[1,2,4,8,9]
# list3=list(filter(lambda x:x in list1,list2))
# print(list3)

# Write a Python program to add two given lists using map and lambda. Go to the editor
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]

# a=[1, 2, 3]
# b=[4, 5, 6]
# c=list(map(lambda x,y:x+y,a,b))
# print(c) 

# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function. Go to the editor
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48

# my_list=[2, 4, -6, -9, 11, -12, 14, -5, 17]
# my_list1=list(filter(lambda ))