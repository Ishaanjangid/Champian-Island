import time
import sys

# This function create a loading animation
def load(text, delay=0.1):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

# This function create a typewrite effect #
def typewriter(s , delay = 0.086):
    for i in s:
        print(i, end="", flush=True)
        time.sleep(delay)
    print()

# This funtion will help to seperate out 
# specific part of a text file

def story_part(file_path,initial_index,final_index):
    line_number = list(range((initial_index -1) ,final_index ))
    mylines = []

    with open(file_path) as f:
        for i , line in enumerate(f):
            if i in line_number:

                mylines.append(line.rstrip())
            elif i > final_index:
                break
    for content in mylines:
        typewriter(content)


if __name__ == "__main__" :
    load("############")
    load("############", 0.05)
    load()
    typewriter()
    story_part()