"""
Ternary Search Tree

A ternary search tree is a special trie data structure where the child nodes of a standard trie are ordered as a binary search tree.


Unlike trie(standard) data structure where each node contains 26 pointers for its children, each node in a ternary search tree contains only 3 pointers:
1. The left pointer points to the node whose value is less than the value in the current node.
2. The equal pointer points to the node whose value is equal to the value in the current node.
3. The right pointer points to the node whose value is greater than the value in the current node.

reference :
http://www.geeksforgeeks.org/ternary-search-tree/
http://www.sanfoundry.com/java-program-ternary-search-tree/

"""


class TSTNode(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.eq = None
        self.endOfWord = False  # True if the character is last character of one of the words


class TernarySearchTree(object):

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return not self.root

    def makeEmpty(self):
        self.data = None

    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, 0, word)

    def _insert(self, node, idx, word):
        c = ord(word[idx])
        if not node:
            node = TSTNode(c)
        if c < node.data:
            node.left = self._insert(node.left, idx, word)
        elif c > node.data:
            node.right = self._insert(node.right, idx, word)
        else:
            if idx + 1 < len(word):
                node.eq = self._insert(node.eq, idx + 1, word)
            else:  # idx = len(word)-1
                node.endOfWord = True
        return node

    def delete(self, word):
        if not word:
            return
        self._delete(self.root, 0, word)

    def _delete(self, node, idx, word):
        if not node:
            return

        c = ord(word[idx])
        if c < node.data:
            self._delete(node.left, idx, word)
        elif c > node.data:
            self._delete(node.right, idx, word)
        else:
            # to delete a word only needs to make endOfword false
            if node.endOfWord and idx == len(word) - 1:
                node.endOfWord = False
            elif idx + 1 < len(word):
                self._delete(node.eq, idx + 1, word)

    def search(self, word):
        if not word:
            return False

        return self._search(self.root, 0, word)

    def _search(self, node, idx, word):
        if not node:
            return False

        c = ord(word[idx])
        if c < node.data:
            return self._search(node.left, idx, word)
        elif c > node.data:
            return self._search(node.right, idx, word)

        else:
            if node.endOfWord and idx == len(word) - 1:
                return True
            elif idx + 1 < len(word):
                return self._search(node.eq, idx + 1, word)
            return False
    def __repr__(self):
        rst = []
        self._travese(self.root,rst, [])
        return ",".join(map(lambda a: "".join(a),rst))
    def _travese(self,n,rst,l):
        if n:
            self._travese(n.left, rst,l)
            l.append(chr(n.data))            
            if n.endOfWord:
                rst += [list(l)]
                if not n.eq:
                    del l[:]
            self._travese(n.eq,rst,l)
            self._travese(n.right,rst,l)
            
    
        
