#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    tries = 0
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    while tries < 3:
        guessed_number = randint(1, 100)
        ans = input(f'Question: {guessed_number}\nYour answer: ')  # answer
        even_number = guessed_number % 2 == 0 and True or False
        odd_number = guessed_number % 2 != 0 and True or False
        right_ans = even_number and 'yes' or odd_number and 'no'  # right answer
        wrong_answer = even_number and 'no' or odd_number and 'yes'
        if ans == right_ans:
            print('Correct!')
            tries += 1
        elif ans == wrong_answer:
            print(f'{ans} is wrong answer ;(. Correct answer was {right_ans}.')
            print(f'Let\'s try again, {name}!')
            break
    if tries == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
