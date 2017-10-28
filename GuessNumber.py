import random
computerRandomNo = random.randint(0,100)
print computerRandomNo

while True: # This will run the program in loop for ever.
    humanEnterNO = int(input("Enter the Number between 1 to 100 :"))
    #humanEnterNO = int(humanEnterNO)
    if humanEnterNO in range(0,100):
        if  computerRandomNo > humanEnterNO:
            print("Guess a higher number :")
        elif computerRandomNo < humanEnterNO:
            print("Guess a lower number :")
        else:
            print("Wohh you have guessed the number right ..")
            break  # This will break the while loop if the condition is true.
    else:
        print("The number is not in range .Please enter the number again")
