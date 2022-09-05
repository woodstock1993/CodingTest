def get_next(series):
    num = series[0]
    series_next = []
    num_count = 0

    for i in series:
        if i is num:
            num_count += 1
        else:
            series_next.append(num)
            series_next.append(num_count)
            num = i
            num_count = 1

    series_next.append(num)
    series_next.append(num_count)

    return series_next

def solution(n):
    series = [1]

    for i in range(0, n):
        strs = ""
        for j in series:
            strs += str(j)
        series = get_next(series)

    return strs