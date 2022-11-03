""" REVC : Complementing a Strand of DNA
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""


def reverse_complement(dna_string):
    complement = {
        'A': 'T', 'T': 'A',
        'C': 'G', 'G': 'C'
    }
    revc_string = ""
    for symbol in reversed(dna_string):
        revc_string += complement[symbol]
    return revc_string


if __name__ == "__main__":
    with open("in\\revc.txt", "r") as dataset:
        revc = reverse_complement(dataset.readline())
    print(revc)