import concurrent.futures
from hashlib import md5
from random import choice

def get_coin():
    count = 0
    while True:
        if count == 5:
            break
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            count += 1

with concurrent.futures.ProcessPoolExecutor() as executor: