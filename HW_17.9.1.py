while True:
    try:
        array = list(map(int, input("Введите числа через пробел: ").split()))
    except:
        raise ValueError("Это не число!")
    if bool(array) == False:
        raise ValueError("Вы ничего не ввели!")
    if len(array) == 1:
        raise ValueError("Вы забыли пробелы или ввели одно число!")
    break

while True:
    try:
        element = int(input("Введите число: "))
    except:
        raise ValueError("Ошибка ввода!")
    break

# Быстрая сортировка.
import random

def qsort_random(array):
    if len(array) <= 1:
        return (array)
    p = random.choice(array)
    left = [i for i in array if i < p]
    center = [i for i in array if i == p]
    right = [i for i in array if i > p]

    return qsort_random(left) + center + qsort_random(right)
print(f"Список отсортирован по возрастанию элементов :\n {qsort_random(array)}")


# Поиск номера позиции элемента, который меньше числа, введенного пользователем ,
# а следующий за ним больше или равен этому числу.

sort_array = qsort_random(array)

def binary_search(sort_array, element):
    left, right = 0, len(sort_array)
    if sort_array[0] < element < sort_array[-1]:
        while left < right:
            midll = (left + right) // 2
            if sort_array[midll] < element:
                left = midll + 1
            else:
                right = midll
        return left - 1

    else:
        print(f"Число {element} не соответствует заданным условиям поиска")

if binary_search(sort_array, element) is not None:
    print(f"Номер позиции меньшего элемента = {binary_search(sort_array, element)}")
