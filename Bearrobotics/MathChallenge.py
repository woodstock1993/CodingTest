from collections import deque


def MathChallenge(strParam):
    strParam = list(strParam.split())
    number_sample = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    op_sample = ['+', '-', '*', '/']
    length = len(strParam)
    stack = []
    cnt = 0

    for i in range(len(strParam)):
        if strParam[i] not in op_sample:
            stack.append(int(strParam[i]))
            cnt += 1
        elif strParam[i] in op_sample:

            # 맨 마지막의 부호를 처리해 주는 부문
            if strParam[i] == '+' and i == length - 1:
                num = 0
                while stack:
                    num += stack.pop()
                return num
            elif strParam[i] == '*' and i == length - 1:
                num = 1
                while stack:
                    num *= stack.pop()
                return num
            elif strParam[i] == '-' and i == length - 1:
                queue = deque(stack)
                num = queue.popleft()
                while queue:
                    num -= queue.popleft()
                return num
            elif strParam[i] == '/' and i == length - 1:
                queue = deque(stack)
                num = queue.popleft()
                if 0 in queue:
                    return
                while queue:
                    num /= queue.popleft()
                return num

            # 중간에 부호가 나타났을 때 숫자 처리 -> 부호 이전의 숫자를 계산해서 stack에 넣는다.
            if strParam[i] == '+' and cnt > 0:
                temp = []
                while cnt:
                    temp.append(stack.pop())
                    cnt -= 1
                num = sum(temp)
                stack.append(num)
            elif strParam[i] == '*' and cnt > 0:
                temp = []
                num = 1
                while cnt:
                    temp.append(stack.pop())
                    cnt -= 1
                while temp:
                    num *= temp.pop()
                stack.append(num)
            elif strParam[i] == '-' and cnt > 0:
                temp = []
                while cnt:
                    temp.append(stack.pop())
                    cnt -= 1
                num = temp.pop()
                while temp:
                    num -= temp.pop()
                stack.append(num)
            elif strParam[i] == '/' and cnt > 0:
                temp = []
                while cnt:
                    temp.append(stack.pop())
                    cnt -= 1
                num = temp.pop()
                if 0 in temp:
                    return
                while temp:
                    num /= temp.pop()
                stack.append(num)

    return
    # code goes here


# keep this function call here
print(MathChallenge(input()))
