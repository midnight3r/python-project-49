#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    tries = 0
    while tries < 3:
        divider = 2
        result = ""
        guess_number = randint(1, 100)
        answer = str(input(f'Question: {guess_number}\nYour answer: '))
        if guess_number == 1 and answer == 'no':
            print('Correct!')
            tries += 1
        elif guess_number == 1 and answer != 'no':
            print(f'{answer} is wrong answer ;(. Correct answer was \"no\".')
            print(f'Let\'s try again, {name}!')
            break
        while divider <= guess_number:
            if guess_number % divider != 0:
                divider += 1
            elif guess_number == divider:
                result = 'yes'
                break
            elif guess_number % divider == 0:
                divider += 1
                result = 'no'
                break
        if answer == result:
            print('Correct!')
            tries += 1
        if answer != result:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}.')
            print(f'Let\'s try again, {name}!')
            break
    if tries == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
