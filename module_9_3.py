first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zip_fir_sec = zip(first, second)
first_result = (len(x) - len(y) for x, y in zip_fir_sec if len(x) != len(y))
print(list(first_result))


second_result = (len(first[i]) == len(second[i]) for i in range(0, max(len(first), len(second))))
print(list(second_result))




