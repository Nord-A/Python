

def gen_numbers():
    for i in range(10000000):
        yield i

a = gen_numbers()

print(next(a),next(a),next(a))