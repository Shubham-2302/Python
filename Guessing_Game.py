import random
import logging
import math

log = logging.Logger(name = "Game_Logger",level = logging.DEBUG)

def validate_input(input)->bool:
    try:
        check  = float(int(input))
        if check.is_integer:
            return int(input)
    except ValueError as ve:    
        if "invalid literal for int() with base 10" in str(ve):
            print("Madar yeh sahi number dikh raha hain teko Lodu \n")
        else:
            print("Error:", ve)
        log.critical(f"Error {ve}")
        # print("Madar yeh sahi number dikh raha hain teko Lodu")
        return None


#Taking inputs
lower = int(input("Enter a lower bound for the number :- "))
upper = int(input("Enter a upper bound for the number :- "))

answer = random.randint(lower,upper)
limit = round(math.log((upper-lower),2)+1)
log.debug(" Computer can gues the number in {} guesses ".format(limit))
log.debug("Let's see how many guess it takes you to do it?")

#Guessing and checking
count=0
strike = 0

while(count<=limit):
    number = (input("Guess a number"))
    number = validate_input(number)
    # print(game)
    if (number is None):
        print("dhat teri maa ki")
        break
    
    count +=1


    print("Checking .........")

    if(answer == number):
        print("Damn you are good at it",f" \t You took {count} tries")
        break
    elif(number < answer and number>lower):
        print("guess too small")
    elif(number > answer and number<upper):
        print("guess too big")
    elif(number > 0 and (number>upper or number < lower)):
        log.warning("Watch your guesses man")
    elif(number<0):
        log.error("Invalid Number man")
        strike +=1
        print("3 strikes and you are out, Current Strike %d",strike)
    elif(type(number)!=int):
        log.critical("Tu ghar ja tere liye hain hi nahin yeh game")



        

print(f" the number was {answer}")


        
        