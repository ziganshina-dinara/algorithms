# Непрерывный рюкзак
def maximum_cost(max_volume, list_items):
    list_items_with_weight_by_volume = [(x[0], x[1], x[0] / x[1]) for x in list_items]
    list_items_with_weight_by_volume.sort(key=lambda x: x[2], reverse=True)
    current_summ = 0
    current_volume = 0
    i = 0
    while (i < len(list_items_with_weight_by_volume)) and (current_volume < max_volume):
        item = list_items_with_weight_by_volume[i]
        if current_volume + item[1] <= max_volume:
            current_summ += item[0]
            current_volume += item[1]
        else:
            part = (max_volume - current_volume) / item[1]
            current_volume += item[1] * part
            current_summ += item[0] * part
        i += 1
    return current_summ

def main():
    n, max_volume = map(int, input().split(' '))
    list_items = []
    for i in range(n):
        list_items.append(list(map(int, input().split(' '))))
    cost = maximum_cost(max_volume, list_items)
    print(cost)


if __name__ == "__main__":
    main()