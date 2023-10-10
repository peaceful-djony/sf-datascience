from numpy import random
from numpy import mean

NUM_FROM = 1
NUM_TO = 100
SCORE_ITERATIONS = 10000

random.seed(10)


def score_game(func) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        rand_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = random.randint(NUM_FROM, NUM_TO + 1, size=SCORE_ITERATIONS)  # загадали список чисел

    for number in random_array:
        res = func(number)
        count_ls.append(res)

    score = int(mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

    return score


def game_core_v3(number: int = 1) -> int:
    """
    Подсчет попыток "угадывание" заданного числа number
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # инициализация начального значения счетчика
    count = 0
    # инициализация начального значения для угадывания псевдослучайным образом
    predict = random.randint(NUM_FROM, NUM_TO + 1)
    # инициализация левой границы проверяемого диапазона
    left_edge = NUM_FROM - 1
    # инициализация правой границы проверяемого диапазона
    right_edge = NUM_TO + 1

    # цикл поиска с условием выхода, когда угадываемое число predict станет равен загаданному числу number
    while number != predict:
        # увеличение счетчика попыток угадывания
        count += 1
        if number < predict:
            # смещение - установка правой границы поиска в значение predict
            right_edge = predict
        elif number > predict:
            # смещение - установка левой границы поиска в значение predict
            left_edge = predict
        # predict - среднее значение между обновленным диапазоном
        predict = left_edge + (right_edge - left_edge) // 2

    return count


if __name__ == '__main__':
    result = score_game(game_core_v3)
    print(f'Run benchmarking for game_core_v3: {result}', end='')
