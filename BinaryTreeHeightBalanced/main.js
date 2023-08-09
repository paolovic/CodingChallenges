var isBalanced = function (root) {
    function dfs(root) {
        if (root === null) {
            return 0;
        }
        const depth_left = dfs(root.left); // Calculate the depth of the left subtree
        const depth_right = dfs(root.right); // Calculate the depth of the right subtree

        // Check if the current node is balanced
        if (Math.abs(depth_left - depth_right) > 1) {
            return -1;
        }

        // Return the maximum depth of the left and right subtrees from the current node
        return Math.max(depth_left, depth_right) + 1;
    }

    return dfs(root) !== -1; // Check if the tree is balanced
};

//Tree structure
//          1
//        /     \
//       2      3
//      / \     / \
//     4   5   6   7

let root1 = {
    val: 1,
    left: {
        val: 2,
        left: {
            val: 4,
            left: null,
            right: null,
        },
        right: {
            val: 5,
            left: null,
            right: null,
        },
    },
    right: {
        val: 3,
        left: {
            val: 6,
            left: null,
            right: null,
        },
        right: {
            val: 7,
            left: null,
            right: null,
        },
    },
    /*right : null*/
    /*right: {
        val: 3,
        left: null,
        right: null,
    },*/
}

console.log(isBalanced(root1));