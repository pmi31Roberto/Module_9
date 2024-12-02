def all_variants(text):
    for size in range(len(text)):
        for value_2 in range(len(text) - size):
            yield text[value_2:value_2 + size + 1]


a = all_variants("abc")
for i in a:
    print(i)
