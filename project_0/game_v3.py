import numpy as np
def random_predict(number) :
    number= np.random.randint(1, 101)
    count = 0
    border_min = 0
    border_max = 101
    while True:
        count +=1
        predict_num = (border_min + border_max) // 2
        if predict_num > number:
            border_max = predict_num
        elif predict_num < number:   
            border_min = predict_num
        else:
            return count
print(f'Количество попыток: {random_predict(100)}')
def score_game(random_predict) :
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
if __name__ == '__main__':
    score_game(random_predict)
