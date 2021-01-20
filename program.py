import modules

while True:
    print('\n+-----------------------------------+')
    print(' 1. Divisible numbers\n 2. Guess a number between 1 and 100\n 3. Exit program')
    print('+-----------------------------------+')
    choice = input('\nChoose an option: ')
    if choice == '1':
        print('Enter your first number')
        first_number = modules.get_number()
        print('Enter your second number')
        second_number = modules.get_number()
        numbers_dict = modules.check_divisibility(first_number, second_number)
        print(numbers_dict)
        input('\nPress Enter to continue...')
    elif choice == '2':
        modules.guess_randint()
    elif choice == '3':
        print('Exiting...')
        break
    else:
        print('Type a valid option')