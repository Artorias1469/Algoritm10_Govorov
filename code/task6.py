#!usr/bin/env python3
# -*- coding: utf-8 -*-


import heapq

def print_sorted_sums(A, B):
    n = len(A)
    sorted_sums = []

    # Создаем кучу из первых сумм A[i] + B[0] для всех i от 0 до n-1
    heap = [(A[i] + B[0], i, 0) for i in range(n)]
    heapq.heapify(heap)

    # Итеративно извлекаем минимальный элемент из кучи,
    # добавляем его в отсортированный список и добавляем следующую сумму A[i] + B[j+1] в кучу
    while heap:
        sum, i, j = heapq.heappop(heap)
        sorted_sums.append(sum)

        if j+1 < n:
            heapq.heappush(heap, (A[i] + B[j+1], i, j+1))

    # Выводим отсортированный список сумм
    for sum in sorted_sums:
        print(sum, end=' ')
    print()


def main():
    A = [1, 4, 7]
    B = [2, 5, 8]
    print_sorted_sums(A, B)


if __name__ == "__main__":
    main()