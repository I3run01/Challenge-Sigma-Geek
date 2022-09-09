from piNumber import pi
import json, requests
import math

list = []
charactersNumber = 9
piStart = 0

print('running')
print('')

while True:
    response = requests.get(f'https://api.pi.delivery/v1/pi?start={piStart}&numberOfDigits=100')
    json_data = json.loads(response.text)
    pi = str(json_data['content'])
    start = 0

    while start <= (len(pi)-charactersNumber):
        stringNum = pi[start: start + charactersNumber]

        repeatLetter = 0
        for c in range (0, round((charactersNumber/2)+0.1)):
            if(stringNum[c] == stringNum[(charactersNumber-1)-c]):
                repeatLetter += 1
            else:
                break

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

    piStart += 80
    if(len(list) > 0):
        break
    

if(len(list) > 0):
    print(f'number: {list[0]}')

else:
    print('no number was found')
print('')
print('finished')