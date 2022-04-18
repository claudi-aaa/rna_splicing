from codon_dict import codon_codes

#sort intron lengths - checked
def sort_introns(list):
    sorted_introns = sorted(list, key=len, reverse=True)
    print(f'Sorted Introns = {sorted_introns}')
    return sorted_introns

#remove introns
def remove_introns(intron_data, dna_data):
    for intron in intron_data:
        if intron in dna_data:
            dna_data = dna_data.replace(intron, '')
    return dna_data

#convert Ts to Us
def t_to_u(dna_strand):
    new_strand = [nt.replace('T', 'U') for nt in dna_strand]
    rna_strand = "".join(new_strand)
    return rna_strand

#find start pos
def chop_to_start(rna_str):
    start_pos = rna_str.find('AUG')
    rna_str = rna_str[start_pos:]
    return rna_str

#chop into 3s
def match_codons(rna_str):
    codon_str = [rna_str[i:i + 3] for i in range(0, len(rna_str), 3)]
    return codon_str

def make_protein(codon_str):
    protein_string = []
    for codon in codon_str:
        if codon_codes[codon] != 'Stop':
            protein_string.append(codon_codes[codon])
        else:
            break
    result = ''.join(protein_string)
    print(result)



data = open('rosalind_splc-1.txt', 'r')
lines = data.read().split('>')
lines.pop(0)


dna = []
all_introns = []

for item in lines:
    if lines.index(item) > 0:
        no_ros = item[14:]
        no_n = no_ros.strip('\n')
        all_introns.append(no_n)
    else:
        no_ros = item[14:]
        no_n = no_ros.replace('\n', '')
        dna.append(no_n)

introns = sort_introns(all_introns)

rev_dna = remove_introns(introns, dna[0])

rna_strand = t_to_u(rev_dna)

from_start_rna = chop_to_start(rna_strand)

make_protein(match_codons(from_start_rna))


