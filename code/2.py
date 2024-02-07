#!/usr/bin/env python3
# -- coding: utf-8 --


if __name__ == '__main__':
    array = []
    n = int(input('Введите длину массива: '))
    print('Введите элементы массива\n')
    for i in range(n):
        array.append(float(input()))

    pos_1 = 0
    pos_2 = 0
    for i,x in enumerate(array):
        if pos_1 and pos_2:
            break
        elif x > 0 and not pos_1:
            pos_1 = i
        elif x > 0 and not pos_2:
            pos_2 = i

    modified_array = [i for i in array if i] + [0] * array.count(0)

    print(f'Максимальный по модулю: {max(array, key=abs)}')
    print(
        f'Сумма между: {sum(x for i in range(pos_1, pos_2 + 1))}'
        if pos_1 and pos_2
        else 'В массиве один или ноль положительных элементов')
    print(f'Массив со смещением нулей: {modified_array}')
