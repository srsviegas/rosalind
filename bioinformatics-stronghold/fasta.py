# Module for reading FASTA files


from re import split


def readfasta(filename):
    """Reads files in FASTA format.
    
    Every string in a FASTA file begins with a single-line that contains
    the symbol '>' along with some labeling information about the string.
    """
    with open(filename, 'r') as file:
        strings = split('>.*\n', file.read())
    return [s.replace('\n', '') for s in strings[1:]]