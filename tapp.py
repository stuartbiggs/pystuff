#global name

def getName():
    name = input("What is your name: ")
    return name

def getAge():
    age = input("Please enter your age:")
    return age



def displayInfo():
    name = getName()
    age = getAge()
    print("hello " + name)
    print("Your age is :" + age)


#getName()
displayInfo()
