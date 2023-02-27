

def fromatName(fName, lName):
    
    first1Name=fName[0].upper()+ fName[1:].lower()
    last1Name=lName[0].upper()+ lName[1:].lower()
    fullName = fName+lName
    return fullName

firstName=input("Enter Your First Name: ")
lastName=input("Enter your Last Name: ")
formatedName=fromatName(firstName, lastName)
print(f"Your name is {formatedName}")
