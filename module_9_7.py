def is_prime(func):
    def wrapper(a, b, c):
        count = 0
        summ = func(a, b, c)
        for i in range(1, summ + 1 // 2):
            if summ % i == 0:
                count += 1
        if count == 1:
            return 'Простое'
        else:
            return 'Составное'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# sum_three_dec = is_prime(sum_three)
# print(sum_three_dec(2, 3, 6))
# print(sum_three(2, 3, 6))
result = sum_three(2, 3, 6)
print(result)




