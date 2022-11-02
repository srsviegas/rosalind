""" HAMM : Counting Point Mutations
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""


def hamming_distance(s, t):
    assert len(s) == len(t), "Divergent String Lenghts"
    return sum(1 for i in range(len(s)) if s[i] != t[i])


if __name__ == "__main__":
    with open("hamm-in.txt", "r") as dataset:
        hamm_dist = hamming_distance(*dataset.readlines())
    print(hamm_dist)