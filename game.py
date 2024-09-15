import random 

choices= {1:"Stone",2:"Paper",3:"Scissor"}

while(True):
    print("Choose your choice: ")
    print("1.Stone\n2.Paper\n3.Scissor")

    user = int(input("Your Choice: "))

    if user not in choices:
        print("Invalid Move.")
        continue

    computer = random.randint(1,3)

    print(f"Your choice is {choices[user]} and Computer hoice is {choices[computer]}")

    if(user==1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        print("You  won")
    elif(user == computer):
        print("Tie")
    else:
        print("You Lost")

    for_continue=input("Do you want to continue(yes/no)").lower()
    if for_continue == "yes":
        continue
    else:
        print("Exiting code")
        break    

