def solution(n, m, x_axis, y_axis):
    x_axis.insert(0, 0)
    x_axis.append(n)
    y_axis.insert(0, 0)
    y_axis.append(m)

    x_axis.sort()
    y_axis.sort()

    s = []

    for i in range(len(x_axis) - 1):
        width = x_axis[i + 1] - x_axis[i]
        for j in range(len(y_axis) - 1):
            height = y_axis[j + 1] - y_axis[j]
            s.append(width * height)

    answer = max(s)

    return answer