import random
guess=random.randint(1,100)
gameover = False
b=1
while not gameover:
    guess1=int(input("guess the no"))
    if guess1==guess:
        print(f"you win in {b} times")
        gameover=True
    elif guess1 < guess:print("too less")
    else : print("too high")
    b+=1