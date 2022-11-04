""" PROT : Translating RNA into Protein
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English
alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from
these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along
with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the
amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""


from textwrap import wrap


codon_table = {
    "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
    "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
    "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
    "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
    "UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
    "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
    "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
    "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
    "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
    "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
    "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
    "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
    "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G", 
    "CAA":"Q", "AAA":"K", "GAA":"E", "UAA":"Stop",
    "CGA":"R", "AGA":"R", "GGA":"G", "UGA":"Stop",
    "CAG":"Q", "AAG":"K", "GAG":"E", "UAG":"Stop"
}


def translate_rna(mrna_strand):
    protein_string = ""
    for codon in wrap(mrna_strand, 3):
        codon = codon_table[codon]
        if codon == "Stop":
            break
        protein_string += codon
    return protein_string


if __name__ == "__main__":
    with open("in\prot.txt", "r") as dataset:
        protein_string = translate_rna(dataset.readline())
    print(protein_string)