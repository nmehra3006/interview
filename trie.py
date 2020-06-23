class TrieNode(object):
    def __init__(self):
        self.val = ''
        self.children = [None] * 26
        self.end_of_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.words_inserted = []

    def _get_index(self, ch):
        return ord(ch) - ord('a')

    def _get_ch(self, index):
        return chr(97 + index)

    # expected return value: none
    def insert_word(self, word):
        # for every char compute index
        # create new TrieNode if it does not exist at self.children[index]
        # mark endofword true at leaf node

        # each ch represents a 'depth' in the trie
        # with each ch you go to the child of the current node
        node = self.root
        for ch in word:
            index = self._get_index(ch)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.val = ch
        node.end_of_word = True

    # expected return value: boolean
    def exists(self, word):
        node = self.root
        for ch in word:

            index = self._get_index(ch)
            if not node.children[index]:
                return False

            node = node.children[index]

        return True

    # which dfs: preorder
    def _dfs_helper(self, root, list_of_chars, final_list):

        if not root:
            return

        list_of_chars.append(root.val)

        if root.end_of_word:
            final_list.append("".join(list_of_chars))

        for child in root.children:
            self._dfs_helper(child, list_of_chars, final_list)
        del list_of_chars[-1]

    # expected return value: list of strings
    def get_all_words(self):
        all_words = []

        self._dfs_helper(self.root, [], all_words)

        return all_words

    # expected return value: list of strings else []
    def get_all_words_prefix(self, prefix):

        all_words = []

        return all_words

    def print_trie(self):
        i = 0
        for child in self.root.children:
            if child:
                print (i, chr(97 + i))
            i += 1


my_trie = Trie()
my_trie.insert_word("nikita")
my_trie.insert_word("sid")
my_trie.insert_word("abba")
my_trie.insert_word("jabba")
my_trie.insert_word("rabba")
print (my_trie.exists("sid"))
print (my_trie.exists("sido"))
print (my_trie.get_all_words())






