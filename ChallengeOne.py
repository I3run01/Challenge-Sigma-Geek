from piNumber import pi

start = 0
list = []
charactersNumber = 9

print('start')
while start <= (len(pi)-charactersNumber):
    stringNum = pi[start: start + charactersNumber]

    repeatLetter = 0
    for c in range (0, round((charactersNumber/2)+0.1)):
        if(stringNum[c] == stringNum[(charactersNumber-1)-c]):
            repeatLetter += 1

    if(repeatLetter == round((charactersNumber/2)+0.1)):
        num = float(stringNum)

        flag = False
        if num > 1:
            for i in range(2, int(num)):
                if(num % i) == 0:
                    flag = True
                    break
        
        if flag == False:
            list.append(num)

    start +=  1

print(list[len(list)-1])
print('finished')