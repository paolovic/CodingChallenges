const nums = [1, 2, 3];

function solution(nums, arr = [], res = []) {
    if (nums.length === 0) res.push([...arr]);

    for (let i = 0; i < nums.length; i++) {
        arr.push(nums[i]);
        let rest = nums.filter((_, index) => index !== i);
        solution(rest, arr, res);
        arr.pop()
    }

    return res;
};

console.log(solution(nums));