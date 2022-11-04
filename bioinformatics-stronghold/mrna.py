"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could
have been translated, modulo 1,000,000. (Don't neglect the importance of the stop
codon in protein translation.)
"""


from prot import codon_table
from collections import Counter


number_codon_transl = Counter(codon_table.values())

def count_translations(rna_string, mod=1_000_000):
    possible_rnas = 1
    for codon in rna_string:
        possible_rnas *= number_codon_transl[codon]
        possible_rnas %= mod
    return (possible_rnas * number_codon_transl["Stop"]) % mod


if __name__ == "__main__":
    with open("in\mrna.txt", "r") as dataset:
        rna = dataset.read().replace('\n', '')
    possible_translations = count_translations(rna)
    print(possible_translations)