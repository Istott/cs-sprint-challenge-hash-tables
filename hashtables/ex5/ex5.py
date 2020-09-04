# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # first attempt. passed first test. not second.

    # result = []
    # table = {}

    # for i in files:
    #     filename = i.split("/")[-1]
    #     if filename not in table:
    #         table[filename] = i
    #     # table[filename].append(i)
    
    # for i in queries:
    #     if i in table:
    #         result.append(table[i])

##############

    result = []
    table = {}
    
    for i in range(len(queries)):
        table[queries[i]] = True
    
    for i in files:
        filename = i.split("/")[-1]
        if filename in table:
            result.append(i)

    return result


# if __name__ == "__main__":
#     files = [
#         '/bin/foo',
#         '/bin/bar',
#         '/usr/bin/baz'
#     ]
#     queries = [
#         "foo",
#         "qux",
#         "baz"
#     ]
#     print(finder(files, queries))


if __name__ == "__main__":
    files = ['/dir256/dirb256/file256',
            '/dir256/file256', '/dir3490/dirb3490/file3490',
            '/dir3490/file3490', '/dir8192/dirb8192/file8192',
            '/dir8192/file8192']

    queries = [
            "file3490",
            "file256",
            "file999999",
            "file8192"
        ]
    print(finder(files, queries))