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
        # groceries and shopping
        "asda": ("payment for shopping at Asda", "Expenses:Other Expenses:Grocery shopping"),
        "coop|co-op": ("payment for shopping at CoOp", "Expenses:Other Expenses:Grocery shopping"),
        "aldi": ("payment for shopping at Aldi", "Expenses:Other Expenses:Grocery shopping"),
        "lidl gb": ("payment for shopping at Lidl", "Expenses:Other Expenses:Grocery shopping"),
        "tesco": ("payment for shopping at Tesco", "Expenses:Other Expenses:Grocery shopping"),
        "euro food plus|skarpie|ela european": ("payment at polish shop", "Expenses:Other Expenses:Miscellaneous:PolskiSklep"),
        "windhill stores": ("payment for shopping at Windhill Stores", "Expenses:Other Expenses:Grocery shopping"),
        "b&m.*shipley": ("payment for shopping at B&M Shipley", "Expenses:Other Expenses:Grocery shopping"),
        "morrisons": ("payment for shopping at Morrisons", "Expenses:Other Expenses:Grocery shopping"),
        "waitrose": ("payment for shopping at Morrisons", "Expenses:Other Expenses:Grocery shopping"),

        # bills
        "id mobile": ("phone payment", "Expenses:Bussiness Expenses:Phone"),
        "talktalk": ("Payment to Internet at TalkTalk", "Expenses:Other Expenses:HouseExpenses:Internet"),
        "yw internet": ("Payment for water to Yorkshire Water", "Expenses:Other Expenses:HouseExpenses:Water"),
        "bradford metropoli|bradford met counc": ("Payment for council tax", "Expenses:Other Expenses:HouseExpenses:CouncilTax"),
        "e\.on": ("Payment for energy usage to EON", "Expenses:Other Expenses:HouseExpenses:GasAndElectricity"),
        "jagtar singh": ("Payment for boiler services", "Expenses:Other Expenses:HouseExpenses"),
        "admiral insurance": ("Payment for home insurance", "Expenses:Other Expenses:HouseExpenses"),

        # salary
        "xmementoit ltd.*f.*204112": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),
        "204514.*salary": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),
        "204514.*mileage": ("Mileage payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),

        "uram-ziobro m m": ("From Madzia for bills payment", "Imbalance:MyWifeCurrentAccountImbalance"),
        "enrgy2003570711": ("Council Tax Rebate", "Imbalance:MyWifeCurrentAccountImbalance"),

        "transferwise": ("Tranfer to Polish current using Transferwise", "Current Money:Polish Accounts:NestBank Current Account"),
        "p174519": ("Tranfer to Polish current using Transferwise", "Current Money:Polish Accounts:NestBank Current Account"),

        # flights and transport
        "ryanair": ("Payment for Ryanair tickets", "Expenses:Other Expenses:Travel and Entertainment:Flights"),
        "uber \*trip": ("Payment for Uber trip", "Expenses:Other Expenses:Transport"),
        "northern rail": ("Payment for rail tickets", "Expenses:Other Expenses:Transport"),
        "www.tpexpress.co": ("Payment for rail tickets", "Expenses:Other Expenses:Transport"),
        "tfl travel": ("Payment for rail tickets", "Expenses:Other Expenses:Transport"),

        #games
        "365games": ("Payment for FIFA game at 365games", "Expenses:Other Expenses:Travel and Entertainment:Games"),
        "playstation": ("Payment for PlayStation subscription", "Expenses:Other Expenses:Travel and Entertainment:Games"),

        # travel
        "yorkshire dales ic|castle|national trust|kenwood house": ("Payment for tickets on the trip", "Expenses:Other Expenses:Travel and Entertainment"),
        "burnley.*footbal": ("Payment for football tickets", "Expenses:Other Expenses:Travel and Entertainment"),
        "hotel|airbnb": ("Payment for Ryanair tickets", "Expenses:Other Expenses:Travel and Entertainment:Accomodation"),

        # withdraw cash
        "powerplay|eduletting|dioce|notemachine|soccerleagues|szymon krysiak|goals football": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous"),
        "205322 11jun": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous"),
        "nat west bank": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous"),

        # dividend
        "204514.*dividend": ("Dividends payment for shareholder - Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),
        
        # car expenses
        "vehicle tax": ("Road tax payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Road Tax"),
        "petrol|fuel|sainsburys smkts|shell": ("payment for petrol", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Fuel"),
        "gear up service|ziobrorecoverycar|northcliffe|servicing stop|jct car": ("Payment for car repair", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Services"),
        "ttc driver trainin": ("Payment for TTC speeding course", "Expenses:Other Expenses:InfinitiQ50 expenses"),
        "axa insurance": ("Axa insurance payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Insurance"),
        "2getherinsuran": ("Breakdown Cover", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Breakdown Cover"),
        "car parks": ("Car park payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Car Parks"),
        "parking": ("Car park payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Car Parks"),
        "harrogate borough": ("Car park payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Car Parks"),

        # taxes
        "hmrc gov.uk": ("HMRC - Self-assessment Tax on accounts for year 2021/2022", "Expenses:Other Expenses:Taxes:Self-Assessment Tax"),

        # books
        "wh smith": ("Payment for Books at WH Smith", "Expenses:Other Expenses:Books"),
        "waterstones": ("Payment for Books at Waterstones", "Expenses:Other Expenses:Books"),

        # clothes expenses
        "next retail": ("Payment for clothes at Next Retail", "Expenses:Other Expenses:Clothes"),
        "sportsdirect": ("Payment for clothes at Sports Direct", "Expenses:Other Expenses:Clothes"),
        "avecsportltd": ("Payment for clothes at Avec", "Expenses:Other Expenses:Clothes"),
        "house of fraser": ("Payment for clothes at House Of Fraser", "Expenses:Other Expenses:Clothes"),
        "primark": ("Payment for clothes at Primark", "Expenses:Other Expenses:Clothes"),

        # dining and eating out expenses
        "starbucks": ("Payment for dining at Starbucks", "Expenses:Other Expenses:Dining"),
        "brewers fayre": ("Payment for dining at Brewers Fayre", "Expenses:Other Expenses:Dining"),
        "ubereats|uber\ \*eats|uber\* eats": ("Payment for dining at Uber Eats", "Expenses:Other Expenses:Dining"),
        "latte|costa|bakery": ("Payment for coffee and/or cake", "Expenses:Other Expenses:Dining"),
        "mcdonalds": ("Payment for dining at McDonalds", "Expenses:Other Expenses:Dining"),
        "greggs": ("Payment for dining at Greggs", "Expenses:Other Expenses:Dining"),
        "jessies": ("Payment for dining at Jessies", "Expenses:Other Expenses:Dining"),
        "trowell": ("Payment for dining at Trowell", "Expenses:Other Expenses:Dining"),
        "noble comb": ("Payment for dining at Noble Comb", "Expenses:Other Expenses:Dining"),
        "the idle sa": ("Payment for dining at Idle", "Expenses:Other Expenses:Dining"),
        "livewell vendi": ("Payment for snack at vendor machine", "Expenses:Other Expenses:Dining"),
        "stew\ \&\ oyster": ("Payment for snack at Stew & Oyster", "Expenses:Other Expenses:Dining"),
        "patisserie valerie": ("Payment for snack at patisserie valerie", "Expenses:Other Expenses:Dining"),
        "banjos": ("Payment for snack at Banjos", "Expenses:Other Expenses:Dining"),
        "tong street booze": ("Payment for snack at Tong Street Booze", "Expenses:Other Expenses:Dining"),
        "just eat": ("Payment for dining with Just Eat", "Expenses:Other Expenses:Dining"),
        "deliveroo": ("Payment for dining with Deliveroo", "Expenses:Other Expenses:Dining"),
        "cafe|caffe": ("Payment for coffee at Cafe Bar", "Expenses:Other Expenses:Dining"),
        "huda limited": ("Payment for dining at Huda limited", "Expenses:Other Expenses:Dining"),
        "kfc": ("Payment for dining at KFC", "Expenses:Other Expenses:Dining"),
        "the bridge cafe": ("Payment for dining at The Bridge Cafe", "Expenses:Other Expenses:Dining"),
        "water lane boathou|boathouse inn": ("Payment for dining at Boathouse Saltaire", "Expenses:Other Expenses:Dining"),
        "hitching post": ("Payment for dining at The Hitching Post", "Expenses:Other Expenses:Dining"),
        "grapes": ("Payment for dining at The Grapes", "Expenses:Other Expenses:Dining"),
        "saltaire brew": ("Payment for beer at Saltaire Brewary", "Expenses:Other Expenses:Dining"),
        "pret a manger": ("Payment for coffee at Pret a Manger", "Expenses:Other Expenses:Dining"),
        "websters": ("Payment for dining at Websters", "Expenses:Other Expenses:Dining"),
        "akbar leeds": ("Payment for dining at Akbar Leeds", "Expenses:Other Expenses:Dining"),
        "chip n ern": ("Payment for dining at Chip n ern", "Expenses:Other Expenses:Dining"),
        "kebab ranch": ("Payment for dining at Kebab Ranch", "Expenses:Other Expenses:Dining"),
        "donington park": ("Payment for dining at Donington Park", "Expenses:Other Expenses:Dining"),
        "lbm ph limited": ("Payment for dining at Donington Park", "Expenses:Other Expenses:Dining"),
        "leeds station leon|leon restaurants": ("Payment for dining at Leon", "Expenses:Other Expenses:Dining"),
        "wetherspoons": ("Payment for dining at Wetherspoons", "Expenses:Other Expenses:Dining"),
        "theydon oak": ("Payment for dining at Theydon Oak", "Expenses:Other Expenses:Dining"),
        "toby carvery": ("Payment for dining at Toby Carvery", "Expenses:Other Expenses:Dining"),
        "woolley edge": ("Payment for dining at Moto Woooley", "Expenses:Other Expenses:Dining"),
        "intu uxbridge": ("Payment for dining at Intu", "Expenses:Other Expenses:Dining"),
        "kings (head|arms)": ("Payment for dining at Kings Head", "Expenses:Other Expenses:Dining"),
        "welcome break": ("Payment for dining at Welcome break", "Expenses:Other Expenses:Dining"),
        "(clothiers|lister's) arms": ("Payment for dining at Clothiers Arms", "Expenses:Other Expenses:Dining"),
        "dolci": ("Payment for dining at Dolci", "Expenses:Other Expenses:Dining"),
        "lefteris": ("Payment for dining at Lefteris", "Expenses:Other Expenses:Dining"),
        "coffee": ("Payment for dining at Lefteris", "Expenses:Other Expenses:Dining"),
        "bradford broadway": ("Payment for dining at Lefteris", "Expenses:Other Expenses:Dining"),
        "marina view": ("Payment for dining at Marina View", "Expenses:Other Expenses:Dining"),
        " tea ": ("Payment for dining at tea room", "Expenses:Other Expenses:Dining"),
        "ztl\*ilkley": ("Payment for dining at tea room", "Expenses:Other Expenses:Dining"),
        "bowers tap": ("Payment for dining at Bowers tap", "Expenses:Other Expenses:Dining"),
        "la bottega": ("Payment for dining at La Bottega", "Expenses:Other Expenses:Dining"),
        "the maidenhead": ("Payment for dining at The maidenhead", "Expenses:Other Expenses:Dining"),
        "one stop 0961": ("Payment for dining at One Stop", "Expenses:Other Expenses:Dining"),
        "ye olde bull ring": ("Payment for dining at Ye Olde Bull Ring", "Expenses:Other Expenses:Dining"),
        "quaffery": ("Payment for dining at Quaffery", "Expenses:Other Expenses:Dining"),
        "ydnpa": ("Payment for dining at Ydnpa", "Expenses:Other Expenses:Dining"),
        "super whippy": ("Payment for dining at Super Whippy", "Expenses:Other Expenses:Dining"),
        "spinks nest": ("Payment for dining at Spinks Nest", "Expenses:Other Expenses:Dining"),
        "selecta": ("Payment for dining at Selecta", "Expenses:Other Expenses:Dining"),
        "flying horse": ("Payment for dining at Flying Horse", "Expenses:Other Expenses:Dining"),
        "old thatched inn": ("Payment for dining at Old Thatched Inn", "Expenses:Other Expenses:Dining"),
        "treats": ("Payment for dining at Treats", "Expenses:Other Expenses:Dining"),
        "se greenwich": ("Payment for dining at SE Greenwich", "Expenses:Other Expenses:Dining"),
        "confectione": ("Payment for dining at SE Greenwich", "Expenses:Other Expenses:Dining"),
        "ello group": ("Payment for dining at Ello group", "Expenses:Other Expenses:Dining"),
        "rudds arms": ("Payment for dining at Rudds arms", "Expenses:Other Expenses:Dining"),
        "pizza": ("Payment for pizza", "Expenses:Other Expenses:Dining"),
        "hinxton hall": ("Payment for dining at Hinxton Hall", "Expenses:Other Expenses:Dining"),
        "the red lion": ("Payment for dining at The Red Lion", "Expenses:Other Expenses:Dining"),
        "bella italia": ("Payment for dining at Bella Italia", "Expenses:Other Expenses:Dining"),
        "salt east parade": ("Payment for dining at Salt East Parade", "Expenses:Other Expenses:Dining"),
        "sumup \*jagoda": ("Payment for dining at Polski Klub Jagoda", "Expenses:Other Expenses:Dining"),
        "restau": ("Payment for dining at restaurant", "Expenses:Other Expenses:Dining"),
        "hawthorne farm": ("Payment for dining at Hawthorne Farm", "Expenses:Other Expenses:Dining"),
        "higher ground": ("Payment for dining at Higher Ground Cafe", "Expenses:Other Expenses:Dining"),
        "school service sta": ("Payment for dining at School Service Station", "Expenses:Other Expenses:Dining"),
        "norman rae": ("Payment for dining at Sir Norman Rae", "Expenses:Other Expenses:Dining"),
        "lord rodney": ("Payment for dining at Lord Rodney", "Expenses:Other Expenses:Dining"),
        "iz \*the country ki": ("Payment for dining at The Country", "Expenses:Other Expenses:Dining"),
        "junction inn": ("Payment for dining at Junction Inn", "Expenses:Other Expenses:Dining"),
        "hungry monk": ("Payment for dining at Hungry Monk", "Expenses:Other Expenses:Dining"),
        "oldest sweetsh": ("Payment for dining at Oldest Sweet Shop", "Expenses:Other Expenses:Dining"),
        "old granary": ("Payment for dining at Old Granary", "Expenses:Other Expenses:Dining"),
        "generous pioneer": ("Payment for dining at Generous Pioneer", "Expenses:Other Expenses:Dining"),
        "calder.*hops": ("Payment for dining at Calder & Hops", "Expenses:Other Expenses:Dining"),
        "calverley arms": ("Payment for dining at Calverley Arms", "Expenses:Other Expenses:Dining"),
        "calendar club": ("Payment for dining at Calendar Club", "Expenses:Other Expenses:Dining"),

        # transfer on my bank accounts
        "204112 43041824": ("From Current Account to Savings Account", "Current Money:English Accounts:Barclays Accounts:Barclays Savings Account"),
        "203009 33477010": ("From Car Savings account to Savings Account", "Current Money:English Accounts:Barclays Accounts:House & Car Savings"),
        "204529 53155420": ("From Current account to ISA Account", "Current Money:English Accounts:Barclays Accounts:Barclays ISA"),
        "to monzo": ("to monzo", "Current Money:English Accounts:Monzo Accounts:Monzo Current Account"),

        # internet subscriptions
        "netflix": ("Netflix payment", "Expenses:Other Expenses:TVandInternet"),
        "amazon prime": ("Amazon Prime payment", "Expenses:Other Expenses:TVandInternet"),
        "amazon music": ("Amazon Music payment", "Expenses:Other Expenses:Entertainment"),
        "the athletic": ("internet portal subscription - The Athletic", "Expenses:Other Expenses:Entertainment"),
        "telegraph subscrip": ("internet portal subscription - The Telegraph", "Expenses:Other Expenses:Entertainment"),
        "surfshark": ("internet subscription - Surfshark", "Expenses:Other Expenses:Entertainment"),
        "now.*ents|now.*boost|now 783fb|now.*on 28 dec": ("internet subscription - NOW TV", "Expenses:Other Expenses:Entertainment"),

        # baby expenses
        "smyths": ("Toys at Smyths for Roksanka", "Expenses:Other Expenses:BabyExpenses"),

        "jacek baranowski": ("Return of loan to Jacek", "Income:Gifts Received"),

        "blood and medical|expresstest": ("Payment for Covid Tests", "Expenses:Other Expenses:CovidTests"),

        "land registry": ("Payment for getting house title from HM Land Registry", "Expenses:Other Expenses:Fees"),
        "post office": ("Payment for letter at post office", "Expenses:Other Expenses:Fees"),
        "currys": ("Payment for electronic device at Currys", "Expenses:Other Expenses:Electronics"),

        "aws emea": ("Payment for AWS Services", "Expenses:Other Expenses:Miscellaneous"),
        "amznmktplace|amazon.co.uk": ("Payment at amazon", "Expenses:Other Expenses:Miscellaneous"),
        "ebay": ("Payment for something at Ebay", "Expenses:Other Expenses:Miscellaneous"),
        "registry-trust": ("Payment for something at Registry Trust", "Expenses:Other Expenses:Miscellaneous"),
        "britishredcros": ("Payment to British Red Cross", "Expenses:Other Expenses:Miscellaneous"),
        "ikea": ("Payment at IKEA", "Expenses:Other Expenses:Miscellaneous"),
        "salts mill": ("Payment at Salts Mill", "Expenses:Other Expenses:Miscellaneous"),
        "hayloftplants": ("Payment at hayloftplants", "Expenses:Other Expenses:Miscellaneous"),

        "sopra steria": ("Payment for biometrics appointment", "Expenses:Other Expenses:Citizenship"),
        "2naa031107562": ("Payment for biometrics appointment", "Expenses:Other Expenses:Citizenship"),
        "ncs vue-pte exam": ("Payment for English Exam", "Expenses:Other Expenses:Citizenship"),
        "psi services int": ("Payment for Live in the UK exam", "Expenses:Other Expenses:Citizenship"),

        # ============= BUSINESS ACCOUNT ======================
        "hiscox": ("Hiscox - Payment for Business insurance to Hiscox", "Expenses:Bussiness Expenses:Business Insurance"),
        "zodeq": ("Payment from WellcomeSanger invoice", "Income:UK Income:WellcomeSanger"),
        "commission for": ("Bank account fees", "Expenses:Bussiness Expenses:Fees"),
        "current account.*(sto|bbp)": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "hmrc gov\.uk\.paye": ("HMRC - PAYE - Payment for NIC contributions", "Expenses:Other Expenses:Taxes:NIC contributions"),
        "hmrc (gov\.uk\ )?cotax": ("Corportation Tax Payment for XMementoIT for 2019/2020", "Expenses:Other Expenses:Taxes:Corporation Tax"),
        "hmrc (gov\.uk\ )?vat": ("VAT payment + surcharge", "Expenses:Other Expenses:Taxes:VAT Payment"),
        "companies house": ("Confirmation statement in Companies House", "Expenses:Bussiness Expenses:Fees"),
        "nicola toothill": ("Payment for accountancy ", "Expenses:Bussiness Expenses:Accountancy"),
        "helen kaye": ("Payment for accountancy (Corporation Tax)", "Expenses:Bussiness Expenses:Accountancy"),
        "ppwdl4ux222242jz3c": ("Transfer from XMementoIT's PayPal", "Current Money:English Accounts:Paypal accounts:Paypal XMementoIT GBP"),
        "companieshouse web": ("Confirmation statement payment to Companies House", "Expenses:Bussiness Expenses:Fees"),
        "hmrc shipley": ("Corportation Tax Payment for XMementoIT for 2020/2021", "Expenses:Other Expenses:Taxes:Corporation Tax"),
        "dick hudsons": ("Company Annual Event - Christmas Party", "Expenses:Bussiness Expenses:CompanyAnnualEvents"),

        # salary and dividends
        "uram-ziobro.*dividend": ("Dividends payment for shareholder - Magdalena Uram-Ziobro", "Imbalance:MyWifeCurrentAccountImbalance:MadziaDividends"),
        "uram-ziobro.*salary": ("Salry payment for  Magdalena Uram-Ziobro", "Imbalance:MyWifeCurrentAccountImbalance:MadziaSalary"),
        "204112.*dividend": ("Dividends payment for shareholder - Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "204112.*salary": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "204112.*mileage": ("Mileage payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
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
