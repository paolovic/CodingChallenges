var rightSideView = function (root) {
    if(!root) return [];

    let queue = [root];

    let res = [];

    while(queue.length){
        let levelsize = queue.length;
        for(let i=0; i<levelsize; i++){
            let current = queue.shift();
            if(i === levelsize-1){
                res.push(current.val)
            }
            if(current.left){
                queue.push(current.left);
            }
            if(current.right){
                queue.push(current.right);
            }
        }
    }
    return res;
};

/*
    1
    / \
    2   3
     \   \
      5   4
*/

const tree1 = {
    val: 1,
    left: {
        val: 2,
        left: null,
        right: {
            val: 5,
            left: null,
            right: null
        }
    },
    right: {
        val: 3,
        left: null,
        right: {
            val: 4,
            left: null,
            right: null
        }
    }
};

console.log(rightSideView(tree1));