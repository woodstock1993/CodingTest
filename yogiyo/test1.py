def solution(S):
    if len(S) <= 0:
        return False
    if 'a' in S and 'b' not in S:
        return True
    if 'b' in S and 'a' not in S:
        return True
    start = S[0]
    start_b_index = -1
    if start == 'b':
        return False
    for i in range(1, len(S)):
        if S[i] == 'b':
            i = start_b_index
            break
    if 'a' in S[start_b_index:]:
        return False
    return True


print(solution('babababa'))