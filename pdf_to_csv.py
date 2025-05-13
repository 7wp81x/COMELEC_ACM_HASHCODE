import pdfplumber
import pandas as pd
import re
import sys

def extract_from_pdf(pdf_path):
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if not row or len(row) < 2:
                        continue
                    md5_candidate = row[0].strip()
                    filename_candidate = row[1].strip()
                    if re.fullmatch(r'[a-fA-F0-9]{32}', md5_candidate):
                        data.append([md5_candidate, filename_candidate])

            if not tables:
                lines = page.extract_text().splitlines()
                for line in lines:
                    line = line.strip()
                    match = re.match(r'^([a-fA-F0-9]{32})\s+(.+)$', line)
                    if match:
                        md5 = match.group(1)
                        filename = match.group(2)
                        data.append([md5, filename])

    return data

def pdf_to_csv(pdf_path, output_csv):
    print(f"Extracting md5 hashes form {pdf_path}")
    data = extract_from_pdf(pdf_path)
    if not data:
        print("No valid MD5 - filename pairs found.")
    else:
        df = pd.DataFrame(data, columns=["md5hash", "filename"])
        df.to_csv(output_csv, index=False)
        print(f"Saved to: {output_csv}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_csv.py input.pdf output.csv")
        sys.exit(1)

    pdf_to_csv(sys.argv[1], sys.argv[2])
