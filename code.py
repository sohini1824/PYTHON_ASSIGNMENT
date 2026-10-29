codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",

    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "AGT": "Serine", "AGC": "Serine",

    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",

    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",

    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",

    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",

    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",
    "AGA": "Arginine", "AGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",

    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",

    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",

    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",

    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",

    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine",
}

def display_codon_table():
    print("\n========== STANDARD CODON TABLE ==========")

    for codon in sorted(codon_table):
        print(codon, ":", codon_table[codon])

    print("Total codons:", len(codon_table))

def display_codon_table():
    print("\n========== STANDARD CODON TABLE ==========")

    for codon in sorted(codon_table):
        print(codon, ":", codon_table[codon])

    print("Total codons:", len(codon_table))

def translate_sequence(sequence):
    sequence = "".join(sequence.split()).upper()

    if not sequence:
        print("Error: The sequence cannot be empty.")
        return

def translate_sequence(sequence):
    sequence = "".join(sequence.split()).upper()

    if not sequence:
        print("Error: The sequence cannot be empty.")
        return

    if any(base not in "ATGC" for base in sequence):
        print("Error: Use only A, T, G, or C.")
        return

