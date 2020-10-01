from gen_pr import pr_num
from random import *


def sl():
    s = randint(0, 100000000000000000000000)
    return s


# public
g = sl()
p = sl()
while True:
    if g == p:
        p = sl()
    else:
        break
# private
a = pr_num()  # Alice
b = pr_num()  # Bob
while True:
    if a == b:
        b = pr_num()
    else:
        break

A = pow(int(g), int(a), p)  # to Bob
B = pow(int(g), int(b), p)  # to Alice

key_alice = pow(int(B), int(a), p)
key_bob = pow(int(A), int(b), p)

print('Число g = ' + str(g) + '\n' +
      'Число p = ' + str(p))
print()
print('Число a Алисы = ' + str(a) + '\n' +
      'Число b Боба = ' + str(b))
print()
print('A = ' + str(A) + '\n' +
      'B = ' + str(B))
print()
print('Ключ у Алисы: ' + str(key_alice) + '\n' +
      'Ключ у Боба: ' + str(key_bob))
