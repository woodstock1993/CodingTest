// 괄호 대칭 판별 함수
function ppang(bracket) {
    let s = [...bracket]
    for (let i = 0; i <= s.length; i++) {
        for (let i = 0; i <= s.length; i++) {
            for (let j = 0; j < s.length-1; j++) {
                if (s[j] === '(' && s[j+1] === ')') {s.splice(j,2)}
                else if (s[j] === '[' && s[j+1] === ']') {s.splice(j,2)}
                else if (s[j] === '{' && s[j+1] === '}') {s.splice(j,2)}
            }
        }
    }
    if (s == "") return true
    else return false
}


// 유효한 괄호인지 아닌지 판별해주는 함수, 유효하지 않을 경우 부족한 괄호 정보를 알려준다.
function isRightBracket(s) {
    let b1_c = 0;
    let b2_c = 0;
    let b3_c = 0;

    let b1_check = '';
    let b2_check = '';
    let b3_check = '';

    let res2 = {'open1': 0, 'open2': 0, 'open3': 0}

    for (let i = 0; i < s.length; i++) {
        // 괄호 개수 세기 전, 여는 입구가 나왔는지 체크해 주는 부문; 여는 괄호가 선행해서 나왔을 때 닫는 괄호 -1 카운트 할 수 있음
        if (s[i] === '(') {
            b1_check = "open";
            res2['open1'] += 1
        } else if (s[i] === '[') {
            b2_check = "open";
            res2['open2'] += 1
        } else if (s[i] === '{') {
            b3_check = "open";
            res2['open3'] += 1
        }
        else if (s[i] === ')'  && res2['open1'] > 0 && b1_check === 'open') {
            res2['open1'] -= 1
            if (res2['open1'] === 0) {b1_check = 'closed'}
        }
        else if (s[i] === ']'  && res2['open2'] > 0 && b2_check === 'open') {
            res2['open2'] -= 1
            if (res2['open2'] === 0) {b2_check = 'closed'}
        }
        else if (s[i] === '}'  && res2['open3'] > 0 && b3_check === 'open') {
            res2['open3'] -= 1
            if (res2['open3'] === 0) {b3_check = 'closed'}
        }

        // 여는괄호와 닫는 괄호의 개수가 일치하는지 판별하기 위해 쓰이는 변수들
        if (s[i]==='(') {
            b1_c += 1;
        } else if (s[i] === ')') {
            b1_c -=1;
        } else if (s[i] === '[') {
            b2_c += 1;
        } else if (s[i] === ']') {
            b2_c -= 1;
        } else if (s[i] === '{') {
            b3_c += 1;
        } else if (s[i] === '}') {
            b3_c -= 1;
        }
    }

    /*
     1. 여는괄호가 선행해서 나왔을 때 닫는 괄호가 선행하는 괄호만큼 나오는지 체크하고,
     2. 여는 괄호와 닫는 괄호 개수가 서로 짝이 맞는지 확인하고
     3. 해당 괄호가 서로 대칭일 때 참을 반환한다.
    */
    if (res2['open1'] === 0 && res2['open2'] === 0 && res2['open3'] === 0
            && (b1_c === 0) && (b2_c === 0) && (b3_c === 0)
            && (b1_check !== 'open') && (b2_check !== 'open')  && (b3_check !== 'open')
            && (ppang(s) === true)
            ) {
        return true;
    } else return [false, b1_c, b2_c, b3_c];
}


function solution(s) {
    let info = isRightBracket(s);
    let bracket = '';
    if (info[0] !== false) return 0;

    // 조건에 부합하는 괄호가 아닐 때 부족한 괄호를 지정해 주는 부문
    if (info[1] > 0) bracket = ')';
    else if (info[1] < 0) bracket = '(';
    else if (info[2] > 0) bracket = ']';
    else if (info[2] < 0) bracket = '[';
    else if (info[3] > 0) bracket = '}';
    else if (info[3] < 0) bracket = '{';

    // 완전탐색으로 부족한 괄호를 기존의 문자 곳곳에 넣어서 해당 문자가 조건에 부합하는 괄호일 때 count한다.
    let answer = 0;
    for(let i = 0; i <= s.length; i++) {
        let temp = s;
        temp = [...temp];
        temp.splice(i, 0, bracket);
        temp = temp.join().replace(/,/g, '')
        if (isRightBracket(temp) === true) answer += 1
    }
    return answer;
}