from Bio import Entrez
from Bio import SeqIO
import json
import xmltodict

Entrez.email = "A.N.Other@example.com"

with Entrez.efetch(db='nucleotide', rettype='gb', retmode='text', id='NM_002112.4') as handle:

    for seq_record in SeqIO.parse(handle, 'gb'):

        for feature in seq_record.features:

            if feature.type == 'CDS':

                CDS_dict = {
                    'gene': feature.qualifiers['gene'],
                    'EC_number': feature.qualifiers['EC_number'],
                    'note': feature.qualifiers['note'],
                    'codon_start': feature.qualifiers['codon_start'],
                    'product': feature.qualifiers['product'],
                    'protein_id': feature.qualifiers['protein_id'],
                    'db_xref': feature.qualifiers['db_xref'],
                    'translation': feature.qualifiers['translation']
                }

        record_dict = {
            'ID': seq_record.id,
            'Gene_symbol': CDS_dict['gene'][0],
            'HGNC_ID': CDS_dict['db_xref'][2].split(':')[2],
            'DNA_sequence': str(seq_record.seq),
            'RNA_sequence': str(seq_record.seq.replace("T", "U")),
            'Protein_sequence': CDS_dict['translation'][0],
            'Protein_ID': CDS_dict['protein_id'][0]
        }

    print(json.dumps(record_dict, indent=4))

'''
response = Entrez.efetch(db='nucleotide', rettype='gb', retmode='XML', id='NM_002112.4')
record = xmltodict.parse(response.read())['GBSet']['GBSeq']

record_dict = {}

for key, value in record.items():

    key = key.replace('GBSeq_', '')

    record_dict[key] = value
'''