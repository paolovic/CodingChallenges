var isValid = function (s) {
    if (s[0] === ')' || s[0] === ']' || s[0] === '}' || s.length % 2 !== 0) return false;

    let stack = [];
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(' || s[i] === '[' || s[i] === '{') stack.push(s[i]);
        else {
            let prev = stack.pop();
            if (s[i] === ')' && prev !== '(') return false;
            if (s[i] === ']' && prev !== '[') return false;
            if (s[i] === '}' && prev !== '{') return false;
        }
    }
    return stack.length === 0;
};

let s1 = "()";
console.log(isValid(s1));

let s2 = "[]";
console.log(isValid(s2));

let s3 = "}";
console.log(isValid(s3));

let s4 = "({[]}";
console.log(isValid(s4));