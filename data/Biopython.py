from Bio.Seq import Seq
dna = Seq("ATGCATGCGCTATCGCATGCGTCATG")
print(dna)

from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
for sequence in SeqIO.parse("desa-trimmed-no-microcollius.fa", "fasta"):
    print(sequence.id)
    #print(sequence.count_amino_acids()['A']) 