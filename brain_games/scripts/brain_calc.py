#!/usr/bin/env python3

from random import choice, randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        operators = ('+', '-', '*')
        operator = choice(operators)
        print(f'Question: {num_1} {operator} {num_2}')
        answer = input('Your answer: ')
        if operator == '+' and str(answer) == str(num_1 + num_2):
            print('Correct!')
            i += 1
        elif operator == '-' and str(answer) == str(num_1 - num_2):
            print('Correct!')
            i += 1
        elif operator == '*' and str(answer) == str(num_1 * num_2):
            print('Correct!')
            i += 1
        elif operator == '*' and str(answer) != str(num_1 * num_2):
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 * num_2}.\nLet\'s try again, {name}!')
            break
        elif operator == '+' and str(answer) != str(num_1 + num_2):
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 + num_2}.\nLet\'s try again, {name}!')
            break
        elif operator == '-' and str(answer) != str(num_1 - num_2):
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 - num_2}.\nLet\'s try again, {name}!')
            break

    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
