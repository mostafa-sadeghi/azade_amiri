# numbers = [1, 2 ,"ali"]

# numbers[0] = 10000
# print(numbers)


# numbers = (1, 2, 3)
# print(type(numbers))

# numbers[0] = 1000  # error


# favorite_sports = {
#     'sara': 'football',
#     'artin': 'tennis',
#     'armin': 'football'
# }

# print(favorite_sports)
# print(f"sara likes {favorite_sports['sara']}")

# name = input("enter a name: ")
# sport = input("enter your favorite sport's name: ")

# favorite_sports[name] = sport
# print(favorite_sports)


# favorite_sports1 = {
#     'sara': 'football',
#     'artin': 'tennis',
#     'armin': 'football'
# }
# favorite_sports2 = {
#     'artin': 'tennis',
#     'sara': 'football',
#     'armin': 'football'
# }


# print(favorite_sports1 == favorite_sports2)


# list1 = [1,2,3]
# list2 = [3,2,1]

# print(list1 == list2)


# favorite_sports = {
#     'sara': 'football',
#     'artin': 'tennis',
#     'armin': 'football'
# }


# del favorite_sports['armin']

# print(favorite_sports)


# a = 12
# b = 5
# c = 333

# if a > b and a > c:
#     print(f"{a} is the greatest.")

# elif b > c and b > a:
#     print(f"{b} is the greatest.")

# else:
#     print(f"{c} is the greatest.")


# print("user" and 1)
# print(1==1 and "user")
# print(1==1 and "user" and "pass")
# print(False or "user")
# print("user" or False)


# for i in range(3):
#     print(i)


# for i in range(3):
#     print("blalallall")


# total = 0
# for i in range(3):
#     number = int(input("enter a number: "))
#     total += number
# print(total)
# print(i)


# for s in "python":
#     print(s.upper(), end=" ")


# total = 0
# for number in [1,2,3,4,5,6,88]:
#     if number % 2 ==0:
#         total += number

# print(total)


# my_list = ["p", "y","t","h", "o","n"]
# res = ""
# for char in my_list:
#     res += char.upper()

# print(res)

# res = ""
# for i in range(len(my_list)):
#     res += my_list[i].upper()

# print(res)


# my_list = ["p", "y", "t", "h", "o", "n"]
# res = ""
# for item in enumerate(my_list):
#     print(item[0], item[1])

# for index, value in enumerate(my_list):
#     print(index, value)


# i = 0
# while i < 5:
#     print("blalalal")
#     i += 1


import turtle

screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(600, 600)
screen.title("my game")


turtle1 = turtle.Turtle()
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
turtle1.shape("turtle")
turtle1.shapesize(2, 2)
turtle1.color("red", "green")
turtle1.pensize(5)
turtle1.begin_fill()
turtle1.speed("fastest")
for i in range(4):
    turtle1.forward(100)
    turtle1.left(90)
turtle1.end_fill()
turtle1.hideturtle()

turtle1.penup()
turtle1.goto(0, 260)
turtle1.write("BALLALALALAL", align="center", font=("arial", 22))


turtle.done()
