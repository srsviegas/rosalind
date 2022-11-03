""" RNA | Transcribing DNA into RNA
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed
by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""


def transcribe(dna_string):
    return dna_string.replace('T', 'U')


if __name__ == "__main__":
    with open("in\\rna.txt", "r") as dataset:
        rna = transcribe(dataset.readline())
    print(rna)