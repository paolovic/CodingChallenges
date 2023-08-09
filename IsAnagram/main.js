var isAanagram = function (s, t) {
    if (s.length !== t.length) {
        return false;
    }
    let frequency = new Map();
    for (const c of s) {
        if (frequency.has(c)) {
            frequency.set(c, frequency.get(c) + 1);
        }
        else {
            frequency.set(c, 1);
        }
    }
    for (const c of t) {
        if (!frequency.get(c) || frequency.get(c) === 0) {
            return false;
        }
        frequency.set(c, frequency.get(c) - 1);
    }
    return true;
}

let s = "anagram";
let t = "agranam";
console.log(isAanagram(s, t));
//expected output: true

let s2 = "rat";
let t2 = "car";
console.log(isAanagram(s2, t2));
//expected output: false

let s3 = "";
let t3 = "";
console.log(isAanagram(s3, t3));
//expected output: true

let s4 = "a";
let t4 = "b";
console.log(isAanagram(s4, t4));
//expected output: false