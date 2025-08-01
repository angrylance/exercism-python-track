CODONS_TRANSLATION = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}

STOP_CODONS = ("UAA", "UAG", "UGA")


def proteins(strand: str) -> list[str]:
    """
    Decodes a given strand sequence to proteins sequence.
    Args:
        strand (str): a given strand to decode.
    Returns:
        list[str]: sequence of proteins
    """
    proteins_seq = []
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        if codon in STOP_CODONS:
            break
        proteins_seq.append(CODONS_TRANSLATION[codon])
    return proteins_seq
