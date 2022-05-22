"""
Различные слагаемые.
По данному числу 1 < n < 10^9 найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых.
"""
def find_various_summands(n):
    variants = range(1, n + 1)
    list_summands = []
    summ = 0
    i = 0
    while (summ < n):
        if n - (summ + variants[i]) > variants[i]:
            list_summands.append(variants[i])
            summ += variants[i]
        elif n - (summ + variants[i]) == 0:
            list_summands.append(variants[i])
            summ += variants[i]
            return list_summands
        i += 1


def main():
    n = int(input())
    various_summands = find_various_summands(n)
    print(str(len(various_summands)) + '\n' + ' '.join([str(x) for x in various_summands]))


if __name__ == "__main__":
    main()