#usage: python3 ./attack2doc.py

    #input_file = "./MITRE_ATTACK_techniques.csv"
    #output_file = "./MITRE_ATTACK_techniques.txt"



import csv
import os

def csv_to_document(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for row in reader:
                outfile.write(f"Entry {row['ID']}:\n\n")
                for column, value in row.items():
                    outfile.write(f"{column}: {value}\n")
                outfile.write("\n" + "-"*50 + "\n\n")

def main():


    input_file = input("Enter the path to your CSV file: ")
    output_file = input("Enter the path for the output text file: ")

    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    try:
        csv_to_document(input_file, output_file)
        print(f"Conversion complete. Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()