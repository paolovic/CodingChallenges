var kthSmallest = function (root, k) {
    let count=0;
    let result;

    function traverse(node){
        if(!node) return;
        traverse(node.left);
        if(++count===k) {
            result=node;
            return;
        }
        traverse(node.right);
    };
    traverse(root);
    return result;
};

/*
     3
    / \
   1   4
    \
    2
*/

const tree1 = {
    val: 3,
    left: {
        val: 1,
        left: null,
        right: {
            val: 2,
            left: null,
            right: null
        }
    },
    right: {
        val: 4,
        left: null,
        right: null
    }
};

console.log(kthSmallest(tree1, 1)); // 1