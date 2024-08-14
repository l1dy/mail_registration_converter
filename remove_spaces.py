def remove_spaces(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line = line.lstrip()  # Remove leading spaces
                line = line.replace('; ', ';')  # Remove space after semicolon
                outfile.write(line)

if __name__ == "__main__":
    input_file = 'ausgabe_no_comma.csv'  # Input filename (modified from previous step)
    output_file = 'ausgabe_final.csv'  # Output filename (modified file)
    remove_spaces(input_file, output_file)
