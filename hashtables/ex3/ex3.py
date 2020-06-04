def intersection(arrays):
    result = []
    numbers = {}
    array_count = len(arrays)
    for num in arrays[0]:
        numbers[num] = 1
    for arr in arrays[1:]:
        for num in arr:
            if num in numbers:
                numbers[num] += 1
    for number in numbers:
        if numbers[number] == array_count:
            result.append(number)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
