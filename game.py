import random
user_wins=0
computer_wins=0

option =['rock', 'scissors', 'paper']

while True:
    user_input= input('type rock/scissors/paper or q to quit: ').lower()
    if user_input=='q':
        break

    if user_input not in ['rock', 'scissors', 'paper']:
        continue
    random_number=random.randint(0,2)
    #rock:0, scissor:2, paper:
    
    computer_pick=option[random_number]
    print('computer picked', computer_pick + ".")

    if user_input=='rock' and computer_pick=='scissors':
        print('you won')
        user_wins+=1
        continue

    elif user_input=='paper' and computer_pick=='rock':
        print('you won')
        user_wins+=1
        continue

    elif user_input=='scissors' and computer_pick=='paper':
        print('you won')
        user_wins+=1
        continue
    else:
        print('you lost')
        computer_wins+=1
print ('you won', user_wins,'times.')
print('the computer won', computer_wins,'times.')
print('goodbye')


