# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []


    for i in queries:
        for j in files:
            if i in j:
                result.append(j)
        else:
            continue
    

    #for i in queries:
    # if paths contains(queries):
    #   path.append(arr)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
