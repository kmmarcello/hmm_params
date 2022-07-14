"""from Bio.Seq import Seq
dna = Seq("ATGCATGCGCTATCGCATGCGTCATG")
print(dna)
"""


from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

for gene in SeqIO.parse("desA-concat-filamentous.fa", "fasta"):
    X = ProteinAnalysis("desA-concat-filamentous.fa", "fasta")
    print(gene.id)
    print("Sequence length %i" % len(gene))
    
    