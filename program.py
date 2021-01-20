import modules

def get_number():
    while True:
        try:
            number = int(input())
            break
        except ValueError:
            print('Numbers only please...')
    return number

show_menu = True
while show_menu:
    print('\n+-----------------------------------+')
    print(' 1. Divisible numbers\n 2. Guess a number between 1 and 100\n 3. Exit program')
    print('+-----------------------------------+')
    choice = input('\nChoose an option: ')
    if choice == '1':
        print('Enter your first number')
        first_number = get_number()
        print('Enter your second number')
        second_number = get_number()
        modules.check_divisibility(first_number, second_number)
    elif choice == '2':
        modules.guess_randint()
    elif choice == '3':
        print('Exiting...')
        show_menu = False
        break
    else:
        print('Type a valid option')