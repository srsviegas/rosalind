"""
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC
is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4
and 12. You may return these pairs in any order.
"""


from revc import reverse_complement


def is_revpalindrome(dna_string):
    return dna_string == reverse_complement(dna_string)


def count_revpalindromes(dna_string, minl=4, maxl=12):
    revpal_list = []
    for start in range(len(dna_string)):
        for end in range(minl, maxl+1):
            if start + end > len(dna_string):
                break
            elif is_revpalindrome(dna_string[start:start+end]):
                print(dna_string[start:start+end])
                revpal_list.append((start+1, end))
    return revpal_list


if __name__ == "__main__":
    with open("in\\revp.txt", "r") as dataset:
        string = "".join(dataset.readlines()[1:]).replace('\n', '')
        revpals = count_revpalindromes(string)
    with open("out\\revp.txt", "w") as output:
        for item in revpals:
            output.write(f'{item[0]}\t{item[1]}\n')