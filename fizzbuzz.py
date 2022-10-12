while True:
    length = input('Enter length: ')
    try:
        length = int(length)
        break
    except:
        print('Invalid length!')
while True:
    fizz = input('Enter fizz number: ')
    try:
        fizz = int(fizz)
        if fizz > 0:
            break
        else:
            print('Invalid fizz number!')
            continue
    except:
        print('Invalid fizz number!')
while True:
    buzz = input('Enter buzz number: ')
    try:
        buzz = int(buzz)
        if buzz > 0 and buzz != fizz:
            break
        else:
            print('Invalid buzz number!')
            continue
    except:
        print('Invalid buzz number!')

for i in range(length):
    n = i+1
    if n%fizz==0 and n%buzz==0:
        print('FIZZBUZZ')
    elif n%fizz==0:
        print('FIZZ')
    elif n%buzz==0:
        print('BUZZ')
    else:
        print(n)