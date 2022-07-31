def drawbox(box):
    arr = []
    for i in range(box[0] + 1, box[2]):
        for j in range(box[1] + 1, box[3]):
            arr.append([i, j])
    return arr


def drawbox2(box):
    arr = []
    for i in range(box[0], box[2]):
        for j in range(box[1], box[3]):
            arr.append([i, j])
    return arr



def solution(boxes):
    answer = [0]
    ranger = [boxes[0]]
    check = False
    for i in range(1, len(boxes)):
        x, y = boxes[i][2], boxes[i][3]
        x2,y2 = boxes[i][0],boxes[i][1]
        for j in range(len(ranger)):
            rx, ry = ranger[j][2], ranger[j][3]
            if x2 > rx and y2 > ry:
                check == True
                break
        if check == False:
            answer.append(i)
        check == False
    return answer


print(solution([[1, 1, 3, 3], [2, 2, 4, 4], [1, 6, 5, 7], [3, 3, 5, 5]]))
