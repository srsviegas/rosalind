"""
To allow for the presence of its varying forms, a protein motif is represented
by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino
acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given
access ID followed by a list of locations in the protein string where the motif
can be found.
"""


from fasta import search_uniprot
from re import search


def search_motif(motif, string):
    ocurrences = []
    last_ocrr = 0
    while True:
        match = search(motif, string[last_ocrr:])
        if match is not None:
            last_ocrr += match.start() + 1
            ocurrences.append(last_ocrr)
        else:
            break
    return ocurrences
    

if __name__ == "__main__":
    with open("in\mprt.txt", "r") as dataset:
        uniprot_ids = dataset.read()[:-1].split('\n')

    nglycosy_pos = dict.fromkeys(uniprot_ids)
    nglycosy_motif = "N[^P][S|T][^P]"
    for id in nglycosy_pos.keys():
        protein = search_uniprot(id.split('_', 1)[0])
        nglycosy_pos[id] = search_motif(nglycosy_motif, protein)
        
    with open("out\mprt.txt", "w") as output:
        for id in nglycosy_pos.keys():
            if nglycosy_pos[id] != []:
                output.write(f'{id}\n')
                for ocurrence in nglycosy_pos[id]:
                    output.write(f'{ocurrence} ')
                output.write('\n')