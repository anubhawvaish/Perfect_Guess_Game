import random
target=random.randint(1,100)
attempts=0
while True:
    num=int(input("Enter your guess: "))
    if num==target:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif num<target:
        print("Too low! Try again.")
        attempts+=1
    else:
        print("Too high! Try again.")
        attempts+=1