import random
lst=["s","w","g"]
human_point=0
computer_point=0
print("-----SNAKE WATER GUN GAME------")
print("s for snake,w for water,g for gun")
for i in range(11):
    turn=input("s or w or g:")
    choice=random.choice(lst)
    #for turn="s"
    if turn=="s" and choice=="w":
        print("Human win")
        human_point+=1
    elif turn=="s" and choice=="g":
        print("Computer win")
        computer_point+=1
    #for turn="w"
    elif turn=="w" and choice=="g":
        print("Human win")
        human_point+=1
    elif turn=="w" and choice=="s":
        print("Computer win")
        computer_point+=1
    #for turn="g"
    elif turn=="g" and choice=="s":
        print("Human win")
        human_point+=1
    elif turn=="g" and choice=="w":
        print("Computer win")
        computer_point+=1
    #if both are equal
    elif turn==choice:
        print("TIE both get 0 point")

print("-------GAME OVER--------")
if human_point>computer_point:
    print("Human wins Computer loose")
else:
    print("Computer wins Human loose")
print(f"The human point is {human_point} & the computer point is {computer_point}")












