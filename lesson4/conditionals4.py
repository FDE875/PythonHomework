import random
while True:
    number=random.randint(1,100)
    for attempt in range(50):
        a=int(input("Select number: "))
        if a> number:
            print("Too high")
        elif a<number:
            print("Too low")
        else:
            print("You guessed right!")
            break


    else:
        print("You guessed it right!")
        break
    answer=input("Play again? ")
    if answer not in [ 'Y', 'YES', 'y', 'yes', 'ok']:
        break