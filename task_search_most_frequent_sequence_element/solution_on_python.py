def find_frequent_element(array):
    list_res = []
    array.sort()
    q = 0
    for i in range(len(array)):
        q += 1
        if i + 1 < len(array):
            if array[i] != array[i+1]:
                list_res.append((array[i], q))
                q = 0
        else:
            list_res.append((array[i], q))
    list_res.sort(key=lambda x: (x[1], x[0]))
    return list_res[-1][0]

def main():
    n = int(input())
    array = list(map(int, input().split()))
    freq_el = find_frequent_element(array)
    print(freq_el)



if __name__ == "__main__":
    main()