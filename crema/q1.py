def getFinalString(s):
    cnt = 0
    while 'AWS' in s:
        s = s.replace('AWS', '')
        cnt += 1
    if cnt == 0:
        print(-1)
    elif s == '':
        print('null')
    else:
        print(s)


getFinalString("AAWSWS")