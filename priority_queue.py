"""
Первая строка входа содержит число операций 1 < n < 10^5. Каждая из последующих n строк задают операцию одного из следующих двух типов:

Insert x, где 0 < x < 10^9 — целое число;
ExtractMax
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
"""
class PriorityQueue:
    def __init__(self):
        self.array = []

    def sift_up(self):
        i = len(self.array) - 1  # index node x
        while i > 0:
            parent_index = (i - 1) // 2
            if self.array[parent_index] < self.array[i]:
                self.array[parent_index], self.array[i] = self.array[i], self.array[parent_index]
                i = parent_index
            else:
                break

    def sift_down(self):
        i = 0
        while i < len(self.array):
            child_index_1 = 2 * i + 1
            child_index_2 = 2 * i + 2
            if child_index_2 < len(self.array):
                if self.array[child_index_2] > self.array[child_index_1]:
                    bigest_child_index = child_index_2
                else:
                    bigest_child_index = child_index_1
            elif child_index_1 < len(self.array):
                bigest_child_index = child_index_1
            else:
                break
            if self.array[i] < self.array[bigest_child_index]:
                self.array[bigest_child_index], self.array[i] = self.array[i], self.array[bigest_child_index]
                i = bigest_child_index
            else:
                break
    def insert(self, x):
        self.array.append(x)
        self.sift_up()

    def extract_max(self):
        if len(self.array) > 1:
            to_return = self.array[0]
            self.array[0] = self.array.pop(-1)
            self.sift_down()
            return to_return
        else:
             return self.array.pop()


def main():
    n_iter = int(input())
    queue_pri = PriorityQueue()
    for i in range(n_iter):
        command = input()
        if 'ExtractMax' in command:
            print(queue_pri.extract_max())
        else:
            x = int(command.split()[1])
            queue_pri.insert(x)



if __name__ == "__main__":
    main()
