const n = 8;

function solution(n) {
    if (n === 0) return 0;
    let prev1 = 0;
    let prev2 = 1;
    for (let i = 2; i <= n; i++) {
        let r = prev1 + prev2;
        prev1 = prev2;
        prev2 = r;
    }
    return prev2;
};

console.log(solution(n));