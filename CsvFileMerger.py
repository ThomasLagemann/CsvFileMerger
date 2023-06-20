import os
import csv
import argparse

default_path = ".\csv"
default_delimiter=";"
default_output="merged.csv"
default_columns = 2
globalHeaderRow = []
rowsWithoutHeader = []
filenameColumn = []
    
def createArgParser():
    parser = argparse.ArgumentParser()
    # Add arguments
    parser.add_argument('-p','--path', type=str, help='The path to the folder conraining CSV files.', dest = 'path', required=True)
    parser.add_argument('-d','--delimiter', type=str, default=default_delimiter, help='The delimiter used in the CSV files.',dest='delimiter')
    parser.add_argument('-o','--output', type=str, default=default_output, help='The path to the merged output CSV file.', dest='output')
    parser.add_argument('-c','--columns', type=int, default=default_columns, help='The number of columns from the inputs CSV files that will be written into export CSV file.', dest='columns')
    return parser
        
if __name__ == "__main__":
    
    parser = createArgParser()
    # Parse arguments
    args = parser.parse_args()
        
    for file in os.listdir(args.path):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 
            full_path = os.path.join(args.path, filename)
            with open(full_path, 'r', encoding='utf-8-sig') as file:
                csvReader = csv.reader(file, delimiter=args.delimiter)
                headerRow = next(csvReader)
                if len(headerRow) > len(globalHeaderRow):
                    globalHeaderRow = headerRow[0:args.columns]
                for row in csvReader:
                    filenameColumn.append(filename)                
                    rowsWithoutHeader.append(row[0:args.columns])
            continue
        else:
            continue

    headerRowLength = len(globalHeaderRow)
    globalHeaderRow.append("Filename")
    with open(args.output, 'w', newline='', encoding='utf-8-sig') as outputFile:
        csvWriter = csv.writer(outputFile,delimiter=args.delimiter)
        csvWriter.writerow(globalHeaderRow)
        for i in range(1,len(rowsWithoutHeader)):
            row = rowsWithoutHeader[i]
            for j in range(len(row), headerRowLength):
                row.append("")
            
            row.append(filenameColumn[i])
            csvWriter.writerow(row)
