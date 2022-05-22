"""
Задача на программирование: кодирование Хаффмана
По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код.
 В первой строке выведите количество различных букв k, встречающихся в строке, и размер получившейся закодированной строки.
 В следующих k строках запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.
"""
def huffman_coding(string):
    letters = set(string)
    if len(letters) == 1:
        dict_coding = {list(letters)[0]: '0'}
    else:
        list_nodes = [Node(letter, string.count(letter), None, None, None) for letter in letters]
        pr_queue = Priority_Queue(list_nodes)
        while len(pr_queue.nodes) > 1:
            pr_queue.make_new_node_from_pair_modes_with_lowest_priorities()
        dict_coding = {}
        temp_node = pr_queue.nodes[0]
        coding = ''
        while (temp_node.left_leaf != None) or (temp_node.right_leaf != None):
            while (temp_node.left_leaf != None) or (temp_node.right_leaf != None):
                if temp_node.left_leaf:
                    temp_node = temp_node.left_leaf
                    coding += '0'
                else:
                    temp_node = temp_node.right_leaf
                    coding += '1'
            if temp_node.letter:
                dict_coding[temp_node.letter] = coding
            if coding[-1] == '0':
                temp_node.parent.left_leaf = None
            else:
                temp_node.parent.right_leaf = None
            temp_node = pr_queue.nodes[0]
            coding = ''

    return  dict_coding


class Node:
    def __init__(self, letter, freq, left_leaf, right_leaf, parent):
        self.letter = letter
        self.freq = freq
        self.left_leaf = left_leaf
        self.right_leaf = right_leaf
        self.parent = parent

class Priority_Queue:
    def __init__(self, nodes):
        self.nodes = nodes

    def make_new_node_from_pair_modes_with_lowest_priorities(self):
        self.nodes.sort(key=lambda x: x.freq)
        node_1 = self.nodes.pop(0)
        node_2 = self.nodes.pop(0)
        new_node = Node(None, node_1.freq + node_2.freq, node_1, node_2, None)
        node_1.parent = new_node
        node_2.parent = new_node
        self.nodes.append(new_node)


def main():
    string = input()
    coding_dict = huffman_coding(string)
    coding_sting = str()
    for letter in string:
        coding_sting += coding_dict[letter]
    print(len(coding_dict), len(coding_sting))
    for letter in coding_dict.keys():
        print(letter + ':', coding_dict[letter])
    print(coding_sting)


if __name__ == "__main__":
    main()
