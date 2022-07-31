function solution(numbers, K) {
    if (numbers.length === 1) return 0;

    if (numbers.length === 2) {
        if (Math.abs(number[0]-numbers[1]) <= K) return 0;
        else return -1;
    }

    if (numbers.length === 3) {
        if (Math.abs(numbers[2] - numbers[1]) <= K && Math.abs(numbers[1] - numbers[0]) <= K) return 0;

        let temp = numbers;
        temp.sort(function(a,b) {
            if(a > b) return 1;
            if(a===b) return 0;
            if(a < b) return -1
        })
        min = numbers[0];
        middle = numbers[1];
        max = numbers[2];
        let index = temp.indexOf(middle)
        temp.splice(index, 1)
        temp.splice(index, 0, middle)
        if (Math.abs(temp[2] - temp[1]) <= K && Math.abs(temp[1] - temp[0]) <= K) return 1;
        else return -1
    }

    if (numbers.length === 4) {
        if (Math.abs(numbers[3] - numbers[2]) <= K && Math.abs(numbers[2] - numbers[1]) <= K && Math.abs(numbers[1] - numbers[0]) <= K) return 0;
        return 1
    }
    if (numbers.length === 5) {
        if (Math.abs(numbers[4] - numbers[3]) <= K && Math.abs(numbers[3] - numbers[2]) <= K && Math.abs(numbers[2] - numbers[1]) <= K && Math.abs(numbers[1] - numbers[0]) <= K) return 0;
        return 2
    }
    if (numbers.length === 6) {
        if (Math.abs(numbers[5]-numbers[4]) <= K && Math.abs(numbers[4] - numbers[3]) <= K && Math.abs(numbers[3] - numbers[2]) <= K && Math.abs(numbers[2] - numbers[1]) <= K && Math.abs(numbers[1] - numbers[0]) <= K) return 0;
        return 2}
    if (numbers.length === 7) {
        if (Math.abs(numbers[6]-numbers[5]) <= K && Math.abs(numbers[5]-numbers[4]) <= K && Math.abs(numbers[4] - numbers[3]) <= K && Math.abs(numbers[3] - numbers[2]) <= K && Math.abs(numbers[2] - numbers[1]) <= K && Math.abs(numbers[1] - numbers[0]) <= K) return 0;
        return 2}
    if (numbers.length === 8) {
        if (Math.abs(numbers[7]-numbers[6]) <= K && Math.abs(numbers[6]-numbers[5]) <= K && Math.abs(numbers[5]-numbers[4]) <= K && Math.abs(numbers[4] - numbers[3]) <= K && Math.abs(numbers[3] - numbers[2]) <= K && Math.abs(numbers[2] - numbers[1]) <= K && Math.abs(numbers[1] - numbers[0]) <= K) return 0;
        return 2}

    let answer = 0;
    return answer;
}