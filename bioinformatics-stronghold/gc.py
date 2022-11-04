"""
The GC-content of a DNA string is given by the percentage of symbols in the string
that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that
the reverse complement of any DNA string has the same GC-content.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content
of that string. 
"""


from fasta import readfasta


def gc_content(dna_string):
    gc_count = dna_string.count('G') + dna_string.count('C')
    return gc_count / len(dna_string) * 100


if __name__ == "__main__":
    dna_strings = readfasta("in\gc.txt", get_ids=True)
    gc_list = ((id, gc_content(dna)) for id, dna in dna_strings.items())
    highest_gc = max(gc_list, key=lambda x: x[1])
    with open("out\gc.txt", "w") as output:
        output.write(f"{highest_gc[0]}\n")
        output.write("%.6f" % highest_gc[1])