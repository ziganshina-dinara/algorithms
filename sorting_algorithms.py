import numpy as np

# quick_sort
def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


# Insertion sort
def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            i -= 1
            array[i + 1] = array[i]
        array[i + 1] = key


#   MERGE SORT
def merge(array, p, q, r):

    array_1 = np.zeros(q - p + 1)
    array_2 = np.zeros(r - q)
    for i in range(len(array_1)):
        array_1[i] = array[p + i]
    for i in range(len(array_2)):
        array_2[i] = array[q + 1 + i]

    i = 0
    j = 0
    for k in range(p, r):
        if array_1[i] <= array_2[j]:
            array[k] = array_1[i]
            i += 1
        else:
            array[k] = array_2[j]
            j += 1


def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q,r)



if __name__ == '__main__':

    # quick_sort
    array = np.array([3,6,7,84,5,6,1,45,7,89,0,3])
    print(array)
    quick_sort(array, 0, len(array)-1)
    print('after sorting:')
    print(array)

    array = np.array([3])
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print('after sorting:')
    print(array)

    array = np.array([])
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print('after sorting:')
    print(array)

    # insertion_sort
    array = np.array([3, 6, 7, 84, 5, 6, 1, 45, 7, 89, 0, 3])
    print(array)
    insertion_sort(array)
    print('after sorting:')
    print(array)

    array = np.array([3])
    print(array)
    insertion_sort(array)
    print('after sorting:')
    print(array)

    array = np.array([])
    print(array)
    insertion_sort(array)
    print('after sorting:')
    print(array)

    # merge sort
    array = np.array([3, 6, 7, 84, 5, 6, 1, 45, 7, 89, 0, 3])
    print(array)
    merge_sort(array, 0, len(array) - 1)
    print('after sorting:')
    print(array)

    array = np.array([3])
    print(array)
    merge_sort(array, 0, len(array) - 1)
    print('after sorting:')
    print(array)

    array = np.array([])
    print(array)
    merge_sort(array, 0, len(array) - 1)
    print('after sorting:')
    print(array)