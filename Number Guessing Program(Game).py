'''
Create a number guessing Programm. In the programm there are three level : 
easy,medium and hard Every level should have a different guessing chance
'''

import random
import time

print(f"\n\t---------Number guessing program--------")

# file handling
with open("easy.txt", "r") as f:
    f.read()

print(f" ---*Instructions---\n")
print(f"There are three level : easy,medium and hard Every level should have a different guessing chance")
print(f"\n1. Choose the level before start the game")
print(f"2. After you choosing the level you should complete Game")
print(f"3. As per the instruction you have to follow the certain rules")

print("\n\tAll the best :)")

# Computer generated random number
computer=random.randint(0,10)

print(computer)

'''user=int(input("\nEnter Your number from 1 to 10 :"))
print(f"\nYou Entered number is : {user}")'''

'''if(user>=10):
    print(f"\nInvalid Number Enter number ranging from 1 to 10")
    exit()
'''

# Fuction For easy level
def easy_level():
    print(f"\n*Instructions*")
    print("\n You Will get 3 chances to guessing the write number in easy level \n")

    chances=3
    count=0

    
    while count<chances:
            user_guess=int(input("\nEnter Your number from 1 to 10 :"))
            print(f"\nYou Entered number is : {user_guess}")
            count+=1

            if(user_guess==computer):
                print("\t\nYou Win!!\n Congratulations!")
                print(f"You guess the in number of gusses is:{count}")
                
                # Writing number of count
                with open("easy.txt", "w") as f:
                     f.write(str(count))
                f.close()
                
                time.sleep(2)
                exit()
            elif(user_guess>computer):
                print(f"Please enter less than {user_guess} OR smaller number than this :)")
                print(f"Your guesses is:{count}")
                time.sleep(2)
                
            elif(user_guess<computer):
                print(f"Please enter larger than {user_guess} OR larger number :)")
                print(f"Your guesses is:{count}")
                time.sleep(2)

            elif(user_guess>10):
                print("Invalid Number")

    
    
# funtion for medium_level
def medium_level():
    print(f"\n*Instructions*")
    print("\n You Will get 2 chances to guessing the write number in medium level \n")

    count=0
    chances=2

    while(count<chances):
        user_guess=int(input("\nEnter Your number from 1 to 10 :"))
        print(f"\nYou Entered number is : {user_guess}")
        count+=1

        if(user_guess==computer):
                print("\t\nYou Win!!\n Congratulations!")
                print(f"You guess the in number of gusses is:{count}")
                time.sleep(2)

                with open("medium.txt", "w") as f:
                     f.write(str(count))
                f.close()
                
                exit()
        elif(user_guess>computer):
            print(f"Please enter less than {user_guess} OR smaller number than this :)")
            print(f"Your guesses is:{count}")
            time.sleep(2)
                
        elif(user_guess<computer):
            print(f"Please enter larger than {user_guess} OR larger number :)")
            print(f"Your guesses is:{count}")
            time.sleep(2)

# funtion for hard_level
def hard_level():
    print(f"\n*Instructions*")
    print("\n You Will get 1 chances to guessing the write number in hard level \n")

    count=0
    chances=1

    while(count<chances):
        user_guess=int(input("\nEnter Your number from 1 to 10 :"))
        print(f"\nYou Entered number is : {user_guess}")
        count+=1

        if(user_guess==computer):
                print("\t\nYou Win!!\n Congratulations!")
                print(f"You guess the in number of gusses is:{count}")
                time.sleep(2)

                with open("hard.txt", "w") as f:
                     f.write(str(count))
                f.close()
                

                exit()
        elif(user_guess>computer):
            print(f"Please enter less than {user_guess} OR smaller number than this :)")
            print(f"Your guesses is:{count}")
            time.sleep(2)
                
        elif(user_guess<computer):
            print(f"Please enter larger than {user_guess} OR larger number :)")
            print(f"Your guesses is:{count}")
            time.sleep(2)


# Choosing level
print("\n1. Easy")
print("2. Medium")
print("3. Hard")

level_type=int(input("\n\nEnter Your Level Type From them(enter level number: )"))

def choose_level(level):
    if(level==1):
        print(f"You Choose Easy Level")
        easy_level()
    elif(level==2):
        print(f"You Choose Medium Level")
        medium_level()
    elif(level==3):
        print(f"You Choose Hard Level")
        hard_level()
    else:
        print(f"You Enter wrong choice")
        exit()
    
    return None



choose_level(level_type)