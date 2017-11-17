def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        list_strand_a = list(strand_a)
        list_strand_b = list(strand_b)
        hamming_counter = 0
        for nucleotide in range(0,len(list_strand_a)):
            if list_strand_a[nucleotide] == list_strand_b[nucleotide]:
                pass
            else:
                hamming_counter +=1
        return hamming_counter

    # handle 2 strings being passed in
    # strings will be same length
    # loop throuh each char of string, and compare to other char from other string.
    # For each diff, ++ to counter
    # return counter (int)
    # if different length raise Value Error
    # first strand is longer = Value Error
    # second strand is longer = Value Error
    else:
        raise ValueError('Two strands need to be of the same length')

