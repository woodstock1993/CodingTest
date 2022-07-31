import re


def ArrayChallenge(strArr):
    # input()안 원소 문자열 정리
    arr = []
    for i in range(len(strArr)):
        li = re.split(r'[(),]', strArr[i])
        del li[0]
        del li[-1]
        li = list(map(int, li))
        arr.append(li)

    # 자식 입장에서 부모 리스트를 값으로 갖는 딕셔너리 생성
    dic = {}
    for i in range(len(arr)):
        if arr[i][0] not in dic:
            dic[arr[i][0]] = [arr[i][1]]
        else:
            dic[arr[i][0]].append(arr[i][1])
    # print(dic)

    # 위에서 생성한 딕셔너리가 갖는 값을 숫자로 환원
    dic_ = {}
    for k, v in dic.items():
        if k not in dic_:
            dic_[k] = len(v)

    print(dic_)

    # 자식이 2개의 부모를 가질 때 False 리턴
    dic_ = sorted(dic_.items(), key=lambda x: x[1], reverse=True)
    if len(dic_) >= 1:
        if dic_[0][1] >= 2:
            return False

    # 부모 입장에서 자식의 수를 값으로 하는 딕셔너리 생성
    new_dic = {}
    for k, v in dic.items():
        if v[0] not in new_dic:
            new_dic[v[0]] = 1
        else:
            new_dic[v[0]] += 1

    # 부모 중 하나라도 3명 이상의 자식을 가질 때 False 리턴
    new_dic = sorted(new_dic.items(), key=lambda x: x[1], reverse=True)

    # print(new_dic)

    if len(new_dic) >= 1:
        if new_dic[0][1] >= 3:
            return False
        return True
    return True


# keep this function call here
# print(ArrayChallenge(
#     ["(2,1)", "(3,1)", "(4,2)", "(5,2)", "(6,3)", "(7,3)", "(8,4)", "(9,4)", "(10,5)", "(11,5)", "(12,6)", "(13,6)",
#      "(14,6)"]))
# print(ArrayChallenge(["(1,2)", "(1,3)"]))
# print(ArrayChallenge(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))