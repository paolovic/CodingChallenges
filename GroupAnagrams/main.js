var groupAnagrams = function (strs) {
    let sorted = strs.map(s => sortAlphabet(s));
    indices = new Map();
    for (let i=0; i<sorted.length; i++) {
        s = sorted[i];
        if (indices.has(s)){
            indices.get(s).push(strs[i]);
        }
        else{
            indices.set(s, [strs[i]]);
        }
    }
    return indices.values();
}

function sortAlphabet(str) {
    return [...str].sort((a, b) => a.localeCompare(b)).join("");
}

//Test Case 1
let input = [
    "eat", "tea", "tan", "ate", "nat", "bat"
]
let output = groupAnagrams(input)
console.log(output)
//[["eat", "ate", "tea"], ["tan", "nat"], ["bat"]]

//Test Case 2
input = ["listen", "silent", "elbow", "below", "car", "arc"]
output = groupAnagrams(input)
console.log(output)
//[["listen", "silent"], ["elbow", "below"], ["car", "arc"]]