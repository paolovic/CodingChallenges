const nums = [6, 2, 4, 3, 1, 5];

function insertion(nums) {
    for (let i = 1; i < nums.length; i++) {
        let t = nums[i];
        let j = i - 1;
        while (j >= 0 && t < nums[j]) {
            nums[j+1] = nums[j];
            j--;
        }
        nums[j+1] = t;
    }
    return nums;
};

console.log(insertion(nums));