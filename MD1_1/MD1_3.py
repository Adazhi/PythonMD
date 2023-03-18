def ihours() :
    while True :
        try:
            h = input('Enter Hours: ')
            h = int(h)
            return h
        except:
            print('Error, please enter numeric input!')

def irate() :
    while True :
        try:
            r = input('Enter Rate: ')
            r = int(r)
            return r
        except:
            print('Error, please enter numeric input!')

hours = ihours()
rate = irate()
print('------------')
print('Hours:', hours)
print('Rate:', rate)