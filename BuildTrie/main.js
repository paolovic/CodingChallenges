var Trie = function () {
    this.trie = {};
};

/**
 * @param {string} word
 * @return {void}
 */

Trie.prototype.insert = function (word) {
    let trie = this.trie;
    for (let char of word) {
        if (!trie[char] || trie[char] === null) {
            trie[char] = {};
        }
        trie = trie[char];
    }
    trie.isWord = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */

Trie.prototype.search = function (word) {
    let trie = this.trie;
    for (let char of word){
        if (!trie[char] || trie[char] === null) {
            return false;
        }
        trie = trie[char];
    }
    return trie.isWord;
};

//Test Case 1: Insert and search one word
const trie1 = new Trie();
trie1.insert("apple");
//console.log("trie1", JSON.stringify(trie1, null, 2));

const trie2 = new Trie();
trie2.insert("apple");
trie2.insert("banana");
trie2.insert("carrot");
//console.log("trie2", JSON.stringify(trie2, null, 2));
console.log(trie2.search("carrot"));
console.log(trie2.search("carrot2"));