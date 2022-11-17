import json, requests
from time import sleep

def request():
    response = requests.get(f'https://api.pi.delivery/v1/pi?start={piStart}&numberOfDigits=900')
    json_data = json.loads(response.text)
    return str(json_data['content'])

list = []
charactersNumber = 21
piStart = 172833600

print('running')
print(100*'-')

while True:

    while True:
        try:
            pi = request()
            break
        except:
            sleep(2)
            print(f'PiStart now is -> {piStart}')
            print('Erro, trying again')
            print(20*'-')
            
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

    piStart += 800
    if(len(list) > 0):
        break

print(100*'-')
print(f'number: {list[0]}')
print(100*'-')
print('finished')