number = 10

again = True
count = 5

while again != 'q':
    print("I'm thinking of a number...")
    guess = int(input("What number am I thinking of? "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
 
    if count > 0:
        if guess > number:
            print('Your guess was higher than the number.')
        else:
            print('Your guess was lower than the number.')
        count -= 1
        print(f'You have {count} hints left')

    again = input('Enter q to exit or enter to take another guess.')

if again == 'q':
    print(f"Sorry! The number was {number}.")
