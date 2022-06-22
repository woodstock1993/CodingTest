"""
     가로5, 세로5 길이의 문자 출력
"""


def paint_number(string):
    for elem in string:
        elem = int(elem)
        for i in range(5):
            if elem == 1:
                print('--#--', end='')

            if elem == 2:
                if i % 2 == 0:
                    print('-###-', end='')
                elif i == 1:
                    print('---#-', end='')
                elif i == 3:
                    print('-#---', end='')

            if elem == 3:
                if i % 2 == 0:
                    print('-###-')
                else:
                    print('---#-')


paint_number('13')