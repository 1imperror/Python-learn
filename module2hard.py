import random


def get_cipher():
    num = list(range(3, 21))
    a = random.choice(num)
    return a


n = get_cipher()
n = int(input('Введите число от 3 до 20: '))

p_num_1 = list(range(1, n))
p_num_2 = list(range(1, n))
result = ''

for i in p_num_1:
    for j in p_num_2:
        b = i
        c = j
        if b >= c:
            continue
        else:
            k = n % (b + c)
            if k == 0:
                result = result + str(b) + str(c)
print(f'{n} - {result}')
