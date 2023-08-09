let nums = [-1, 0, 3, 5, 9];
let target = 9;

function binarySearch(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((right + left) / 2);
        if (nums[mid] === target) {
            return mid;
        }
        if (nums[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return -1;
};

console.log(binarySearch(nums, target));