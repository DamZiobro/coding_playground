#! /usr/bin/env python
"""
Get Barclays export CSV file with transaction
and prepare GnuCash-friendly CSV file.
"""

import csv
import re
from datetime import datetime

import fire

DEFAULT_TRANSFER = "Expenses:Other Expenses:Miscellaneous"

def barclays_to_gnucash(input_file_csv, output_file_csv):

    output_rows = []
    with open(input_file_csv) as input_csv:
        csv_reader = csv.DictReader(input_csv)
        for row in csv_reader:
            output_row = {}
            output_row["Date"] = (
                datetime.strptime(row["Date"], "%d/%m/%Y").strftime("%y-%m-%d")
            )

            description, transfer = transform(row["Memo"])
            if not transfer or not description:
                description, transfer = ask_for_description(row, transfer)

            output_row["Description"] = description
            output_row["Transfer"] = transfer

            output_row["Withdrawal"] = None
            output_row["Deposit"] = None
            amount = float(row["Amount"])
            if amount < 0:
                output_row["Withdrawal"] = abs(amount)
            else:
                output_row["Deposit"] = abs(amount)

            output_rows.append(output_row)

    with open(output_file_csv, "w") as output_csv:
        fields = ["Date", "Description", "Transfer", "Withdrawal", "Deposit"]
        csv_writer = csv.DictWriter(output_csv, fieldnames=fields)
        #csv_writer.writeheader()
        for row in output_rows:
            print(row)
            csv_writer.writerow(row)


def transform(description):
    mappings = {
        "netflix": ("Netflix payment", "Expenses:Other Expenses:TVandInternet"),
        "asda": ("payment for shopping at Asda", "Expenses:Other Expenses:Grocery shopping"),
        "coop|co-op": ("payment for shopping at coop", "Expenses:Other Expenses:Grocery shopping"),
        "aldi": ("payment for shopping at aldi", "Expenses:Other Expenses:Grocery shopping"),
        "id mobile": ("phone payment", "Expenses:Bussiness Expenses:Phone"),
        "talktalk": ("Payment to Internet at TalkTalk", "Expenses:Other Expenses:HouseExpenses:Internet"),
        "uram-ziobro m m": ("From Madzia for bills payment", "Imbalance:MyWifeCurrentAccountImbalance"),
        "euro food plus|skarpie": ("payment at polish shop", "Expenses:Other Expenses:Miscellaneous:PolskiSklep"),
        "xmementoit ltd.*f.*204112": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),
        "yw internet": ("Payment for water to Yorkshire Water", "Expenses:Other Expenses:HouseExpenses:Water"),
        "bradford metropoli": ("Payment for council tax", "Expenses:Other Expenses:HouseExpenses:CouncilTax"),
        "e\.on": ("Payment for energy usage to EON", "Expenses:Other Expenses:HouseExpenses:GasAndElectricity"),
        "ryanair": ("Payment for Ryanair tickets", "Expenses:Other Expenses:Travel and Entertainment:Flights"),
        "vehicle tax": ("Road tax payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Road Tax"),
        "transferwise": ("Tranfer to Polish current using Transferwise", "Current Money:Polish Accounts:NestBank Current Account"),

        "powerplay|eduletting": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous"),

        "204514.*dividend": ("Dividends payment for shareholder - Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),

        "to monzo": ("to monzo", "Current Money:English Accounts:Monzo Accounts:Monzo Current Account"),
        "petrol|fuel|sainsburys smkts": ("payment for petrol", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Fuel"),

        "starbucks": ("Payment for dining at Starbucks", "Expenses:Other Expenses:Dining"),
        "brewers fayre": ("Payment for dining at Brewers Fayre", "Expenses:Other Expenses:Dining"),
        "ubereats": ("Payment for dining at McDonalds", "Expenses:Other Expenses:Dining"),
        "latte|costa|bakery": ("Payment for coffee and/or cake", "Expenses:Other Expenses:Dining"),
        "mcdonalds": ("Payment for dining at McDonalds", "Expenses:Other Expenses:Dining"),
        "greggs": ("Payment for dining at Greggs", "Expenses:Other Expenses:Dining"),
        "jessies": ("Payment for dining at Jessies", "Expenses:Other Expenses:Dining"),
        "trowell": ("Payment for dining at Trowell", "Expenses:Other Expenses:Dining"),

        # ============= BUSINESS ACCOUNT ======================
        "hiscox": ("Hiscox - Payment for Business insurance to Hiscox", "Expenses:Bussiness Expenses:Business Insurance"),
        "zodeq": ("Payment from WellcomeSanger invoice", "Income:UK Income:WellcomeSanger"),
        "commission for": ("Bank account fees", "Expenses:Bussiness Expenses:Fees"),
        "current account.*(sto|bbp)": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "hmrc gov\.uk\.paye": ("HMRC - PAYE - Payment for NIC contributions", "Expenses:Other Expenses:Taxes:NIC contributions"),
        "hmrc gov\.uk\ cotax": ("Corportation Tax Payment for XMementoIT for 2019/2020", "Expenses:Other Expenses:Taxes:Corporation Tax"),
        "hmrc gov\.uk\ vat": ("VAT payment + surcharge", "Expenses:Other Expenses:Taxes:VAT Payment"),
        "companies house": ("Confirmation statement in Companies House", "Expenses:Bussiness Expenses:Fees"),
        "nicola toothill": ("Payment for accountancy ", "Expenses:Bussiness Expenses:Accountancy"),
        "uram-ziobro.*dividend": ("Dividends payment for shareholder - Magdalena Uram-Ziobro", "Imbalance:MyWifeCurrentAccountImbalance:MadziaDividends"),
        "204112.*dividend": ("Dividends payment for shareholder - Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
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


def ask_for_description(row, transfer):
    print(f"  => input => {row}")
    desc = row['Memo']
    transfer = DEFAULT_TRANSFER
    while not yes_or_no(f"Is transfer acceptable => '[{transfer}]'"):
        transfer = input(f"write transfer value [{transfer}]: ") or DEFAULT_TRANSFER

    while not yes_or_no(f"Is description accepted => '{desc}'"):
        desc = input(f"write description value [{desc}]: ") or desc

    return desc, transfer


if __name__ == "__main__":
    fire.Fire(barclays_to_gnucash)
