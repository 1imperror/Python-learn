def is_prime(func):
    def wrapper(*args, **kwargs):
        result_1 = func(*args, **kwargs)
        for i in range(2, int(result_1 ** 0.5) + 1):
            if result_1 % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return result_1
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_


result = sum_three(2, 3, 6)
print(result)
