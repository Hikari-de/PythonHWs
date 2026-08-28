def permutations(sequence):
    if len(sequence) <= 1:
        return [sequence]

    first = sequence[0]
    rest = sequence[1:]

    rest_per = permutations(rest)
    result = []
    for perm in rest_per:
        for i in range(len(perm) + 1):
            new_per = perm[:i] + first + perm[i:]

            if new_per not in result:
                result.append(new_per)

    return result

sequence = input()
print(permutations(sequence)) 


    