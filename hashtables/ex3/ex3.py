def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    array_count = len(arrays)
    counter = {}
    array_counter = {}
    for array in arrays:
        for i in range(len(array)):
            if array[i] not in array_counter:
                if array[i] in counter:
                    counter[array[i]] +=1
    
                else: # if i is in intersect
                  counter[array[i]] = 1
        array_counter = {}
    result = [key for (key, value) in counter.items() if value == array_count]
    print (result)
    return result

              
    
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
