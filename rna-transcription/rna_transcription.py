#def to_rna(dna_strand):
#    dna_output = []
#    for nucleotide in dna_strand:
        # error handling here try?
#        try:
#            dna_output += dna(nucleotide)
#        except KeyError:
            # print or return?
#            raise Exception('ValueError')
#    dna_output = "".join(dna_output)
#    return dna_output

def to_rna(dna_strand):
    dna_output = []
    dna_list = list(dna_strand)
    for nucleotide in dna_list:
        if nucleotide == 'G':
            dna_output += 'C'
        elif nucleotide == 'C':
            dna_output += 'G'
        elif nucleotide == 'T':
            dna_output += 'A'
        elif nucleotide == 'A':
            dna_output += 'U'
        else:
            raise ValueError('Input is invalid, please try "G","C","T","A","U"')
    dna_output = "".join(dna_output)
    return dna_output



#Dictionaries need to be used
# key value pair. split / for loop on each input,and map the element to a value pair.

#* `G` -> `C`
#* `C` -> `G`
#* `T` -> `A`
#* `A` -> `U`

#Your function will need to be able to handle invalid inputs by raising a
#`ValueError` with a meaningful message.

def dna(DNA):
    dna_dict = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    return dna_dict[DNA]

