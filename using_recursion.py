def find_perms(word: str):
    indent = " " * len(word)

    print(f'{indent}Permuting {word}')

    # This is the base case

    if len(word) < 2:
        print(f'{indent}Base case!')
        return [word]

    else:
        # List to store our perms in
        perms = []

        # Work through characters in word

        for i in range(len(word)):
            # Strip out characters before and after
            print(f'{indent}Pivoting on {word[i]}')

            before = word[:i]
            after = word[i + 1:]

            # This is the recursive step - we permute the remaining characters
            perm_list = find_perms(before + after)

            # Now combine with our character
            perms += [word[i] + perm for perm in perm_list]
        return perms


if __name__ == '__main__':
    w = input('Word: ')
    print(find_perms(w))
