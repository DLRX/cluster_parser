from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import random
import string
import os

output_folder = r"C:\Users\dodol\Documents\GitHub\cluster_parser\data"
os.makedirs(output_folder, exist_ok=True)

def random_protein_seq(length):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    return ''.join(random.choices(amino_acids, k=length))

for i in range(10):
    records = []
    for j in range(random.randint(1, 100)):  # 3 to 8 sequences per file
        seq = random_protein_seq(random.randint(45, 400))
        record = SeqRecord(Seq(seq), id=f"seq{j+1}", description=f"Fake protein {j+1}")
        records.append(record)
    file_path = os.path.join(output_folder, f"fake_{i+1}.fasta")
    SeqIO.write(records, file_path, "fasta")