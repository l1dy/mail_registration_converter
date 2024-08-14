import csv
import chardet

def main(input_file, output_file):
    # Eingabedatei öffnen und Kodierung erkennen
    with open(input_file, 'rb') as infile:
        raw_data = infile.read()
        encoding = chardet.detect(raw_data)['encoding']
    
    # Eingabedatei erneut öffnen und Daten lesen
    with open(input_file, 'r', encoding=encoding) as infile:
        reader = csv.reader(infile)
        data = list(reader)
    
    # Maximale Anzahl von Spalten festlegen
    max_columns = 13
    
    # Ausgabedatei öffnen und Daten schreiben
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for i in range(0, len(data), max_columns):
            # Zusammenfassen von 13 Zeilen der Eingabedatei zu einer Zeile in der Ausgabedatei
            merged_row = []
            for j in range(max_columns):
                if i + j < len(data):
                    merged_row.extend(data[i + j])
            writer.writerow(merged_row)

if __name__ == "__main__":
    input_file = 'eingabe.csv'  # Dateiname der Eingabedatei
    output_file = 'ausgabe.csv'  # Dateiname der Ausgabedatei
    main(input_file, output_file)
