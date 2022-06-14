def priority_max(point_a, point_b, a_index, b_index):
    priority_index = "5462310"
    ai = priority_index.find(str(a_index))
    bi = priority_index.find(str(b_index))
    if ai < bi:
        return point_a, a_index
    elif ai > bi:
        return point_b, b_index


def priority_min(point_a, point_b, a_index, b_index):
    priority_index = "5462310"
    ai = priority_index.find(str(a_index))
    bi = priority_index.find(str(b_index))
    if ai > bi:
        return point_a, a_index
    elif ai < bi:
        return point_b, b_index


def solution(data):
    sky_code = {1: 20, 2: 20, 3: 17, 4: 10}
    rain_code = {0: 0, 1: 5, 2: 14}
    score = []
    recommend = []
    non_recommend = []
    answer = []

    # 요일 별 점수를 계산해서 score 배열에 [점수, 최악의날_bool, 요일] 리스트를 담는 로직
    for i in range(len(data)):
        least_day = False
        res = 0
        for j in range(len(data[i])):
            if j == 0:
                if data[i][j] == 3:
                    least_day = True
                sky_point = sky_code[data[i][j]]
                res += sky_point
            elif j == 1 and data[i][j] != 0:
                if data[i][j] == 1:
                    least_day = True
                res = 0
                rain_point = rain_code[data[i][j]]
                res += rain_point
            elif j == 2:
                if data[i][j] >= 30 or data[i][j] <= 0:
                    least_day = True
                weather_point = 20 - abs(22 - data[i][j])
                res += weather_point
        score.append([res, least_day, i])

    answer = []
    max_point, max_index = -1000000000, -1000000000
    min_point, min_index = 1000000000, 1000000000
    for i in range(len(score)):

        if score[i][0] > max_point:
            max_point = score[i][0]
            max_index = score[i][2]
        elif score[i][0] == max_point:
            prior_point, prior_index = priority_max(max_point, score[i][0], max_index, score[i][2])
            max_point = prior_point
            max_index = prior_index

        if score[i][0] < min_point:
            min_point = score[i][0]
            min_index = score[i][2]
        elif score[i][0] == min_point:
            prior_point_2, prior_index_2 = priority_min(min_point, score[i][0], min_index, score[i][2])
            min_point = prior_point_2
            min_index = prior_index_2

    answer.append(max_index)
    answer.append(min_index)
    print(score)
    return answer


print(solution([[1,0,11],[3,1,15],[2,0,16],[4,0,17],[2,0,15],[2,1,14],[2,0,12]]))
print(solution([[4,0,12],[1,0,16],[3,0,18],[3,0,17],[2,0,15],[3,2,22],[2,1,17]]))