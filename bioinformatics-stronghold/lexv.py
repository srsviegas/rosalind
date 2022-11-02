""" LEXV : Ordering Strings of Varying Length Lexicographically
Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the substring t' = t[1:m].
We have two cases:

If s=t', then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
Otherwise, s≠t'. We define s<Lext if s<Lext' and define s>Lext if s>Lext' (e.g., APPLET<LexARTS
because APPL<LexARTS).
Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer
n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in
“Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols
are given.)
"""


from itertools import product


def form_strings(string, n):
    str_list = ["".join(p) for i in range(1, n+1) for p in product(string, repeat=i)]
    return sorted(str_list, key=lambda s: [string.index(c) for c in s])


if __name__ == "__main__":
    with open("lexv-in.txt", "r") as dataset:
        alphabet = dataset.readline().split()
        lenght = int(dataset.read(1))
        str_list = form_strings(alphabet, lenght)
    with open("lexv-out.txt", "w") as output:
        for string in str_list:
            output.write(f'{string}\n')