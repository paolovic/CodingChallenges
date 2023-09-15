
var topKFrequent = function (nums, k) {
    let map = {}
    let bucket = []
    let res = []

    for (let i = 0; i < nums.length; i++) {
        map[nums[i]] = map[nums[i]] ? map[nums[i]] + 1 : 1
    }

    for (let [num, freq] of Object.entries(map)) {
        if (!bucket[freq]) {
            bucket[freq] = new Set().add(num)
        } else {
            bucket[freq].add(num)
        }
    }

    for (let i = bucket.length - 1; i >= 0; i--) {
        if (bucket[i]) res.push(...bucket[i])
        if (res.length === k) break
    }

    return res
};

nums = [1, 1, 1, 2, 2, 3]
k = 2
console.log(topKFrequent(nums, k))