def fib(n):
    n = n - 1
    list_numbers = [1, 1]
    if n < 2:
        return 1
    else:
        for i in range(2, n + 1):
            list_numbers.append(list_numbers[i-1] + list_numbers[i-2])
        return list_numbers[n]


def fib_digit(n):
    n = n - 1
    list_numbers = [1, 1]
    if n < 2:
        return 1
    else:
        for i in range(2, n + 1):
            list_numbers.append((list_numbers[i-1] + list_numbers[i-2]) %  10)
        return list_numbers[n]


def fib_mod(n, m):
    n = n - 1
    list_numbers = [1 % m, 1 % m]
    if n < 2:
        return 1 % m
    else:
        for i in range(2, n + 1):
            list_numbers.append((list_numbers[i - 1] % m + list_numbers[i - 2] % m) % m)
        return list_numbers[n]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()