# Module for reading FASTA files


from re import split, findall
import requests


def readfasta(filename, get_ids=False):
    """Reads files in FASTA format.
    
    Every string in a FASTA file begins with a single-line that contains
    the symbol '>' along with some labeling information about the string.

    Returns a generator with all strings in the Fasta file if get_ids=False,
    returns a dictionary with id:string otherwise.
    """
    with open(filename, 'r') as file:
        fasta_file = file.read()
    strings = split('>.*\n', fasta_file)
    if get_ids:
        ids = findall('>.*\n', fasta_file)
        return {id[:-1]:s.replace('\n', '') for id, s, in zip(ids, strings[1:])}
    else:
        return (s.replace('\n', '') for s in strings[1:])


def search_uniprot(uniprot_id, feedback=False):
    """Search UniProt's API with an UniProt Database acess ID.

    Uniprot ID examples:
    A2Z669, B5ZC00, P07204, P20840
    """
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url).content.decode('utf-8')
    if feedback:
        print(f"{uniprot_id} received") 
    return split('\n', response, 1)[1].replace('\n', '')