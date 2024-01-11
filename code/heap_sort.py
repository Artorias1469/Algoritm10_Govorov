#!usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import matplotlib.pyplot as plt
import random
import sympy as sp


def heapify(nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[i] < nums[left]:
        largest = left

    if right < n and nums[largest] < nums[right]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heapSort(nums):
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def roots(x, y):
    sum_x = sum(x)
    sum_y = sum(y)

    sum_x2 = sum(i**2 for i in x)
    sum_xy = sum([i * j for i, j in zip(x, y)])

    n = len(x) + 1

    a, b = sp.symbols('a b')

    equation_1 = sp.Eq(sum_x2 * a + sum_x * b, sum_xy)
    equation_2 = sp.Eq(sum_x * a + (n) * b, sum_y)

    sol = sp.solve((equation_1, equation_2), (a, b))

    x1 = x
    x2 = [sol[a] * i + sol[b] for i in x1]
    return x1, x2


def gen_list(n):
        nums = []
        for _ in range(n):
            nums.append(random.randint(1, 100))
        return nums


def show_grf():
    def create_grf(x, y, x1, y1, name_of_graph, name_x, name_y):
        plt.plot(x, y, 'o', color='red')
        plt.plot(x1, y1, '.-', color='black')

        plt.xlabel(name_x)
        plt.ylabel(name_y)

        plt.title(name_of_graph)
        plt.show()
    
    def ever_sort_gph(x=[], y=[]):
        for i in range(1000, 50001, 1000):
            x.append(i)
            nums = [j for j in range(i)]
            execution_time = timeit.timeit(
                lambda: heapSort(nums), number=1
            )
            y.append(execution_time)
        
        x1, y1 = roots(x, y)

        create_grf(
            x,
            y,
            x1,
            y1, 
            "Список - отсоритрованный", 
            "Размер", 
            "Время"
        )
    
    def worst_sort_gph(x=[], y=[]):
        for i in range(1000, 50001, 1000):
            x.append(i)
            nums = [j for j in range(i, 0, -1)]
            execution_time = timeit.timeit(
                lambda: heapSort(nums), number=1
            )
            y.append(execution_time)

        x1, y1 = roots(x, y)

        create_grf(
            x,
            y,
            x1,
            y1, 
            "Список - неотсоритрованный", 
            "Размер", 
            "Время"
        )
    
    def sr_sort_gph(x=[], y=[]):
        for i in range(1000, 50001, 1000):
            x.append(i)
            nums = gen_list(i)
            execution_time = timeit.timeit(
                lambda: heapSort(nums), number=1
            ) 
            y.append(execution_time)
        
        x1, y1 = roots(x, y)

        create_grf(
            x,
            y,
            x1,
            y1, 
            "Список - случайные значения", 
            "Размер", 
            "Время"
        )

    ever_sort_gph()
    worst_sort_gph()
    sr_sort_gph()


def main():
    show_grf()


if __name__ == "__main__":
    main()