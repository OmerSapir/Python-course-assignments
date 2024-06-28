import re
import argparse
import random
from Bio import Entrez
from Bio import SeqIO


def longest_seq(dna):
    length = 1
    result = ''
    while True:
        regex = r'([GATC]{' + str(length) + r'}).*\1'
        #print(regex)
        m = re.search(regex, dna)
        if m:
            result = m.group(1)
            length += 1
        else:
            break

    print(result)
    print(len(result))


def get_longest_ORF(dna):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    start_positions = [m.start() for m in re.finditer(start_codon, dna)]
    stop_positions = {codon: [m.start() for m in re.finditer(codon, dna)] for codon in stop_codons}
    
    longest_orf = ""
    
    for start in start_positions:
        for stop_codon in stop_codons:
            for stop in stop_positions[stop_codon]:
                if stop > start and (stop - start) % 3 == 0:
                    orf = dna[start:stop+3]
                    if len(orf) > len(longest_orf):
                        longest_orf = orf
                    break
    
    print(longest_orf)
    print(len(longest_orf))



def analyze_dna(path, longest_duplication, longest_ORF):
    try:
        dna = SeqIO.read(path, "genbank")
    except Exception as e:
        print(f"Error reading GenBank file: {e}")
        return
    str_dna = str(dna.seq)

    if longest_duplication:
        longest_seq(str_dna)

    if longest_ORF:
        get_longest_ORF(str_dna)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="'Max length' DNA sequences analysis")
    parser.add_argument("--input", required=True, help="GeneBank file path")
    parser.add_argument("--duplicated", action="store_true", help="Perform the duplicated sequence analysis.")
    parser.add_argument("--ORF", action="store_true", help="Perform the ORF analysis.")

    args = parser.parse_args()
    
    analyze_dna(args.input, args.duplicate, args.ORF)