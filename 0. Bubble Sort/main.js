const nums = [3, 6, 2, 4, 1, 5];

function bubble(nums) {
    for (let i = nums.length - 1; i >= 1; i--) {
        for (let j = 1; j <= i; j++) {
            if (nums[j] < nums[j - 1]) {
                [nums[j], nums[j - 1]] = [nums[j - 1], nums[j]];
            }
        }
    }
    return nums;
};

console.log(bubble(nums));