import statistics
import pprint


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ]
        )
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )

        return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
        )


lista1 = [44, 53, 12, 9999999, 324, 42523, 2, 55, 643, 99]
lista2 = [44, 53, 12, 99999, 324, 42523, 2, 55, 643, 99]
lista3 = [44, 53, 12, 999999, 324, 42523, 2, 55, 643, 99]
lista4 = [44, 53, 12, 99999999, 324, 42523, 2, 55, 643, 99]
lista5 = [44, 53, 12, 999999999, 324, 42523, 2, 55, 643, 99]
lista6 = [44, 53, 12, 9999999999, 324, 42523, 2, 55, 643, 99]
lista7 = [44, 53, 12, 99999999999, 324, 42523, 2, 55, 643, 99]
lista8 = [44, 53, 12, 9999, 324, 42523, 2, 55, 643, 99]

biglist =[lista8, lista6, lista5, lista7, lista4, lista2, lista3, lista1]
result = map(quicksort, biglist)
result2 = list(result)
result3 = quicksort(result2)
print(list(result3))

