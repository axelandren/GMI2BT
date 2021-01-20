def get_number():
    while True:
        try:
            number = int(input())
            break
        except ValueError:
            print('Numbers only please...')
    return number

def check_divisibility(first, second):
    numbers = []
    for i in range(1, 1001):
        if i % first == 0 and i % second == 0:
            numbers.append(i)
    numbers_dict = {
        'Result': numbers,
        'Average': sum(numbers) / len(numbers)
    }
    return numbers_dict

def guess_randint():
    from random import randint
    target = randint(1, 101)
    amount_of_guesses = 0
    print('Guess a number between 1 - 100')
    while True:
        guess = get_number()
        amount_of_guesses += 1
        if guess == target:
            print(f'\nCongratulations! {guess} was the right answer!\nIt took you {amount_of_guesses} tries to get it right.')
            input('\nPress Enter to continue...')
            break
        elif guess < target:
            print(f'The target number is higher than {guess}')
        elif guess > target:
            print(f'The target number is lower than {guess}')