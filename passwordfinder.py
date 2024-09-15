import random

password = random.randint(1000,9999)
print(password)


guess = None

count = 0

for guess in range(1000,9999):
    count +=1
    if guess == password:
        print("Your password is Found:",guess)
        print(f"It takes {count} attempts")
        break

