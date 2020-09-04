def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    positives = {}
    negatives = {}
    result = []

    for i in a:
        if i > 0:
            positives[i] = i
        else:
            negatives[i] = i

    for i in negatives:
        if abs(i) in positives:
            result.append(abs(i))


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
