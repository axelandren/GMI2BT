def check_divisibility(first, second):
    numbers = []
    i = 1
    while i <= 1000:
        if i % int(first) == 0 and i % int(second) == 0:
            numbers.append(i)
        i += 1
    print(f'Result: {numbers}')
    print(f'Average value is: {sum(numbers) / len(numbers)}')
    input('\nPress Enter to continue...')

def guess_randint():
    from random import randint
    target = randint(1, 101)
    amount_of_guesses = 0
    hit_the_target = False
    while hit_the_target == False:
        while True:
            try:
                guess = int(input('Guess the number: '))
                break
            except ValueError:
                print('Numbers only please...')
        amount_of_guesses += 1
        if guess == target:
            print(f'\nCongratulations! {guess} was the right answer!\nIt took you {amount_of_guesses} tries to get it right.')
            input('\nPress Enter to continue...')
            hit_the_target = True
        elif guess < target:
            print(f'The target number is higher than {guess}')
        elif guess > target:
            print(f'The target number is lower than {guess}')