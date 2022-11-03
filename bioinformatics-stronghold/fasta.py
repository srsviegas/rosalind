# Module for reading FASTA files

def readfasta(filename):
    """Reads files in FASTA format.
    
    Every string in a FASTA file begins with a single-line that contains
    the symbol '>' along with some labeling information about the string.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    string_list = []
    aux_str = ""
    for line in lines[1:]:
        line = line.replace('\n', '')
        if line[0] == '>':
            string_list.append(aux_str)
            aux_str = ""
        else:
            aux_str = "".join([aux_str, line])
    string_list.append(aux_str)
    if len(string_list) == 1:
        return string_list[0]
    else:
        return string_list