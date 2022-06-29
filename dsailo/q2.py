def solution(cookie):
    cookie_length = len(cookie)
    answer = 0

    for i in range(cookie_length-1):
        left = i
        right = i+1
        l_sum = 0
        r_sum = 0

        l_sum += cookie[left]
        r_sum += cookie[right]

        while(1):
            if l_sum == r_sum and answer < l_sum:
                answer = l_sum
            elif l_sum < r_sum and left != 0:
                left -= 1
                l_sum += cookie[left]
            elif r_sum <= l_sum and right != cookie_length -1:
                right += 1
                r_sum += cookie[right]
            else:
                break

    return answer