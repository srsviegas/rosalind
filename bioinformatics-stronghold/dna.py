""" DNA | Counting DNA Nucleotides
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols
'A', 'C', 'G', and 'T' occur in s.
"""


def count_symbols(dna_string):
    return map(dna_string.count, "ACGT")


if __name__ == "__main__":
    with open("in\dna.txt", "r") as dataset:
        symbols = count_symbols(dataset.readline())
    print(*symbols)