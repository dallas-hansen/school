def remove_evens(ls):
    return [x for x in ls if x % 2 != 0]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = remove_evens(nums)

    print(result)
