const nums = [2, 7, 11, 15]
const target = 9

function solution(nums, target) {
    let map = new Map();
    for (let i = 0; i < nums.length - 1; i++) {
        let compliment = target - nums[i];
        if (map.has(compliment)) {
            return [i, map.get(compliment)];
        }
        else {
            map.set(nums[i], i);
        }
    }
}

console.log(solution(nums, target))