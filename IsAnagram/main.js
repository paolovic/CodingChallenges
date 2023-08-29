var isAnagram = function (s, t) {
    if (s.length !== t.length) return false;

    let frequency = {};

    for (let c of s) {
        frequency[c] = (frequency[c] || 0) + 1;
    }

    for (let c of t) {
        if (!frequency[c] || frequency[c] === 0) return false;
        else frequency[c]--;
    }

    return true;
};

// Test Case 1
let s = "anagram";
let t = "nagaram";
let result = isAnagram(s, t);
console.log("Expected: true, Output: " + result);

// Test Case 2
s = "rat";
t = "car";
result = isAnagram(s, t);
console.log("Expected: false, Output: " + result);

// Test Case 3
s = "";
t = "";
result = isAnagram(s, t);
console.log("Expected: true, Output: " + result);

// Test Case 4
s = "aacc"
t = "ccac"
result = isAnagram(s, t);
console.log("Expected: false, Output: " + result);
