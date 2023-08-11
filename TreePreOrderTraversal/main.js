const tree = {
    val: 2,
    left: {
        val: 1,
        left: null,
        right: null
    },
    right: {
        val: 3,
        left: null,
        right: null
    }
};

/*
          2
         / \
        1   3
*/

let arr = [];

function preOrderTraversal(tree, arr) {
    if(!tree) return null;
    arr.push(tree.val);
    preOrderTraversal(tree.left, arr);
    preOrderTraversal(tree.right, arr);
    return arr;
};

console.log(preOrderTraversal(tree, arr)); // [2,1,3]