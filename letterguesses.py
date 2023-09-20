import random

letters = "abcdefghijklmnopqrstuvwxyz"
b = len(letters)
print(b)
print("This is a letter guessing game.")
print("The computer guesses a random.")
print("It gives you a hint whether the letter you have guessed prevously is before or after the subject letter in the english alphabetical system.")
print("The hints are warmer or colder based on their postion with a being coldest and z being warmest.")
print("You have 4 chances to guess correctly.")
 
counter = 4
subject = random.choice(letters)
subInd = letters.index(subject,0,26)
while counter>0:
    print(f"You have{counter}guesses.")
    ans = str(input('Enter your guess')).lower() 
    ansInd= letters.index(ans,0,26)
    if subInd<ansInd:
        print("Colder")
        
    elif subInd>ansInd:
        print("Warmer")
    else:
        print("You guessed correctly")
    counter-=1
    
    
