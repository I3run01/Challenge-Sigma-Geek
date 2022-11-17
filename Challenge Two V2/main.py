import json, requests
from time import sleep
from time import time
import threading

def request(value):
    response = requests.get(f'https://api.pi.delivery/v1/pi?start={value}&numberOfDigits=900')
    json_data = json.loads(response.text)
    return str(json_data['content'])

list = []

def mainFunction(piStart, piEnd, index):
    charactersNumber = 21
    primeNumbers = 0
    #inicialValue = piStart

    while True:
        start = 0

        while True:
            try:
                pi = request(piStart)
                break
            except:
                #print(f'{index} is {((piStart-inicialValue)/(piEnd-inicialValue))*100}')
                sleep(2)

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
                    list.append(f'index:_{index}__Number:{num}')
                    list.sort()
                    print(f'first number is: {list[0]}')
                    primeNumbers += 1

            start +=  1

        piStart += 800

        if(piStart >= piEnd or primeNumbers > 0):
            break


#mainFunction(0, 1000000, 0)

inicialPi = 0
step = 10000000

tempo0 = time()
print('running')
print(100*'-')

for c in range(0, 1000):
    threading.Thread(target=mainFunction, args = (c*step+inicialPi, c*step+step+(0.001*step)+inicialPi, c)).start()

tempo1 = time()
print(tempo1-tempo0)
