def get_number():
    while True:
        try:
            number = int(input('Type in your number: '))
            break
        except ValueError:
            print('Numbers only please...')
    return number

print('\n1. Divisible numbers')
print('2. Guess a number between 1 and 100')
print('3. Exit program\n')
import modules
show_menu = True
while show_menu:
    choice = input('Choose an option: ')
    if choice == '1':
        first_number = get_number()
        second_number = get_number()
        modules.check_divisible(first_number, second_number)
    elif choice == '2':
        modules.guess_randint()
    elif choice == '3':
        print('Exiting...')
        show_menu = False
        break
    else:
        print('Type a valid option')