from Bio import SeqIO

record = SeqIO.read("ache.fasta", "fasta")

sequence = record.seq

gc_count = sequence.count("G") + sequence.count("C")
gc_percent = (gc_count / len(sequence)) * 100

print("Sequence ID:", record.id)
print("Sequence Length:", len(sequence))
print("GC Content:", round(gc_percent, 2), "%")