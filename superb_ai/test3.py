def solution(words):
    res = []
    if len(''.join(words)) == len(words):
        return ''.join(words)

    word_length = 10**9
    for string in words:
        arr = list(string)
        for char in arr:
            if word_length > len(char):
                word_length = len(char)
            elif word_length < len(char):
                return ""
            if char not in res:
                res.append(char)
    res = ''.join(res)
    print(res)


# solution(["xz", "xy", "z"])
solution(["x", "y", "xz"])