"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may
return any single solution.)
"""


from fasta import readfasta


def lcsubs(dna_strings):
    first = dna_strings[0]
    longest_c = ''
    for start in range(len(first)+1):
        for end in range(len(first), 0, -1):
            if (len(first[start:end]) > len(longest_c) and
                all(map(lambda s: first[start:end] in s, dna_strings))):
                longest_c = first[start:end]
    return longest_c


if __name__ == "__main__":
    strings = readfasta("in\lcsm.txt")
    print(lcsubs(strings))