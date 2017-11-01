# tst
Ternary Search Tree - Auto Complete Feature

### Pros

- More memory efficient than naive trie implementation.
- Decent search time for a prefix: O(klogn)
  - where k is the length of the word
  - and n is the height of the tree
- For Partial matches, approximation matching, near-neighbor lookups

### Cons

- Slower search than naive trie. 
  - Native trie always search in O(K) 
  - where k is a length of a word.

### Complexity

|        |  Average | Worst |
|--------|---------:|-------|
| lookup | O(log n) | O(n)  |
| insert | O(log n) | O(n)  |
| delete | O(log n) | O(n)  |

where n is height of the Ternary Tree, and base is three

Space : O(n) , where n is a length of a word

