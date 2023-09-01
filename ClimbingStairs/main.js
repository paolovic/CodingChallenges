const stairs = 7;

/*function solution(stairs){
    if(stairs===0) return 1;
    if(stairs===1) return 1;
    return solution(stairs-2)+solution(stairs-1)
}*/

function solution(stairs){
    let prev1 = 1;
    let prev2 = 1;
    let current;
    for(let i=2; i<stairs+1;i++){
        current=prev1+prev2;
        prev1=prev2;
        prev2=current;
    }
    return current;
}

console.log(solution(stairs))