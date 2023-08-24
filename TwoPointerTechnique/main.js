const nums = [-10, -8, -3, 3, 4, 5];

let left = 0;
let right = nums.length - 1;

while (left < right) {
    if (nums[left] + nums[right] === 0) {
        console.log("left: " + nums[left] + ", right: " + nums[right]);
        break;
    }
    if (nums[left] + nums[right] > 0) right--;
    else left++;
}
