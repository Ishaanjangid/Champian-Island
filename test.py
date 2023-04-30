import os
import time
from function import *
from TEAM import *

# Team Selection

# story_part("story.txt",23,26)
# print()
# while True:
#     play = input("Press Enter to continue: ")

#     if play == '':
#         break

# print("Loading")
# load(".........")
# time.sleep(0.5)
# os.system('cls')
# story_part("story.txt",28,32)

#logic
lst = [1,2,3,4]

while True:
    team_select = input("Enter [1,2,3,4] or Q to quit: ")
    
    if team_select.isdigit():
        

        team_select = int(team_select)
        if team_select in lst:
            
            break

    elif team_select == 'q':
        quit()   
    
    else:
        print("Invalit Input")
        continue


team_select == int(team_select)

print()

if team_select == 1:
    print("Team Green")
    story_part("story.txt",37,42)

elif team_select == 2:
    print("Team Yellow")
    story_part("story.txt",61,66)

elif team_select == 3:
    print("Team Red")
    story_part("story.txt",53,58)

elif team_select == 4:
    print("Team Blue")    
    story_part("story.txt",45,50)


lst = [1,2,3]
while True:
    team_info = int(input("Enter: "))
    
    if team_info in lst:
        break
    else:
        continue

print(team_info)


