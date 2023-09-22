def perms(word: str):
    n = len(word)

    perm_list = []

    counter = [None for i in range(n)]

    level = 0

    while level >= 0:
        # This is equivalent to iterating through the characters in the function

        if counter[level] is None:
            # Initialise counter if this is the first visit
            counter[level] = 1
        else:
            # Otherwise increment counter

            counter[level] += 1

        # This needs not to be a character that has already been selected
        # So find one that hasn't been selected

        while counter[level] in counter[:level]:
            counter[level] += 1

        # Check to see whether we have exhausted characters at this level
        # If so, we move down a level (and set current level to None)

        if counter[level] > n:
            counter[level] = None
            level -= 1

        # If we've reached the bottom of the list then save our work
        # This is equivalent to the base-case

        elif level == n - 1:
            perm = ''.join([word[i - 1] for i in counter])
            perm_list.append(perm)
            print(counter)
            input(f'We have the perm {perm}. Press <enter> to continue.')

        # Otherwise we just move to the next level (equivalent to the recursive step)
        else:
            print(counter)
            level += 1

    return perm_list


if __name__ == '__main__':
    w = input('Word: ')
    print(perms(w))
