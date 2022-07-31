def solution(cookie):
    cookie_length = len(cookie)
    answer = -1
    for i in range(cookie_length-1):
        l_i = i
        r_i = i+1
        l_sum = cookie[l_i]
        r_sum = cookie[r_i]
        while l_i != 0 or r_i != cookie_length-1:
            if l_sum == r_sum:
                delta = r_i - l_i + 1
                if delta > answer:
                    answer = delta
            if l_sum >= r_sum and r_i+1 <= cookie_length-1:
                r_sum += cookie[r_i+1]
                r_i += 1
            elif l_sum >= r_sum and l_i-1 >= 0:
                l_sum += cookie[l_i-1]
                l_i -= 1
            elif l_sum < r_sum and l_i-1 >= 0:
                l_sum += cookie[l_i-1]
                l_i -= 1
            if l_i == 0 and l_sum < r_sum:
                break
            if r_i == cookie_length-1 and l_sum > r_sum:
                break
            if l_i == 0 and r_i == cookie_length-1 and l_sum == r_sum:
                delta = r_i - l_i + 1
                if delta > answer:
                    answer = delta
    return answer


print(solution([1, 250, 1, 250, 500, 500]))