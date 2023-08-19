### CH13: Rock, Paper, Scissors Game

import random
print('if user entered 1 : rock but 2 : paper and 3 : Scissors')
user = int(input('enter a number between 1 and 3 : '))

computer = random.randint(1,3)
print(computer)
    

def main():

    if user == 1 and computer == 3:
        print('the user is winner')

    elif user == 3 and computer == 1:
        print('the computer is winner')    
       

    elif user == 3 and computer == 2 :
          print('the user is winner')

    elif user == 2 and computer == 3 :
        print('the computer is winner')

    elif user == 2 and computer == 1:
         print('the computer is winner') 

    elif user == 1 and computer == 2:
         print('the user is winner')  


main()                

if user == computer :
    print (' please enter a new number')
    user = int(input('enter new number: '))
    
    main()        
 


print('the game is finished')             

