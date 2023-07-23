x = input("Enter your name:")
if (type(str(x)) is not str):
    print("You must enter letters")
elif (len(x)>12):
    print("Your name can't longer than 12")
elif (x[0].upper is not True):
    print("First letter must be capitalized")   
else:
    print(x)
    
y = input("Enter your age:") 
if (type(int(y)) is not int):
    print("You must enter numbers")
elif (len(y)>2):
    print("You can not enter longer than 2")
elif ("0"==y[0]):
    print("Age can not start with zero")  
else:
    print(y)  
    
z = input("Enter you number:")
if (type(int(z[0:3])) is not int):
    print("You must enter numbers")
elif (type(int(z[4:7])) is not int):
    print("You must enter numbers")  
elif (type(int(z[8:10])) is not int):
    print("You must enter numbers") 
elif (type(int(z[11:13])) is not int):
    print("You must enter numbers")           
elif (len(z)!=13):
    print("It can't longer or shorter than 13")
elif ("0"!=z[0]):
    print("Number must start with zero")
elif ("-"!=z[3] or "-"!=z[7] or "-"!=z[10]):
    print("You must enter -") 
elif ("55"!=z[1:3] or "50"!=z[1:3] or "51"!=z[1:3] or "70"!=z[1:3] or "77"!=z[1:3]):
    print("Your must enter Azerbaijan's phone code ")             
else:
    print(z)              
