const stocks = [7, 1, 5, 3, 6, 4];

function solution(stocks) {
    let min = stocks[0];
    let profit = 0;
    let buy = 0;
    let sell = 0;
    for (let i = 1; i < stocks.length; i++) {
        if (stocks[i] < min) {
            buy = i;
            min = stocks[i];
        }
        if (stocks[i] - min > profit) {
            profit = stocks[i] - min;
            sell = i;
        }
    }
    return [buy, sell];
};

console.log(solution(stocks));