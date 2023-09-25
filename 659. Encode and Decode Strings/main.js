/**
 * Encodes a list of strings to a single string.
 * 
 * @param {string[]} strs
 * @return {string}
 */

var encode = function (strs) {
    let encoded = strs.join("_$$_");
    return encoded;
};

/**
 * Decodes a single string to a list of strings.
 * 
 * @param {string} s
 * @return {string[]}
 */

var decode = function (s) {
    let decoded = s.split("_$$_");
    return decoded;
};

//Test Case 1
var input = ["Hello", "World", ",", "how", "are", "you"];
var encoded = encode(input);
console.log(encoded);
var decoded = decode(encoded);
console.log(decoded);
// Expected Output: ["Hello", "World", "how", "are", "you"]