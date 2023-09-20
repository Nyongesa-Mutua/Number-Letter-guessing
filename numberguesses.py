#number guesses
import random
#counter for the while loop
counter = 10
# generating random number using already imported random
print("Welcome to this random numver guessing game.")
name = str(input("Enter your name"))
print("You have 10 chances to correctly guess a number randomly genetared by the computer.")
print("After every guess you will get feedbaCck from the machine informing me if it is is greater or less than the random number")
print(f"Good Luck!!{name}")



number = random.randint(1,100)
while counter>0:
    print("You have ",counter, "guesses")
    guess = (input("What is your guess?"))
    if guess is not int:
        print('The system requires an integer in its raw form.')
    else:
        if guess<number:
           print("It is less than the number")
        elif guess>number:
           print("Your guess is greater than the number in question.")
        else:
           print("You gussed it correct")
           break
        counter-=1
    