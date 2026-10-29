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
    if "T" in sequence and "U" in sequence:
        print("Error: Do not mix T and U in one sequence.")
        return
      # Convert RNA into the equivalent DNA alphabet
    dna_sequence = sequence.replace("U", "T")

    # Divide the sequence into groups of three
    codons = []

    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i + 3]

        if len(codon) == 3:
            codons.append(codon)
        else:
            print("\nIncomplete codon at the end:", codon)
             # Stop if there are no complete codons
    if not codons:
        print("No complete codons available for translation.")
        return

    # Translate each codon
    amino_acids = []

    for codon in codons:
        amino_acids.append(codon_table[codon])
         # Display results
    print("\n========== TRANSLATION RESULTS ==========")

    print("Input sequence:", sequence)
     # Display codons in the original DNA/RNA format
    if "U" in sequence:
        display_codons = [codon.replace("T", "U") for codon in codons]
    else:
        display_codons = codons

    print("\nCodons:", " - ".join(display_codons))

    print("Amino acids:", " - ".join(amino_acids))
     # Identify start codons
    if codons[0] == "ATG":
        print("Start codon:", display_codons[0])
    else:
        print("Start codon: Not present at the beginning")
 # Identify stop codons
    stop_codons = ["TAA", "TAG", "TGA"]

    found_stops = []

    for i in range(len(codons)):
        if codons[i] in stop_codons:
            found_stops.append(display_codons[i])

    if found_stops:
        print("Stop codon(s):", ", ".join(found_stops))
    else:
        print("Stop codon: Not found")
 # Display a codon-by-codon table
    print("\n========== CODON DETAILS ==========")
    print(f"{'Codon':<10}{'Amino Acid':<20}")
    print("-" * 30)

    for i in range(len(codons)):
        print(f"{display_codons[i]:<10}{amino_acids[i]:<20}")
print("WELCOME TO THE CODON TABLE GENERATOR")

display_codon_table()

print("\nEnter a DNA or RNA sequence.")

user_sequence = input("Sequence: ")

translate_sequence(user_sequence)
