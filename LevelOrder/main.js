/**
 * @param {TreeNode} root
 * @return {[][]}
 */

var levelOrder = function (root) {
    if (!root) return [];

    let queue = [root];
    let res = [];

    while (queue.length > 0) {
        let level = [];
        let levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            let node = queue.shift();
            level.push(node.val);
            if (node.left !== null) {
                queue.push(node.left);
            }
            if (node.right !== null) {
                queue.push(node.right);
            }
        }
        res.push(level);
    }
    return res;
};

/**
 *       3
 *      / \
 *      9  20
 *         / \
 *        15  7
 */

// Test case 1
const tree1 = {
    val: 3,
    left: {
        val: 9,
        left: null,
        right: null
    },
    right: {
        val: 20,
        left: {
            val: 15,
            left: null,
            right: null
        },
        right: {
            val: 7,
            left: null,
            right: null
        }
    }
};

console.log(levelOrder(tree1));