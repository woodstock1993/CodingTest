cookie = [1,1,2,3]
cookie2 = [1,2,4,5]


def solution(cookie):
    length = len(cookie)-1
    dp = [0] * length
    for i in range(length):
        left_cookie = cookie[i]
        right_cookie = cookie[i+1]

        left_index = i
        right_index = i+1

        while left_index >= 0 and right_index <= length:
            if left_index == 0 and right_index == length:
                if left_cookie == right_cookie:
                    dp[i] = left_cookie
                    break
            if left_index < 0 or right_index > length:
                break
            if left_cookie > right_cookie and right_index == length:
                break
            if left_cookie < right_cookie and left_index == 0:
                break
            if left_cookie == right_cookie:
                dp[i] = left_cookie
                if left_index != 0:
                    left_index -= 1
                    left_cookie += cookie[left_index]
                elif right_index != length:
                    right_index += 1
                    right_cookie += cookie[right_index]

            elif left_cookie > right_cookie:
                right_index += 1
                if right_index > length:
                    break
                right_cookie += cookie[right_index]

            elif left_cookie < right_cookie:
                left_index -= 1
                if left_index < 0:
                    break
                left_cookie += cookie[left_index]

    return max(dp)


print(solution(cookie2))