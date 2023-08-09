const arr = [-10, -8, -3, 3, 4, 5];

let left = 0;
let right = arr.length-1;

while(left < right){
    const sum = arr[left] + arr[right];
    if(sum === 0){
        console.log("left: " + arr[left] + ", right: " + arr[right]);
        break;
    }
    else if(sum < 0){
        left++;
    }
    else{
        right--;
    }
}