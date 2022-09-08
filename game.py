'''
Author: Ahad#3257
License: MIT
Github: https://github.com/CruelDev69/RPS-Console-Game/
'''

import random # Importing Random Module

# Making Game Function
def gameRPS(computer, you):
    if computer == you:
        return None
    if computer == "rock":
        if you == "scissor":
            return False
        elif you == "paper":
            return True 
    elif computer == "paper":
            if you == "rock":
              return False
            elif you == "scissor":
              return True 
    elif computer == "scissor":
            if you == "paper":
              return False
            elif you == "rock":
              return True 

print('''
█▄▄▄▄ █ ▄▄    ▄▄▄▄▄   
█  ▄▀ █   █  █     ▀▄ 
█▀▀▌  █▀▀▀ ▄  ▀▀▀▀▄   
█  █  █     ▀▄▄▄▄▀    
  █    █              
 ▀      ▀             
                      
''')
print("Computer's Turn: Choose between (R)ock, (P)aper or (S)cissor.")
print("Computer has chosen the option.")
randomNumber = random.randint(1, 3)

if randomNumber == 1:
    computer = "rock"
elif randomNumber == 2:
    computer = "paper"
elif randomNumber == 3:
    computer = "scissor"    

you = input("Your Turn: Choose between (R)ock, (P)aper or (S)cissor: ")
print("You have chosen the option.")

a = gameRPS(computer, you)

print(f"Computer chose {computer} and you chose {you}.")

if a == None:
    print("Wow, its a tie maybe try doing a rematch?")
elif a:
    print("Yay! Congratulations you won thw game.")
else: 
    print("Oh no! You lost the game better luck next time.")
