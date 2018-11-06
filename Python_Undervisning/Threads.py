import threading

lock = threading.Lock()

a = 0


def counter():
    global a
    for i in range(10):
        print(i)


t1 = threading.Thread(target=counter)   # Såfremt at i dette tilfælde counter skrives som counter()
                                        # så kalder vi counter functionen, og target bliver lig none
                                        # når counter står uden () så henviser target til referencen af counter
                                        # og koden køres
t1.start()

def inc():
    global a
    with lock:
        for i in range(25000):
            a+=i

def dec():
    global a
    for i in range(25000):
        with lock:
            a-=i

t2 = threading.Thread(target=inc)
t3 = threading.Thread(target=dec)

t2.start()
t3.start()

t2.join()
t3.join()

print(a)