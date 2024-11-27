def apply_all_func(int_list, *functions):
    results = dict(map(lambda fun: (fun.__name__, fun(int_list)), functions))
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))



