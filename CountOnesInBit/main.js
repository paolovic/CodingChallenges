const n = parseInt('11100101', 2); //229
const expected = 5;

function solution(n) {
    let counter = 0;
    while (n > 0) {
        counter += n & 1; //bitwise AND operator, compares the rightmost element of the number's bit representation with a 1.
        n = n >>> 1; // bitwise rightshift operator, shifts the bits to the right and appends a zero to the left. effectively integer division by 2.
    }
    return counter;
};

const result = solution(n);
if (result === expected) {
    console.log('Testcase PASSED!');
}
else {
    console.error('Testcase FAILED! Expected:', expected, ', but got:', result);
}