const isValidBST = function (root) {
    function dfs(root, min, max) {
        if (!root) return true;

        if (root.val <= min || root.val >= max) return false;

        return dfs(root.left, min, root.val) && dfs(root.right, root.val, max);
    }
    return dfs(root, -Infinity, Infinity);
};


/* Test Case 1: Simple Binary Tree
    *     2
    *    / \
    *  1   3
    *  
*/
const tree1 = {
    val: 2,
    left: {
        val: 1,
        left: null,
        right: null
    },
    right: {
        val: 3,
        left: null,
        right: {
            val: 5,
            left: null,
            right: null
        }
    }
};

console.log(isValidBST(tree1));

/* Test Case 2: Binary Tree with duplicate values
    *     2
    *    / \    
    *   2   3 
    * 
    * 
*/

const tree2 = {
    val: 2,
    left: {
        val: 2,
        left: null,
        right: null
    },
    right: {
        val: 3,
        left: null,
        right: null
    }
};

console.log(isValidBST(tree2));


