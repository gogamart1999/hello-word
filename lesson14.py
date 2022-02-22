# f=open("text.txt","r")
# print(f.read())

# f=open("text.txt","r")
# print(f.read(5))


# f=open("text.txt","r")
# # print(f.readline())
# print(f.readlines())
# f.close()


# f=open("text.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# f=open("demofile.txt","r")
# print(f.readline())
# f.close()

# f = open("text.txt", "r+")
# f.write("Now the file has more content!")
# f.close()
# f = open("text.txt", "r")
# print(f.read())
# f.close()

with open ('text.txt','a+') as file:
	file.write('hello word!')
	file.seek(0)
	print(file.read())
# print(file.closed)


# # 
# try:
# 	print(x)
# # except:
# # 	print("Mam ma mia")

# # print(x)
# # print("Mam ma mia")

# except Exception as e:
# 	print(e)

# try:
# 	print(x)
# except NameError:
# 	print("Var x is not cefined")
# except:
# 	print("Som else ernt cefined")


# try:
# 	print("Hel")
# except:
# 	print("Var x is not cefined")
# else:
# 	print("Som else ernt cefined")


# misht ashxatox
# try:
# 	print(x)
# except :
# 	print("Var x is not cefined")
# finally:
# 	print("Som else ernt cefined")

# write a python program to read the whole text of a file and catch the error if files does not exists
# try:
# 	f=open("8text.txt","r")
# except:
# 	print("file is not defiend")

# writhe a python program to cathe error a nume dividing by zero.

# try:
# 	print(15/0)
# except:
# 	print("zero defiend")


# mylist=[1,2,3]
# mystring="hello"
# try:
# 	print(mylist+mystring)
# except:
# 	print("error")


# x=-1
# if x<0:
# 	raise Exception("Sorry,no numbers below zero")

# x="hello"
# if not type(x) is int:
# 	raise TypeError("Only integers are allowed")
# min=6
# max=16



# password=input("Plase enter password")
# if not(len(password)<6 and len(password)>16):
# 	raise Exception("error")

# password=input("Plase enter password")
# count1=count2=0
# if len(password)<6 and len(password)>16:
# 	raise Exception("ok")
# for i in password:
# 	if i.isupper():
# 		count1+=1
# 	if i.isdigit():
# 		count2+=1
# if count1<1 or count2<1:
# 	raise Exception("erro")
# else:
# 	print("Your password is valid")


