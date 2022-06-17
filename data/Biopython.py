"""from Bio.Seq import Seq
dna = Seq("ATGCATGCGCTATCGCATGCGTCATG")
print(dna)
"""


from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

for sequence in SeqIO.parse("desA-concat-filamentous.fa", "fasta"):
    print(sequence.id)
    xSeq = ProteinAnalysis(sequence.seq)
    print(xSeq.count_amino_acids()['A']) 
    