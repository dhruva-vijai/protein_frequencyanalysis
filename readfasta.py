from Bio import SeqIO

def read_amino(fasta_file):
    seq_dict = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        try:
            seq_dict[record.id] = str(record.seq)
        except ValueError:
            pass
    return seq_dict

