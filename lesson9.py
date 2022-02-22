# l=[1,2,3]
# for i in l:
# 	print(i)
# k=[i for i in l]
# print(k)

# d={"a":10,"b":10}
# dict2={k:v for k,v in d.items()}
# print(dict2)

# n=int(input("Enter a number:"))
# x={x:x*x for x in range(1,n+1)}
# print(x)


# list1=[1,2,3,5,]
# my_dict={}
# for i in list1:
# 	my_dict[1]=i*i
# print(my_dict)


# 6)Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

#1
# my_list=[1,2,3,5,6,7]
# my_list.clear()
# print(my_list)

# #2
# my_string="hello word"
# count={}
# for i in my_string:
# 	if i==" ":
# 		continue
# 	count[i]=my_string.count(i)
# print(count)

# # 3
# n=1
# n=int(input())
# while True:
# 	if n<18:
# 		print("No")
# 		n=int(input())
# 	else:
# 		print("Yes")
# 		break

# Write a python program to combine values in python list of dictionaries.
my_list=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item2','amount':750}]
counter=()
for i in my_list:
	if 