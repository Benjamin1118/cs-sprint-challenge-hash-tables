def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    intersect = []

    for i in arrays:
        if i not in intersect:
            intersect[i] = 1
        else:
            return
    return intersect


    #something like if not in cache put it in there
    #else return and try next
    # once it has done it with all of them run the first again



    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
