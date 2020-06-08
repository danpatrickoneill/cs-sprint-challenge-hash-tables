import math

def has_negatives(a):
    result = []
    opposites = {}
    for num in a:
        # Zero has no negative; dodge the edge case
        if num != 0:
            opposites[-num] = num
            if num in opposites:
                result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
