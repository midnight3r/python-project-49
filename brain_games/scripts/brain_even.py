#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f'Hello, {name}!')
    i = 0
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    while i < 3:
        guessed_number = randint(1, 100)
        answer = input(f'Question: {guessed_number}\nYour answer: ')
        if answer != 'yes' and answer != 'no' and guessed_number % 2 == 0:
            print(f'{answer} is wrong answer ;(. Correct answer was \'yes\'.\nLet\'s try again, {name}')
            break
        elif answer != 'yes' and answer != 'no' and guessed_number % 2 != 0:
            print(f'{answer} is wrong answer ;(. Correct answer was \'no\'.\nLet\'s try again, {name}')
            break
        elif answer == 'yes' and guessed_number % 2 != 0:
            print(f'{answer} is wrong answer ;(. Correct answer was \'no\'.\nLet\'s try again, {name}')
            break
        elif answer == 'no' and guessed_number % 2 == 0:
            print(f'{answer} is wrong answer ;(. Correct answer was \'yes\'.\nLet\'s try again, {name}')
            break
        elif answer == 'yes' and guessed_number % 2 == 0:
            print('Correct!')
            i += 1
        elif answer == 'no' and guessed_number % 2 != 0:
            print('Correct!')
            i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
