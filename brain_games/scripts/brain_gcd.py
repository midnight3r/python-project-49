#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    tries = 0
    while tries < 3:
        guess_one = randint(1, 100)
        guess_two = randint(1, 100)
        answer = input(f'Question: {guess_one} {guess_two}\nYour answer: ')
        divider = 100
        while divider >= 2:
            if guess_one % divider == 0 and guess_two % divider == 0:
                divider = divider
                break
            else:
                divider = divider - 1
        if str(answer) == str(divider):
            print('Correct!')
            tries += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {divider}.')
            print(f'Let\'s try again, {name}!')
            break
    if tries == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
