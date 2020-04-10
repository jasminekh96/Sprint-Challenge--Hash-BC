#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_resize)


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

    # a loop? use insert and resize when tickets are done?

    for tick in tickets:
        while tick.source is not None:
            hash_table_insert(hashtable, tick.source, tick.destination)
            FirstTick = None
            if tick.source is None:
                hash_table_insert(hashtable, tick.source, tick.destination)
                hash_table_resize()
                FirstTick = tick
            elif tick.source == FirstTick.destination:
                hash_table_insert(hashtable, tick.source, tick.destination)
                hash_table_resize()
                FirstTick = tick

        


    return route
