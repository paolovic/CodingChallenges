var findMin = function (array) {
    let left = 0;
    let right = array.length - 1;

    while(left < right){
        let mid=Math.floor((right+left)/2);
        
        if(array[mid] > array[right]){
            left = mid + 1;
        }
        else{
            right = mid;
        }
    }
    return array[left];
}

console.log(findMin([3,4,5,1,2]))

console.log(findMin([4,5,6,7,0,1,2]))

console.log(findMin([11,13,15,17]))