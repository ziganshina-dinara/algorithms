import numpy as np

class Stack:

    def __init__(self, n):
        self.top = -1
        self.length = n
        self.massive = [None] * self.length

    def stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, x):
        if self.top + 1 < self.length:
            self.top += 1
            self.massive[self.top] = x
        else:
            print('Stack overflow')

    def pop(self):
        if self.stack_empty():
            print('Stack is empty')
        else:
            self.top -= 1
            return self.massive[self.top + 1]


    class Queue:
        def __init__(self, n):
            self.length = n
            self.array = [None] * self.length
            self.head = 0  # first element
            self.tail = 0  # where add

        def empty(self):
            if self.head == self.empty:
                return True
            else:
                return False

        # i dont now
        # def full(self):
        #     if self.tail == self.length - 1:
        #         if self.tail ==
        #
        #     if self.head == self.tail + 1:
        #         return True
        #     else:
        #         return False

        def enqueue(self, x):
            self.array[self.tail] = x
            if self.tail + 1 == self.length:
                self.tail = 0
            else:
                self.tail += 1

        def dequeue(self):
            if self.empty():
                return 'queue is empty'
            else:
                x = self.array[self.head]
                if self.head == self.length - 1:
                    self.head = 0
                else:
                    self.head += 1
                return x

if __name__ == '__main__':

    my_stack = Stack(10)
    print(my_stack.massive)
    my_stack.stack_empty()
    print(my_stack.massive)
    x = my_stack.pop()
    print(my_stack.massive)
    my_stack.push('yes')
    print(my_stack.massive)
    print(my_stack.pop())
    print(my_stack.massive)
    for i in range(11):
        my_stack.push('yes')
        print(my_stack.massive)