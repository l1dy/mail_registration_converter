def remove_comma_after_semicolon(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line = line.replace(';', '; ')  # Add a space after semicolon
                line = line.replace('; ,', ';')  # Remove comma after semicolon
                outfile.write(line)

if __name__ == "__main__":
    input_file = 'ausgabe.csv'  # Input filename (ausgabe.csv)
    output_file = 'ausgabe_no_comma.csv'  # Output filename (modified file)
    remove_comma_after_semicolon(input_file, output_file)
