The ncbi.py tool searches for protein records in the NCBI database, downloads them, and logs the search details, using several functions:

1. search_protein_ncbi():
The script searches the NCBI protein database for a given term and number and retrieves a specified number of results.

2.download_protein_ncbi():
The script downloads the data for each result and saves it to a file in the 'Data' directory.
Additionally, the script logs the search details (date, term, total results, and number of IDs retrieved)
to a Search_log.csv file in the current directory.
