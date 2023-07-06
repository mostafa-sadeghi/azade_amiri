# print("hello world")


# x = 1

# نام متغیر می تواند هر ترکیبی از کاراکترهای الفبایی انگلیسی، آندراسکور و اعداد باشد با
# این استثنا که اولین کاراکتر نمی تواند عدد باشد

# name1 = 1 # ok
# name_1 = 1 # ok
# _name_1 = 2 # ok

# 1name = 2 # error
# name one = 12 # error

# name_one = 12 # snake case
# nameOne = 12 # cammel case


# x = 1
# print(type(x))

# x = 1.2
# print(type(x))

# z = 1  + 2j
# print(type(z))


# x = "sara"
# print(type(x))


# x:int = 2
# print(x)

# x = True
# print(type(x))
# x = False
# print(type(x))

# string1 = ""

# print(type(string1))
# string2 = ''
# print(type(string2))


# message = 'he said "some thing"'
# print(message)

# message = "he said \"some thing\""
# print(message)

# message = "hello. \nwelcome to python class."
# print(message)
# message = """hello. 
# welcome to python class."""
# print(message)
# message = '''hello. 
# welcome to python class.'''
# print(message)


# message = "hello"
# print(message[0], end=" ")
# print(message[1], end=" ")
# print(message[2], end=" ")
# print(message[3], end=" ")
# print(message[4])
# print(message[5]) # error
# print(len(message))
# print(message[len(message) - 1])
# print(message[-1])
# print(message[:3])
# print(message[:])

# print(message[-1])
# print(message[-2])


# message = "hello"
# print(message[2:])
# print(message[2:5])
# print(message[::2])

# print(message[::-1])

# name = input("enter a name: ")
# print("hello", name)
# family = input("enter your family: ")
# print("hello"+ " " + name)
# print(type(name))
# message = "Hello %s %s"%(name, family)

# message = f"Hello {name} {family}"
# print(message)

# print("hello", name, family)




# number1 = int(input("enter first number: "))
# number2 = float(input("enter second number: "))

# result = number1 + number2

# print("result is:", result)


# print(4 % 2)
# print(5 % 2)

# print(3 > 4)
# print(5 > 4)

# z = 3 > 4  #        >=     <=    ==   !=   >   <
# print(type(z))

# number1 = int(input("enter first number: "))
# number2 = float(input("enter second number: "))


# if number1 > number2:
#     print("number1 is greater")
#     print("ok")

# else:
#     print("number2 is greater")



# number1 = int(input("enter first number: "))
# number2 = float(input("enter second number: "))
# number3 = float(input("enter second number: "))
# max_number = max(number1, number2, number3)
# print(f"max number is: {max_number}")



# print("hi " * 5)


# shopping = [1, "ali", [1,2,3,4,5], [[1,2], ['a']]]
# print(type(shopping))

# print(shopping[3][0][0])

shopping_list = ["item1", "item2", "item3"]
shopping_list[0] = "item0"
print(shopping_list)


list2 = ["bbbb", "aaaa"]

# result = shopping_list + list2
# print(result)

shopping_list.extend(list2)
print(shopping_list)
shopping_list.append(list2)
print(shopping_list)




# shopping_list.append("item4")
# print(shopping_list)

# del shopping_list[0]
# print(shopping_list)

# shopping_list.remove("item3")
# print(shopping_list)

# shopping_list.pop(0)
# print(shopping_list)
