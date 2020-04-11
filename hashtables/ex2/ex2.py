#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # a loop? use insert and retrieve when tickets are needed?

    for tick in tickets:
        hash_table_insert(hashtable, tick.source, tick.destination)
        # base city which is none
    route[0] = hash_table_retrieve(hashtable, "NONE")
    # Then, when constructing the entire route, the `i`th location in the route can be found by checking the hash table for the `i-1`th location.
    for i in range(1, len(route)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    if route[-1] == "NONE":
        return route [:-1]
    else: 
        return None

