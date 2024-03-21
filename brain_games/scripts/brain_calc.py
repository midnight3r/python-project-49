#!/usr/bin/env python3

from random import choice, randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    tries = 0
    while tries < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        operators = ('+', '-', '*')
        operator = choice(operators)
        print(f'Question: {num_1} {operator} {num_2}')
        answer = input('Your answer: ')
        if operator == '+' and str(answer) == str(num_1 + num_2):
            print('Correct!')
            tries += 1
        elif operator == '-' and str(answer) == str(num_1 - num_2):
            print('Correct!')
            tries += 1
        elif operator == '*' and str(answer) == str(num_1 * num_2):
            print('Correct!')
            tries += 1
        elif operator == '*' and str(answer) != str(num_1 * num_2):
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 * num_2}.')
            print(f'\nLet\'s try again, {name}!')
            break
        elif operator == '+' and str(answer) != str(num_1 + num_2):
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 + num_2}.')
            print(f'Let\'s try again, {name}!')
            break
        elif operator == '-' and str(answer) != str(num_1 - num_2):
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 - num_2}.')
            print(f'Let\'s try again, {name}!')
            break

    if tries == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
