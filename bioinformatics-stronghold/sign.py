""" SIGN : Enumerating Oriented Gene Orderings
A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in
which each integer is then provided with either a positive or negative sign (for the
sake of simplicity, we omit the positive sign). For example, π=(5,-3,-2,1,4) is a signed
permutation of length 5.

Given: A positive integer n ≤ 6.
Return: The total number of signed permutations of length n, followed by a list of all
such permutations (you may list the signed permutations in any order).
"""


from itertools import permutations, chain


def signed_permutations(n):
    perm_list = permutations(chain(range(-n, 0), range(1, n+1)), n)
    return [p for p in perm_list if len(set(map(abs, p))) == n]


if __name__ == "__main__":
    lenght = int(input())
    perm_list = signed_permutations(lenght)
    with open("out\sign.txt", "w") as output:
        output.write(f"{len(perm_list)}")
        for perm in perm_list:
            output.write('\n')
            for number in perm:
                output.write(f'{number} ')