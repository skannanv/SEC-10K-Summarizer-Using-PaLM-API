from sec_edgar_downloader import Downloader
import os

def download_10k_filings(ticker, start_year, end_year, output_directory):
    dl = Downloader(company_name="SaiU", email_address="vidhyakshaya.k-26@scds.saiuniversity.edu.in")

    # Loop through the years and download the 10-K filings
    for year in range(start_year, end_year + 1):
        try:
            dl.get("10-K", ticker, year, download_details=True, download_folder=output_directory)
            print(f"Downloaded {ticker} 10-K filing for {year}")
        except Exception as e:
            print(f"Failed to download {ticker} 10-K filing for {year}: {e}")

# Main function to download filings for selected companies
def main():
    companies = {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft Corporation"
        # Add more companies if needed
    }

    start_year = 1995
    end_year = 2023

    output_directory = "/Users/vidhyakshayakannan/Documents/FinTech Assignment/sec-edgar-filings"  # Specify the directory where you want the files to be saved

    for ticker, name in companies.items():
        print(f"Downloading 10-K filings for {name} ({ticker})...")
        download_10k_filings(ticker, start_year, end_year, output_directory)

import os

def merge_text_files(directory, output_file):
    merged_text = ""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".txt"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    merged_text += file_content  # Concatenate file content into a single string

    # Write the merged text to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(merged_text)

input_directory = "/Users/vidhyakshayakannan/Documents/FinTech Assignment/sec-edgar-filings"
output_file = "/Users/vidhyakshayakannan/Documents/FinTech Assignment/output.txt"

merge_text_files(input_directory, output_file)

if __name__ == "__main__":
    main()
