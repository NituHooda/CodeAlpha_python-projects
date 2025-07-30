import re
import os

input_file = input("Enter the path to the .txt file: ").strip()
output_file = input("Enter the output file name (e.g., emails.txt): ").strip()

if not os.path.exists(input_file):
    print(f"❌ Input file does not exist: {input_file}")
    exit()

with open(input_file, 'r') as file:
    text = file.read()

emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

if not emails:
    print("No email addresses found.")
else:
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')
    print(f"\n✅ {len(emails)} emails extracted and saved to {output_file}.")
