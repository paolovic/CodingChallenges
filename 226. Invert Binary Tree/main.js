const tree = {
    val: 2,
    left: {
        val: 1,
        left: {
            val: 77,
            left: null,
            right: null
        },
        right: null
    },
    right: {
        val: 3,
        left: null,
        right: null
    }
}

/*
    2
    / \
    1   3
    /
   77

    2
    / \
    3   1
         \
         77
*/

function solution(node) {
    if (!node) return null;
    [node.left, node.right] = [solution(node.right), solution(node.left)];
    return node;
};

console.log(JSON.stringify(solution(tree), null, 2));