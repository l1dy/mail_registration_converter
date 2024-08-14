import csv
import chardet

def merge_csv_rows(input_file, temp_output_file, max_columns=13):
    # Open input file and detect encoding
    with open(input_file, 'rb') as infile:
        raw_data = infile.read()
        encoding = chardet.detect(raw_data)['encoding']
    
    # Read data from input file
    with open(input_file, 'r', encoding=encoding) as infile:
        reader = csv.reader(infile)
        data = list(reader)
    
    # Write merged data to temporary output file
    with open(temp_output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for i in range(0, len(data), max_columns):
            merged_row = []
            for j in range(max_columns):
                if i + j < len(data):
                    merged_row.extend(data[i + j])
            writer.writerow(merged_row)

def remove_comma_after_semicolon(input_file, temp_output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(temp_output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line = line.replace(';', '; ')  # Add a space after semicolon
                line = line.replace('; ,', ';')  # Remove comma after semicolon
                outfile.write(line)

def remove_spaces(input_file, final_output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(final_output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line = line.lstrip()  # Remove leading spaces
                line = line.replace('; ', ';')  # Remove space after semicolon
                outfile.write(line)

def main(input_file, final_output_file, max_columns=13):
    temp_output_file_1 = 'temp_output_1.csv'
    temp_output_file_2 = 'temp_output_2.csv'

    # Step 1: Merge rows from the CSV file
    merge_csv_rows(input_file, temp_output_file_1, max_columns)

    # Step 2: Remove commas after semicolons
    remove_comma_after_semicolon(temp_output_file_1, temp_output_file_2)

    # Step 3: Remove leading spaces and spaces after semicolons
    remove_spaces(temp_output_file_2, final_output_file)

    # Cleanup temporary files (optional)
    import os
    os.remove(temp_output_file_1)
    os.remove(temp_output_file_2)

if __name__ == "__main__":
    input_file = 'input.csv'  # Input file name
    final_output_file = 'output.csv'  # Final output file name
    main(input_file, final_output_file)
