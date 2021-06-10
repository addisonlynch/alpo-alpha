import argparse
import pandas as pd
import time

from alpo_alpha.helpers import process_results, validate_results, validate_results_fmt


parser = argparse.ArgumentParser(description="Process excel sheets")
parser.add_argument("WorkbookFilename", type=str, help="Filename of the Excel workbook")
parser.add_argument("ResultsFilename", type=str, help="Filename of results plaintext")
args = parser.parse_args()

# Read the google forms excel spreadsheet
df = pd.read_excel(args.WorkbookFilename)

# Read the results excel spreadsheet
results = pd.read_excel(args.ResultsFilename)

validate_results_fmt(results)

# Validate that the entries match the results
all_entries = (
    df["3 UNIT PLAY"].tolist() + df["2 UNIT PLAY"].tolist() + df["1 UNIT PLAY"].tolist()
)
validate_results(all_entries, results)


# Add score columns
df["3_unit_score"] = df["3 UNIT PLAY"].apply(lambda x: process_results(x, 3.0, results))
df["2_unit_score"] = df["2 UNIT PLAY"].apply(lambda x: process_results(x, 2.0, results))
df["1_unit_score"] = df["1 UNIT PLAY"].apply(lambda x: process_results(x, 1.0, results))

# Tally up score
df["Total Score"] = df["3_unit_score"] + df["2_unit_score"] + df["1_unit_score"]

# Sort by name ascending
df = df.sort_values(by=["FULL NAME"])

# Save the file with a timestamp
filename = "results_" + time.strftime("%Y%m%d-%H%M%S") + ".xlsx"

df.to_excel(filename)
