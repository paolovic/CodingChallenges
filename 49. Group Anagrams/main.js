var groupAnagrams = function (strs) {
    let result = [];
    let sorted = strs.map(s => s.split('').sort().join(''));
    let map = {};
    for (let i = 0; i < sorted.length; i++) {
        if (!map[sorted[i]]) map[sorted[i]] = [strs[i]];
        else {
            map[sorted[i]].push(strs[i]);
        }
    }
    return Object.values(map);
};

// Test Case 1
let input = ["eat", "tea", "tan", "ate", "nat", "bat"];
let output = groupAnagrams(input);
console.log(output);
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

//Test Case 2
input = ["listen", "silent", "below", "elbow", "state", "taste"];
output = groupAnagrams(input);
console.log(output);
// Output: [["listen","silent"],["below","elbow"],["state","taste"]]
