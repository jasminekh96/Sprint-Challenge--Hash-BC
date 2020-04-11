#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for weight in range(length):
        weight1 = hash_table_retrieve(ht, limit - weights[weight])
        if weight1 is not None:
            print(weight, weight1)
            return(weight, weight1)
        else:
            hash_table_insert(ht, weights[weight], weight)


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
