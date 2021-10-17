import os
import random
import time


ex_nmu = 10

min_st_dig = 6
max_st_dig = 10

exclude_max = 3

bingo_time = 60


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_dig():
    # return 10
    return random.randint(min_st_dig, max_st_dig)


def ex_generatur(max_dig, sig):
    x = random.randint(exclude_max, max_dig - 1)
    y = max_dig - x
    if sig == '-':
        ex = f'{max_dig} - {x} ='
        return ex, y
    else:
        ex = f'{x} + {y} = '
        return ex, max_dig


def sign_random():
    v = random.randint(1, 2)
    return '-' if v == 1 else '+'


def controller():
    wrong = 0
    for t in range(ex_nmu):
        ex, y = ex_generatur(get_dig(), sign_random())
        print(ex)

        a = 0
        try:
            a = int(input())
        except Exception as e:
            print(f'{bcolors.WARNING}Нужно вводить цифры!!{bcolors.ENDC}')

        if a == y:
            print('Молодец! Правильно!')
        else:
            wrong += 1
            print(f'{bcolors.FAIL}Полька! Ошибка! Правильный ответ{bcolors.ENDC}', y)
        print('-------------------')
    print('------------------------------------------------------')
    print('Верных ответов: ', ex_nmu-wrong, '. Неверных ответов: ', wrong)
    return wrong


if __name__ == '__main__':
    for t in range(20):
        start = int(round(time.time()))
        wrong = controller()
        end_ = int(round(time.time())) - start
        print(f"{bcolors.OKGREEN}Затрачено времени : {int(end_) if end_ > 0 else 0} c{bcolors.ENDC}")
        if wrong == 0 and end_ < bingo_time:
            os.system('say "Молодец. Ты заслужила ipad."')
            break





