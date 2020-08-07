#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # trip = []
    route = []
    route.head = source
    # route.head = source
    # while destimation is not None:
    while destination is not None:
        route.next = source.destination
    #   route.next = source.destination()
    # return route

    return route
