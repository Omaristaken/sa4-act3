number = 10

again = True
trys = 3

while again != 'q':
    print("I'm thinking of a number...")
    guess = int(input("What number am I thinking of? "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
 
    
    if guess > number:
        print('Your guess was higher than the number.')
    else:
        print('Your guess was lower than the number.')


    trys -= 1
    if trys == 0:
        break
    print(f'You have {trys} trys left')

    again = input('Enter q to exit or enter to take another guess.')

if again == 'q' or trys == 0:
    print(f"Sorry! The number was {number}.")
