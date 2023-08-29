/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */

var lowestCommonAncestor = function (root, p, q) {
    if(!root) return null;
    if(root.val > p.val && root.val > q.val){
        return lowestCommonAncestor(root.left, p, q);
    }
    else if(root.val < p.val && root.val < q.val){
        return lowestCommonAncestor(root.right, p, q);
    }
    else{
        return root;
    }
};

/*
        6
        / \
       2   8
     / \    / \
    0  4    7  9
      / \
      3  5    
*/

const tree1 = {
    val: 6,
    left: {
        val: 2,
        left: {
            val: 0,
            left: null,
            right: null
        },
        right: {
            val: 4,
            left: {
                val: 3,
                left: null,
                right: null
            },
            right: {
                val: 5,
                left: null,
                right: null
            }
        }
    },
    right: {
        val: 8,
        left: {
            val: 7,
            left: null,
            right: null
        },
        right: {
            val: 9,
            left: null,
            right: null
        }
    }
};

const p1 = { val: 2, left: null, right: null };
const q1 = { val: 8, left: null, right: null };

let startTime = performance.now(); 
let node = lowestCommonAncestor(tree1, p1, q1);
let endTime = performance.now(); 
let timeElapsed = endTime - startTime;

console.log("Lowest Common Ancestor: " + JSON.stringify(node, null, 2) + " in " + timeElapsed + "ms")

