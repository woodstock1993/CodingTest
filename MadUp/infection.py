def solution(entry_log, infect):
    infection_list = []
    p_infect = infect
    n_infect = infect*-1
    office = []
    out =[]

    for i in range(len(entry_log)):
        if entry_log[i] > 0:
            office.append(entry_log[i])
            if infect in office:
                for elem in office:
                    infection_list.append(elem)
        elif entry_log[i] < 0:
            office.remove(-1*entry_log[i])

    infection_list = sorted(list(set(infection_list)))
    infection_list.remove(infect)

    return infection_list