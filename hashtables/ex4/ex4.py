def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    index = {}
    #grab all pos or neg
    #loop through

    for i in a:
        if i < 0:
            counter = abs(i)
            if counter in index:
                result.append(counter)
        else:
            counter = i * -1
            if counter in index:
                result.append(i)
        index[i] = True

    return result
    #     if (i*(-1)) in a:
    #         if i > 0 and i not in result:
    #             result.append(i)
    #         elif (i*(-1)) > 0 and (i*(-1)) not in result: 
    #                 result.append(i*(-1))
    #         else:
    #             continue
    #     else:
    #         continue
    # return result.sort()


        #if i * -1 == a[]
    
    # for i in arr:
    # if i * -1 == arr[i]:
        # put in answer
    # elif:
        #next element


    #return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
