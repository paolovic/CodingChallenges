/*
                5
                /   \
               4     8
               /     / \
              11    13  4
              / \        \
             7   2        1
*/

const tree = {
    value: 5,
    left: {
        value: 4,
        left: {
            value: 11,
            left: {
                value: 7,
                left: null,
                right: null
            },
            right: {
                value: 2,
                left: null,
                right: null
            }
        },
        right: null
    },
    right: {
        value: 8,
        left: {
            value: 13,
            left: null,
            right: null
        },
        right: {
            value: 4,
            left: null,
            right: {
                value: 1,
                left: null,
                right: null
            },
        }
    }
};

let targetSum = 23;

function pathSum(root, targetSum) {
    if (!root) return false;

    targetSum -= root.value;

    if (!root.left && !root.right && targetSum === 0) return true;

    return pathSum(root.left, targetSum) || pathSum(root.right, targetSum);
};


console.log(pathSum(tree, targetSum));