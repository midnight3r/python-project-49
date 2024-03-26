#!/usr/bin/env python3

from random import randint
import prompt


def is_prime_number(guess_number):
    divider = 2
    if guess_number == 1:
        return 'no'
    while divider <= guess_number:
        if guess_number % divider != 0:
            divider += 1
        elif guess_number == divider and guess_number != 1:
            return 'yes'
        elif guess_number % divider == 0:
            return 'no'


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    tries = 0
    while tries < 3:
        guess_number = randint(1, 100)
        result = is_prime_number(guess_number)
        answer = str(input(f'Question: {guess_number}\nYour answer: '))
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
