def to_rna(dna_strand: str) -> str:
    """
    Translates the given DNA sequance to RNA by the rules:
        G -> C
        C -> G
        T -> A
        A -> U
    Args:
        dna_strand(str): The given DNA sequance to translate
    Returns:
        str: The translated RNA sequance

    """
    # Solution 1, for loop:
    # rna_seq = []
    # for letter in dna_strand:
    #     if letter == "G":
    #         rna_seq.append("C")
    #     if letter == "C":
    #         rna_seq.append("G")
    #     if letter == "T":
    #         rna_seq.append("A")
    #     if letter == "A":
    #         rna_seq.append("U")
    # return "".join(rna_seq)

    # Solution 2, list of tuples:
    # translation = {"G": "C", "C": "G", "T": "A", "A": "U"}
    # rna_seq = (translation[key] for key in dna_strand)
    # return "".join(rna_seq)

    # solution 3, maketrans and translate:
    dna, rna = "GCTA", "CGAU"
    translation = str.maketrans(dna, rna)
    return dna_strand.translate(translation)
