def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    weight_dict = {}

    for i in range(len(weights)):
        if limit - weights[i] in weight_dict:
            return (i, weight_dict[limit - weights[i]])
        weight_dict[weights[i]] = i

    return None


weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))
