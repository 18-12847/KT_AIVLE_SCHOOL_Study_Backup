def min_of(a):
    minimum = a[0]
    for i in range(1, len(a)):
        if a[i] < minimum:
            minimum = a[i]
    return minimum