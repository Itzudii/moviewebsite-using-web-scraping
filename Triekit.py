class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.children.setdefault(ch, TrieNode())
        curr.is_end = True

    def _collect_words(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)
        for ch, child in node.children.items():
            self._collect_words(child, prefix + ch, result)

    def search(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return []  # No words with this prefix
            curr = curr.children[ch]
        result = []
        self._collect_words(curr, prefix, result)
        return result