def separate_duplicates(arr):

    start, end = 0, 1

    for i in range(len(arr) - 1):

        if arr[start] > arr[end]:

            return len(arr[:start + 1])
        
        if arr[start] == arr[end]:

            duplicated = arr.pop(end)
            arr.append(duplicated)

        else:

            start += 1
            end += 1

    return len(arr[:start + 1])

print(separate_duplicates([1, 1, 2, 2, 3, 3]))
print(separate_duplicates([1, 2, 3, 4]))