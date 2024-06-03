import sys
import os
import csv
from datetime import datetime
from Bio import Entrez


Entrez.email = "omer@sapir.com"

def search_protein_ncbi(term, number):
    handle = Entrez.esearch(db='protein', term=term, idtype="acc", retmax=number)
    record = Entrez.read(handle)
    handle.close()
    return record["Count"], record["IdList"], len(record["IdList"])


def download_protein_ncbi(term, number):
    Count, IdList, len_IdList = search_protein_ncbi(term, number)
    doc_ids = IdList
    
    filenames = []
    os.makedirs('Data', exist_ok=True)  # Ensure the directory exists

    for i, doc_id in enumerate(doc_ids):
        handle = Entrez.efetch(db="protein", id=doc_id, rettype="gb", retmode="text")
        data = handle.read()
        handle.close()
        filename = os.path.join('Data', f"{term}_{doc_id}.gb")
        with open(filename, "w") as file:
            file.write(data)
        filenames.append(filename)

    log_file = 'Search_log.csv'

    file_exists = os.path.isfile('Search_log')
    with open('Search_log', "a", newline="") as csvfile:
        fieldnames = ["date", "term", "max", "total"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "term": term,
            "max": len_IdList,
            "total": Count
        })



def main():
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} TERM NUMBER")
    
    term = sys.argv[1]
    count = int(sys.argv[2])

    download_protein_ncbi(term, count)

if __name__ == "__main__":
    main()