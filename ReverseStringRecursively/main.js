const str = 'hello';

function solution(str) {
    if (str == "") { return str }

    return str[str.length-1] + solution(str.slice(0, str.length-1));
}

console.log(solution(str));