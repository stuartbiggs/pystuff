#global name

def getName():
    name = input("What is your name: ")
    return name

def getAge():
    age = input("Please enter your age: ")
    age1 = int(age)
    if age1 > 30:
        ageV = "old"
    else:
        ageV = "young"
    
    
    
    return ageV
    return age1


def displayInfo():
    name = getName()
    age = getAge()
    #ageV = getAge()
    print("Hello " + name)
    print("You are " + age)
    #print("You are " + ageV)

#getName()
displayInfo()
