var subsets = function(nums){
    let result = [[]];

    function recurse(index, currArr){
        for(let i=index; i<nums.length; i++){
            currArr.push(nums[i]);
            result.push([...currArr]);
            recurse(i+1, currArr);
            currArr.pop();
        }
    }
    recurse(0, []);
    return result;
};

const nums1 = [1, 2, 3];
console.log(subsets(nums1));
// Expected Output
// [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

const nums2 = [0];
console.log(subsets(nums2));
// Expected Output
// [[],[0]]
