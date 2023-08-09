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

var minDepth = function (root) {
    if (!root) return 0;
    let queue = [root];
    let depth = 1;

    while(queue.length>0){
        let levelSize = queue.length;
        for(let i=0; i<levelSize; i++){
            let node = queue.shift();
            if(!node.left && !node.right){
                return depth;
            }
            if(node.left){
                queue.push(node.left);
            }
            if(node.right){
                queue.push(node.right);
            }
        }
        depth++;
    }
}

console.log(minDepth(tree1));