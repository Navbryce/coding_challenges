from collections import Counter


# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    """
    matches strings with queries and counts
    """
    counter = Counter(queries)

    for string in strings:
        if string in counter:
            counter[string] += 1

    counter.subtract(Counter(queries))

    list = []
    for key in queries:  # maintains order
        list.append(counter[key])
    return list
