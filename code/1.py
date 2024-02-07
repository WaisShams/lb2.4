#!/usr/bin/env python3
# -- coding: utf-8 --


if __name__ == '__main__':
    lis = []
    lisa = []
    n = int(input('Введите длину массива: '))
    k = 0
    print('Введите элементы массива\n')
    for i in range(n):
        lis.append(int(input()))
   
    for i,x  in enumerate(lis):
        if x == 0:
            k += 1
            print(i, 'индекс нулевого элемента')
    print('Колчисетво нулевых элементов = ', k)
    
