def solution(C, F, X):
    hire_number = 0
    host_time = X / 2
    host_alba_time = (C / 2) + X / (2 + F)

    if host_time <= host_alba_time:
        return round(host_time, 6)

    host_alba_time_2 = (C / 2) + (C / (2 + F)) + (X / (2 + 2 * F))
    if host_alba_time <= host_alba_time_2:
        return round(host_alba_time, 6)

    host_alba_time_3 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (X / (2 + 3 * F))
    if host_alba_time_2 <= host_alba_time_3:
        return round(host_alba_time_2, 6)

    host_alba_time_4 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (X / (2 + 4 * F))
    if host_alba_time_3 <= host_alba_time_4:
        return round(host_alba_time_3, 6)

    host_alba_time_5 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                X / (2 + 5 * F))
    if host_alba_time_4 <= host_alba_time_5:
        return round(host_alba_time_4, 6)

    host_alba_time_6 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (X / (2 + 6 * F))
    if host_alba_time_5 <= host_alba_time_6:
        return round(host_alba_time_5, 6)

    host_alba_time_7 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (C / (2 + 6 * F)) + (X / (2 + 7 * F))
    if host_alba_time_6 <= host_alba_time_7:
        return round(host_alba_time_6, 6)

    host_alba_time_8 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (C / (2 + 6 * F)) + (C / (2 + 7 * F)) + (X / (2 + 8 * F))
    if host_alba_time_7 <= host_alba_time_8:
        return round(host_alba_time_7, 6)

    host_alba_time_9 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (C / (2 + 6 * F)) + (C / (2 + 7 * F)) + (C / (2 + 8 * F)) + (X / (2 + 9 * F))
    if host_alba_time_8 <= host_alba_time_9:
        return round(host_alba_time_8, 6)

    host_alba_time_10 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (C / (2 + 6 * F)) + (C / (2 + 7 * F)) + (C / (2 + 8 * F)) + (C / (2 + 9 * F)) + (
                                    X / (2 + 10 * F))
    if host_alba_time_9 <= host_alba_time_10:
        return round(host_alba_time_9, 6)

    host_alba_time_11 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (C / (2 + 6 * F)) + (X / (2 + 7 * F)) + (C / (2 + 8 * F)) + (C / (2 + 9 * F)) + (
                                    C / (2 + 10 * F)) + (X / (2 + 11 * F))
    if host_alba_time_10 <= host_alba_time_11:
        return round(host_alba_time_10, 6)

    host_alba_time_12 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (C / (2 + 6 * F)) + (X / (2 + 7 * F)) + (C / (2 + 8 * F)) + (C / (2 + 9 * F)) + (
                                    C / (2 + 10 * F)) + (C / (2 + 11 * F)) + (X / (2 + 12 * F))
    if host_alba_time_11 <= host_alba_time_12:
        return round(host_alba_time_11, 6)

    host_alba_time_13 = (C / 2) + (C / (2 + F)) + (C / (2 + 2 * F)) + (C / (2 + 3 * F)) + (C / (2 + 4 * F)) + (
                C / (2 + 5 * F)) + (C / (2 + 6 * F)) + (X / (2 + 7 * F)) + (C / (2 + 8 * F)) + (C / (2 + 9 * F)) + (
                                    C / (2 + 10 * F)) + (C / (2 + 11 * F)) + + (C / (2 + 12 * F))(X / (2 + 13 * F))
    if host_alba_time_12 <= host_alba_time_13:
        return round(host_alba_time_12, 6)


