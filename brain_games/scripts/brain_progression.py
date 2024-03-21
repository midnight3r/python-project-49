#!/usr/bin/env python3

from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    list_of_num = list(range(1, 101))
    tries = 0
    while tries < 3:
        start_of_list = randint(0, 81)
        end_of_list = start_of_list + 20
        final_list = list_of_num[start_of_list:end_of_list:2]
        random_num = randint(0, 9)
        guess = final_list.pop(random_num)
        final_list.insert(random_num, '..')
        answer = input(f'Question: {final_list}\nYour answer: ')
        if str(answer) == str(guess):
            print('Correct!')
            tries += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {guess}.')
            print(f'Let\'s try again, {name}!')
            break
    if tries == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
