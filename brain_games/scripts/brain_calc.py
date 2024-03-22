#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    tries = 0
    while tries < 3:
        n_1 = randint(1, 100)  # random number 1
        n_2 = randint(1, 100)  # random number 2
        expressions = (n_1 + n_2, n_1 - n_2, n_1 * n_2)
        str_exp = (f'{n_1} + {n_2}', f'{n_1} - {n_2}', f'{n_1} * {n_2}')
        rand_num = randint(0, 2)  # random number for list
        print(f'Question: {str_exp[rand_num]}')
        ans = input('Your answer: ')
        right_ans = expressions[rand_num]
        wrong_ans = f'{ans} is wrong answer ;(. Correct answer was {right_ans}.'
        if str(ans) == str(right_ans):
            print('Correct!')
            tries += 1
        elif str(ans) != str(right_ans):
            print(wrong_ans)
            print(f'Let\'s try again, {name}!')
            break

    if tries == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
