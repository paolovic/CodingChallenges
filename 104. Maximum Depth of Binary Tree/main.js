const tree = {
  value: 3,
  left: {
    value: 9,
    left: null,
    right: null,
  },
  right: {
    value: 20,
    left: {
      value: 15,
      left: null,
      right: null,
    },
    right: {
      value: 7,
      left: null,
      right: null,
    },
  },
};

/*                      3
                     /\
              9            20
              /\           /\
          null null     15         7 
                        /\          /\   
                    null null       null null
*/

/*function maxDepth(root) {
  if(root===null) return 0;
  return Math.max(maxDepth(root.right), maxDepth(root.left))+1
}*/

function maxDepth(root) {
  let max = 0;

  function dfs(node, depth) {
    if (node === null) return 0;
    if (depth > max) {
      max = depth;
    }
    dfs(node.left, depth + 1);
    dfs(node.right, depth + 1);
  }
  dfs(root, 1);
  return max;
}

console.log(maxDepth(tree))






