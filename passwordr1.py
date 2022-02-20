
userNames = ["Genevievee","Joseph", "David", "Ronaldo", "John"]


passwords = ["G&32", "W@12", "%&34", "3(@w", "84#1"]


name = str(input("Enter Your First name: "))


if (name in userNames):
    index = userNames.index(name)
    print("Hello, "+ name + "! The password is : "+ passwords[index])
else:
    print("Hello,"+ name + "! See you later.")



