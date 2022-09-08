from piNumber import pi


charactersNumber = len(pi)-1

print('start')
list = []

while charactersNumber > 2:

    start = 0
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
                print(num)
                list.append(num)

        start +=  1
    charactersNumber -= 1

    if(list > 0):
        break

    
print('finished')
print(list[len(list)-1])

print(pi[charactersNumber])