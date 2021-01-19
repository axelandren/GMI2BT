def check_divisible(first, second):
    numbers_list = []
    i = 1
    while i <= 1000:
        if i % int(first) == 0 and i % int(second) == 0:
            numbers_list.append(i)
        i = i + 1
    print(f'Result: {numbers_list}')
    input('\nPress Enter to continue...')

def guess_randint():
    from random import randint
    target = randint(1, 101)
    hit_the_target = False
    while hit_the_target == False:
        while True:
            try:
                guess = int(input('Guess the number: '))
                break
            except ValueError:
                print('Numbers only please...')
        if guess == target:
            print(f'\nCongratulations! Number {guess} was the right answer!')
            input('\nPress Enter to continue...')
            hit_the_target = True
        elif guess < target:
            print(f'The target number is higher than {guess}')
        elif guess > target:
            print(f'The target number is lower than {guess}')