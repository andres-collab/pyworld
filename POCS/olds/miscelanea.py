
from time import sleep

seconds = 0

try:
    while True:
        print(seconds)
        seconds += 1
        sleep(1)
except KeyboardInterrupt:
    print('Sacabó')
    
    
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!'+  str(len(string)))
    
print ('Campana y se acabó')
