## CsvFileMerger

Takes all .csv files in the given path and merges them into a single document with a common header.
The filename of the source document the row is taken from is added in the last column of each row.

## Usage:
CsvFileMerger.py [-h] [-path PATH] [-delimiter DELIMITER] [-output OUTPUT]

optional arguments:

    -h, --help            show this help message and exit
  
    -path PATH            The path to the folder conraining CSV files.
  
    -delimiter DELIMITER  The delimiter used in the CSV files.
  
    -output OUTPUT        The path to the merged output CSV file.
