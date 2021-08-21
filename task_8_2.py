# Закодируйте любую строку из трех слов по алгоритму Хаффмана

class Node:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left_el = None
        self.right_el = None


class HuffmanTree:
    def __init__(self, text):
        self.init_text = text
        char_weights = self.get_char_weights(text)
        self.leaf_tree = [Node(sym, freq) for sym, freq in char_weights.items()]
        while len(self.leaf_tree) != 1:
            self.leaf_tree.sort(key=lambda node: node.value, reverse=True)
            node_tree = Node(value=(self.leaf_tree[-1].value + self.leaf_tree[-2].value))
            node_tree.left_el = self.leaf_tree.pop(-1)
            node_tree.right_el = self.leaf_tree.pop(-1)
            self.leaf_tree.append(node_tree)
        self.root = self.leaf_tree[0]
        self.buffer = list(range(10))
        self.sym_codes = {}

    @staticmethod
    def get_char_weights(text):
        result = {}
        for sym in text:
            if sym in result:
                result[sym] += 1
            else:
                result[sym] = 1
        return result

    def generate_sym_codes(self, tree, length_code):
        node = tree
        if not node:
            return
        elif node.name:
            sym_code = ''
            for idx in range(length_code):
                sym_code = f'{sym_code}{self.buffer[idx]}'
            self.sym_codes[node.name] = sym_code
            return
        self.buffer[length_code] = 0
        self.generate_sym_codes(node.left_el, length_code + 1)
        self.buffer[length_code] = 1
        self.generate_sym_codes(node.right_el, length_code + 1)

    def get_code(self):
        self.generate_sym_codes(self.root, 0)
        result = []
        for sym in self.init_text:
            result.append(self.sym_codes[sym])
        return ''.join(result)


if __name__ == '__main__':
    user_text = input('Enter text: ')
    huffman_tree = HuffmanTree(user_text)
    print(f'Code: {huffman_tree.get_code()}')
