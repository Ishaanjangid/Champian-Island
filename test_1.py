lst = [1,2,3,4]

while True:
    

    team_select = input("Enter [1,2,3,4] or Q to quit: ")
    
    if team_select.isdigit():

        team_select = int(team_select)
        if team_select in lst:
            print("This is in [1,2,3,4]")
            break

    elif team_select == 'q':
        quit()   
    
    else:
        print("Invalit Input")
        continue

print()
print(team_select)     