
def add(x,y):
    return x+y 

def multiply(x,y):
    return x*y 

def subtract(x,y):
    return x-y 

def divide(x,y):
    if y==0:
        print("Can't divide with 0, Enter valid number.")
    else:
        return x/y        

while(True):
    x=float(input("Enter your number:-"))
    y=float(input("Enter your number:-"))
    print("Choose operation to perform :")
    print("1 for addition\n2 for subtraction\n3 for multiplication\n4 for divide")
    value= int(input("Enter your number:-"))
    if(value == 1):
        result=add(x,y)
        print(result)
    elif(value == 2):
        result=subtract(x,y)
        print(result)
    elif(value == 3):
        result=multiply(x,y)
        print(result)
    elif(value == 4):
        result=divide(x,y)
        print(result)
    else:
        print("Invalid input, Please enter valid Operation.")


    for_continue = input("Do you want to continue(yes/no)").lower() 
    if for_continue == "yes":
        continue
    else:
        print("Exiting program...")
        break   








