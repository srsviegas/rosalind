""" PERM : Enumerating Gene Orders
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For
example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n ≤ 7.
Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order).
"""


from itertools import permutations


if __name__ == "__main__":
    lenght = int(input())
    perm_list = list(permutations(range(1, lenght+1)))
    with open("perm-out.txt", "w") as output:
        output.write(f'{len(perm_list)}')
        for perm in perm_list:
            output.write('\n')
            for integer in perm:
                output.write(f'{integer} ')