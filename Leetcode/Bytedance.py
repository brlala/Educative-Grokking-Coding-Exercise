def get_count(target):
    res = []
    max_diff = len(str(target)) * 9
    for i in range(target - max_diff, target):
        if (i + sum(int(num) for num in str(i))) == target:
            res.append(i)
    return res


print(get_count(123456833214))
