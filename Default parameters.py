#def net_price(list_price,discount = 0,tax = 0.07):
    #return list_price * (1 - discount) * (1 + tax)

#print(net_price(500))
#print(net_price(500, 0.5))
#print(net_price(500, 0.3, 0))

import time

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(30,15)
