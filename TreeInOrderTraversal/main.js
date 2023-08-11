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

function inOrderTraversal(tree, arr) {
    if(!tree) return null;
    inOrderTraversal(tree.left, arr);
    arr.push(tree.val);
    inOrderTraversal(tree.right, arr);
    return arr;
};

console.log(inOrderTraversal(tree, arr)); // [2,1,3]