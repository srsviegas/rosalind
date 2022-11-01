""" DNA | Counting DNA Nucleotides
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols
'A', 'C', 'G', and 'T' occur in s.
"""


def count_molecules(dna_string):
    return map(dna_string.count, "ACGT")


if __name__ == "__main__":
    with open("dna_in.txt", "r") as dataset:
        n_molecules = count_molecules(dataset.readline())
    print(*n_molecules)