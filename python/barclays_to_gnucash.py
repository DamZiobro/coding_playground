#!/usr/bin/env python
"""
Get Barclays export CSV file with transaction
and prepare GnuCash-friendly CSV file.
"""

import csv
import re
from datetime import datetime

import fire

DEFAULT_TRANSFER = "Expenses:Other Expenses:Miscellaneous"

def barclays_csv_to_gnucash_csv(input_file_csv):

    output_rows = []
    with open(input_file_csv) as input_csv:
        csv_reader = csv.DictReader(input_csv)
        for row in csv_reader:

            if not row["Date"]:
                print(f"WARNING: skipping row as no data included: {row}")
                continue

            print(f"row: {row}")
            output_row = {}
            output_row["Date"] = (
                datetime.strptime(row["Date"], "%d/%m/%Y").strftime("%y-%m-%d")
            )

            description, transfer = transform(row["Memo"])
            if not transfer or not description:
                description, transfer = ask_for_description(row, transfer, row["Memo"])

            output_row["Description"] = description
            output_row["Transfer Account"] = transfer

            output_row["Withdrawal"] = None
            output_row["Deposit"] = None
            amount = float(row["Amount"])
            if amount < 0:
                output_row["Withdrawal"] = abs(amount)
            else:
                output_row["Deposit"] = abs(amount)

            output_rows.append(output_row)

    return output_rows

def nestbank_csv_to_gnucash_csv(input_file_csv):

    output_rows = []
    with open(input_file_csv) as input_csv:
        csv_reader = csv.DictReader(input_csv)
        for row in csv_reader:

            if not row.get("Data operacji"):
                print(f"WARNING: skipping row as no date field included: {row}")
                continue

            print(f"row: {row}")
            output_row = {}
            output_row["Date"] = (
                datetime.strptime(row["Data operacji"], "%d-%m-%Y").strftime("%y-%m-%d")
            )

            description, transfer = transform(row["Tytuł operacji"])
            if not transfer or not description:
                description, transfer = ask_for_description(row, transfer, row["Tytuł operacji"])

            output_row["Description"] = description
            output_row["Transfer Account"] = transfer

            output_row["Withdrawal"] = None
            output_row["Deposit"] = None
            amount = float(row["Kwota"])
            if amount < 0:
                output_row["Withdrawal"] = abs(amount)
            else:
                output_row["Deposit"] = abs(amount)

            output_rows.append(output_row)

    return output_rows

def pkobp_csv_to_gnucash_csv(input_file_csv):

    output_rows = []
    with open(input_file_csv, encoding="iso-8859-1") as input_csv:
        csv_reader = csv.DictReader(input_csv)
        for row in csv_reader:

            if not row.get("Data operacji"):
                print(f"WARNING: skipping row as no date field included: {row}")
                continue

            print(f"row: {row}")
            output_row = {}
            output_row["Date"] = (
                datetime.strptime(row["Data operacji"], "%Y-%m-%d").strftime("%y-%m-%d")
            )

            description, transfer = transform(row["Opis transakcji"])
            if not transfer or not description:
                description, transfer = ask_for_description(row, transfer, row["Opis transakcji"])

            output_row["Description"] = description
            output_row["Transfer Account"] = transfer

            output_row["Withdrawal"] = None
            output_row["Deposit"] = None
            amount = float(row["Kwota"])
            if amount < 0:
                output_row["Withdrawal"] = abs(amount)
            else:
                output_row["Deposit"] = abs(amount)

            output_rows.append(output_row)

    return output_rows

def bank_csv_to_gnucash_csv(input_file_csv, output_file_csv, bank_name="barclays"):

    output_rows = []
    if bank_name.lower() == "barclays":
        output_rows = barclays_csv_to_gnucash_csv(input_file_csv)
    elif bank_name.lower() == "nestbank":
        output_rows = nestbank_csv_to_gnucash_csv(input_file_csv)
    elif bank_name.lower() == "pkobp":
        output_rows = pkobp_csv_to_gnucash_csv(input_file_csv)
    else:
        raise ValueError("Unknown bank_name provided as 3rd arg")

    with open(output_file_csv, "w") as output_csv:
        fields = ["Date", "Description", "Transfer Account", "Withdrawal", "Deposit"]
        csv_writer = csv.DictWriter(output_csv, fieldnames=fields)
        #csv_writer.writeheader()
        for row in output_rows:
            print(row)
            csv_writer.writerow(row)

def transform(description):
    mappings = {
        # groceries and shopping
        "asda": ("payment for shopping at Asda", "Expenses:Other Expenses:Grocery shopping"),
        "ipko": ("from nestbank current", "Current Money:Polish Accounts:PKO BP Current Account"),
    }

    for pattern, values in mappings.items():
        if re.search(pattern, description.lower()):
            return values

    #return description, "Expenses:Other Expenses:Miscellaneous"
    return description, None


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question + " (Y/n): ") or "Y").lower().strip()
        if reply[:1] == "y":
            return True
        if reply[:1] == "n":
            return False


def ask_for_description(row, transfer, row_desc):
    print(f"  => input => {row}")
    desc = row_desc
    transfer = DEFAULT_TRANSFER
    while not yes_or_no(f"Is transfer acceptable => '[{transfer}]'"):
        transfer = input(f"write transfer value [{transfer}]: ") or DEFAULT_TRANSFER

    while not yes_or_no(f"Is description accepted => '{desc}'"):
        desc = input(f"write description value [{desc}]: ") or desc

    return desc, transfer


if __name__ == "__main__":
    fire.Fire(bank_csv_to_gnucash_csv)
