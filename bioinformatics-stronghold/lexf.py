""" LEXF : Enumerating k-mers Lexicographically
Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order
(and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the
standard order of symbols in the English alphabet).
"""


from itertools import product


if __name__ == "__main__":
    with open("in\lexf.txt", "r") as dataset:
        alphabet = dataset.readline().split()
        lenght = int(dataset.readline())

    strings_formed = product(alphabet, repeat=lenght)

    with open("out\lexf.txt", "w") as output:
        for string in strings_formed:
            output.write(f"{''.join(string)}\n")