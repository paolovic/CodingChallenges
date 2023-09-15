class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie["isWord"] = True

    def dfs(self, trie: object, word: str, index: int):
        if index == len(word):
            return "isWord" in trie

        if word[index] == ".":
            for key in trie:
                if key!="isWord" and self.dfs(trie[key], word, index + 1):
                    return True
            return False
        elif word[index] in trie:
            return self.dfs(trie[word[index]], word, index + 1)
        else:
            return False

    def search(self, word: str) -> bool:
        return self.dfs(self.trie, word, 0)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word = ""
obj.addWord(word)
word = "and"
obj.addWord(word)
word = "dad"
obj.addWord(word)
word = "mad"
obj.addWord(word)
word = "bat"
print(obj.trie)
obj.addWord(word)
print(obj.search(word))
word = "a.d"
print(obj.search(word))
word = "bad"
print(obj.search(word))
word = "dad"
print(obj.search(word))
word = "mad"
print(obj.search(word))
word = "pad"
print(obj.search(word))
