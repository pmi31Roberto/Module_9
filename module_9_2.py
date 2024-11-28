first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) >= 5]
print(first_result)

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)

first_and_second_strings = first_strings + second_strings
third_result = {string: len(string) for string in first_and_second_strings if len(string) % 2 == 0}
print(third_result)
