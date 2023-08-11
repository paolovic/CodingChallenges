const tree = {
    value: 2,
    left: {
        value: 1,
        left: null,
        right: null
    },
    right: {
        value: 3,
        left: null,
        right: null
    }
}

/*
     2
    / \
   1   3

    Post Order Traversal: 1, 3, 2
*/

let arr = [];

function postOrderTraversal(tree, arr) {
    if (!tree) { return; }
    postOrderTraversal(tree.left, arr);
    postOrderTraversal(tree.right, arr);
    arr.push(tree.value);
    return arr;
};

console.log(postOrderTraversal(tree, arr)); // [1, 3, 2]