/**
 * @param {TreeNode} root
 * @return {number}
 */

var goodNodes = function (root) {
    if(!root) return 0;
    let count = 0;
    function recurse(root, max){
        if(!root) return;
        if(root.val >= max) {
            count++;
            max = root.val;
        }
        recurse(root.left, max);
        recurse(root.right, max);
    }
    recurse(root, root.val);
    return count;
};

// Tree structure for test case 1
//      3
//     / \
//    1   4
//   / \   \
//  3   1   5

const tree1 = {
    val: 3,
    left: {
        val: 1,
        left: {
            val: 3,
            left: null,
            right: null
        },
        right: {
            val: 1,
            left: null,
            right: null
        }
    },
    right: {
        val: 4,
        left: null,
        right: {
            val: 5,
            left: null,
            right: null
        }
    }
}

console.log(goodNodes(tree1)); // 4
