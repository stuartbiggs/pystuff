#global name

def getName():
    name = input("What is your name: ")
    return name

def displayName():
    name = getName()
    print("hello " + name)

#getName()
displayName()
