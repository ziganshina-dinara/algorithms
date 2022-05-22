"""
Задача на программирование: декодирование Хаффмана

Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв, встречающихся в строке, и размер получившейся
закодированной строки, соответственно. В следующих k строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого.
Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается
в строке хотя бы один раз. Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты.
Заданный код таков, что закодированная строка имеет минимальный возможный размер.

В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита. Гарантируется, что длина правильного
ответа не превосходит 10^4 символов.
"""
def decoding(dict_decoding, encoded_string):
    max_length_coding_letter = max([len(x) for x in dict_decoding.keys()])
    string = str()
    while (len(encoded_string) > 0):
        for k in range(1, max_length_coding_letter + 1):
            sub = encoded_string[0:k]
            if sub in dict_decoding:
                string += dict_decoding[sub]
                encoded_string = encoded_string[k:]
                break
    return string


def main():
    number_letters, encoded_string_length = map(int, input().split())
    dict_decoding = {}
    for i in range(number_letters):
        letter, encoded_letter = input().split(': ')
        dict_decoding[encoded_letter] = letter
    encoded_string = input()
    string_decoding = decoding(dict_decoding, encoded_string)
    print(string_decoding)


if __name__ == "__main__":
    main()
