# This is a choose your own adventur game
from function import *
import random
import os
import time


print("Welcome to The game")
while True:
    play = input("Press Enter to continue: ")

    if play == '':
        break

name = (input("Enter name: ")).capitalize()
print(f"Welcome {name} into the Champion Island")
print("Loaggin",end = '')
load("...............",0.05)
time.sleep(2.5)
os.system('cls')

story_part("story.txt" , 2,6)

print()
while True:
    answer = (input("Enter: ")).lower()
    if answer == 'yes':
        print(f"Welcome to the Comptition, {name}")
        break
    
    elif answer == 'no':
        print(f"Thx for playing {name}.")
        quit()
    
    else:
        print("Invalid Input")
        continue

print("Loading " , end = '')
load(".............",0.05)
load("..............")
time.sleep(2.5)
os.system('cls')


story_part("story.txt", 9,11)

while True:
    answer = (input("Enter ('q' for quit): ")).lower()
    if answer == 'yes':
        print("    ")
        typewriter(f"Welcome to Compition {name}")
        break
    
    elif answer == 'no':
        print(f"{name} you should play the Games are not over")
        continue
    
    elif answer == 'q':
        quit()

    else:
        print("Invalid Input")
        continue

load(".........",0.05)
load(".........")
time.sleep(2.5)
os.system('cls')

typewriter(f"This is a Enterence test {name},\nto check wheather you are ready or not!")
load(".........")
load("Level 0: ")
time.sleep(2.5)
os.system('cls')


# Rock,Paper,Scissors

story_part("story.txt",14,19)


time.sleep(1)
os.system('cls')
while True:
    answer = (input("Enter ('q' for quit): ")).lower()
    if answer == 'yes':
        break
    
    elif answer == 'no':
        print(f"Hattori is Wating for you?")
        continue
    
    elif answer == 'q':
        quit()

    else:
        print("Invalid Input")
        continue


print("Loading " , end = '')
load(".............")

option = ['rock','paper','scissors']
player = 0
opponent = 0
match = 0


while True:
    

    match += 1
    print()
    player_pick = (input("Enter rock/paper/scissors or 'Q' to Quit: ")).lower()
    
    if player_pick== 'q':
        quit()

    if player_pick not in option:
        print("Invalid Input:") 
        continue

    r = random.randint(0,2)

    opponent_pick = option[r]
    print(f"Hattori: {opponent_pick}")
    
    # Logic of Game.
    if player_pick == opponent_pick:
        print("Tie")
        player += 0
        opponent += 0
    
    elif player_pick == 'rock' and opponent_pick == 'scissors':
        print("Win")
        player += 1

    elif player_pick == "paper" and opponent_pick == "rock":
        print("Win")
        player += 1

    elif player_pick == "scissors" and opponent_pick == "paper":
        print("Win")
        player += 1
    
    else:
        print("Lose")
        opponent += 1
    
    if match == 3 :
        if player > opponent:
            print("__________")
            typewriter("You WIN! ")
            break

        elif player == opponent :
            print("__________")
            typewriter("It's a TIE!")
            typewriter(f"Your score is {player}")
            typewriter(f"Hattori score is {opponent}")
            player = 0
            opponent = 0
            match = 0
            continue

        else:
            print("__________")
            typewriter("You LOSE!")
            typewriter(f"Your score is {player}")
            typewriter(f"Hattori score is {opponent}")
            player = 0
            opponent = 0
            match = 0
            continue

    


print("Loading " , end = '')
load(".............")
typewriter(f"Your score is {player}")
typewriter(f"Hattori score is {opponent}")

time.sleep(2.5)
os.system('cls')

print("HATTORI HANZO:-", end = '')
typewriter("You're stronger than you look ...")
typewriter("(could he be the choosen one...)")
print()

typewriter("Move forword.... Join a Team...")
typewriter("All the Best for your Journy")

print(f"{name}:-")
TypeError("Thank You!!!")

while True:
    play = input("Press Enter to Join a Team: ")

    if play == '':
        break

print("Saving Progress...",end='')
load("......",0.5)

if  player > opponent :
    time.sleep(5)
    os.system('cls')


while True:
    play = input("Press Enter to continue: ")

    if play == '':
        break

