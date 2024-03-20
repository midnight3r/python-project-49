#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        guess_number_one = randint(1, 100)
        guess_number_two = randint(1, 100)
        answer = input(f'Question: {guess_number_one} {guess_number_two}\nYour answer: ')
        divider = 100
        while divider >= 2:
            if guess_number_one % divider == 0 and guess_number_two % divider == 0:
                divider = divider
                break
            else:
                divider = divider - 1
        if str(answer) == str(divider):
            print('Correct!')
            i += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {divider}.\nLet\'s try again, {name}!')
            break
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
