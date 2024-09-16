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
        "coop|co-op": ("payment for shopping at CoOp", "Expenses:Other Expenses:Grocery shopping"),
        "aldi": ("payment for shopping at Aldi", "Expenses:Other Expenses:Grocery shopping"),
        "lidl gb": ("payment for shopping at Lidl", "Expenses:Other Expenses:Grocery shopping"),
        "tesco": ("payment for shopping at Tesco", "Expenses:Other Expenses:Grocery shopping"),
        "euro food plus|skarpie|ela european|on 13 dec clp|dobre bo polskie|maja polish shop": ("payment at polish shop", "Expenses:Other Expenses:Miscellaneous:PolskiSklep"),
        "windhill stores": ("payment for shopping at Windhill Stores", "Expenses:Other Expenses:Grocery shopping"),
        "b&m.*shipley": ("payment for shopping at B&M Shipley", "Expenses:Other Expenses:Grocery shopping"),
        "morrisons": ("payment for shopping at Morrisons", "Expenses:Other Expenses:Grocery shopping"),
        "waitrose": ("payment for shopping at Morrisons", "Expenses:Other Expenses:Grocery shopping"),
        "shipley convenienc": ("payment for shopping at Shipley CostCutter", "Expenses:Other Expenses:Grocery shopping"),

        # bills
        "id mobile": ("phone payment", "Expenses:Bussiness Expenses:Phone"),
        "talktalk": ("Payment to Internet at TalkTalk", "Expenses:Other Expenses:HouseExpenses:Internet"),
        "virgin media": ("Payment to Internet at VirginMedia", "Expenses:Other Expenses:HouseExpenses:Internet"),
        "yw internet|yorkshire water": ("Payment for water to Yorkshire Water", "Expenses:Other Expenses:HouseExpenses:Water"),
        "bradford metropoli|bradford met counc|bradford council": ("Payment for council tax", "Expenses:Other Expenses:HouseExpenses:CouncilTax"),
        "e\.on": ("Payment for energy usage to EON", "Expenses:Other Expenses:HouseExpenses:GasAndElectricity"),
        "jagtar singh": ("Payment for boiler services", "Expenses:Other Expenses:HouseExpenses"),
        "admiral insurance": ("Payment for home insurance", "Expenses:Other Expenses:HouseExpenses"),
        "acw garden centre": ("Payment for garden things at ACW Garden Center", "Expenses:Other Expenses:HouseExpenses"),

        # salary
        "xmementoit ltd.*f.*204112": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),
        "204514.*salary": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),
        "204514.*mileage": ("Mileage payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),

        "transferwise": ("Tranfer to Polish current using Transferwise", "Current Money:Polish Accounts:NestBank Current Account"),
        "p174519": ("Tranfer to Polish current using Transferwise", "Current Money:Polish Accounts:NestBank Current Account"),

        # flights and transport
        "ryanair": ("Payment for Ryanair tickets", "Expenses:Other Expenses:Travel and Entertainment:Flights"),
        "uber \*trip|uber\* trip": ("Payment for Uber trip", "Expenses:Other Expenses:Transport"),
        "northern rail": ("Payment for rail tickets", "Expenses:Other Expenses:Transport"),
        "www.tpexpress.co": ("Payment for rail tickets", "Expenses:Other Expenses:Transport"),
        "tfl travel": ("Payment for rail tickets", "Expenses:Other Expenses:Transport"),
        "shipley stn": ("Payment for rail tickets", "Expenses:Other Expenses:Transport"),

        #games
        "365games": ("Payment for FIFA game at 365games", "Expenses:Other Expenses:Travel and Entertainment:Games"),
        "playstation": ("Payment for PlayStation subscription", "Expenses:Other Expenses:Travel and Entertainment:Games"),
        "the game collectio": ("Payment for FIFA game at The Game Collections", "Expenses:Other Expenses:Travel and Entertainment:Games"),

        # travel
        "yorkshire dales ic|castle|national trust|kenwood house": ("Payment for tickets on the trip", "Expenses:Other Expenses:Travel and Entertainment"),
        "burnley.*footbal": ("Payment for football tickets", "Expenses:Other Expenses:Travel and Entertainment"),
        "hotel|airbnb": ("Payment for Ryanair tickets", "Expenses:Other Expenses:Travel and Entertainment:Accomodation"),

        # withdraw cash
        "powerplay|eduletting|dioce|notemachine|soccerleagues|szymon krysiak|goals football|goals bradford": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous"),
        "205322 11jun": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous"),
        "nat west bank|404144shipley|grange sports|bradford sports ce": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous"),

        # betting / gambling
        "betfred|bet365": ("betting / gambling at betfred or bet365", "Expenses:Other Expenses:Miscellaneous"),

        # temu.com
        "temu.com": ("Purchase at Temu.com", "Expenses:Other Expenses:Miscellaneous:Temu"),

        # dividend
        "204514.*dividend": ("Dividends payment for shareholder - Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:XMementoIT Business Current"),

        # car expenses
        "vehicle tax": ("Road tax payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Road Tax"),
        "petrol|fuel|sainsburys smkts|shell": ("payment for petrol", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Fuel"),
        "gear up service|ziobrorecoverycar|northcliffe|servicing stop|jct car|f1auto|formula one autoce|halfords": ("Payment for car repair or service", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Services"),
        "ttc driver trainin": ("Payment for TTC speeding course", "Expenses:Other Expenses:InfinitiQ50 expenses"),
        "axa insurance|1stcentralinsuranc|darwin insurance": ("Car insurance payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Insurance"),
        "2getherinsuran": ("Breakdown Cover", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Breakdown Cover"),
        "car parks|airedale nhs|city of york": ("Car park payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Car Parks"),
        "parking|parki|leeds park row|citipark|riverbank": ("Car park payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Car Parks"),
        "harrogate borough|q park leeds": ("Car park payment", "Expenses:Other Expenses:InfinitiQ50 expenses:Infiniti Q50 - Car Parks"),

        # taxes
        "hmrc gov.uk|hmrc self assessme": ("HMRC - Self-assessment Tax on accounts for year 2021/2022", "Expenses:Other Expenses:Taxes:Self-Assessment Tax"),

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
        "latte|costa|bakery|the old library|batch\?d|avanti|villette|the corner shop": ("Payment for coffee and/or cake", "Expenses:Other Expenses:Dining"),
        "mcdonald": ("Payment for dining at McDonalds", "Expenses:Other Expenses:Dining"),
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
        "pizza|papajohn": ("Payment for pizza", "Expenses:Other Expenses:Dining"),
        "hinxton hall": ("Payment for dining at Hinxton Hall", "Expenses:Other Expenses:Dining"),
        "the red lion": ("Payment for dining at The Red Lion", "Expenses:Other Expenses:Dining"),
        "bella italia": ("Payment for dining at Bella Italia", "Expenses:Other Expenses:Dining"),
        "salt east parade": ("Payment for dining at Salt East Parade", "Expenses:Other Expenses:Dining"),
        "sumup \*jagoda": ("Payment for dining at Polski Klub Jagoda", "Expenses:Other Expenses:Dining"),
        "restau": ("Payment for dining at restaurant", "Expenses:Other Expenses:Dining"),
        "hawthorne farm": ("Payment for dining at Hawthorne Farm", "Expenses:Other Expenses:Dining"),
        "higher ground": ("Payment for dining at Higher Ground Cafe", "Expenses:Other Expenses:Dining"),
        "tambourine cof": ("Payment for dining at Tambourine Coffee", "Expenses:Other Expenses:Dining"),
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
        "agh solutions|apple vending": ("Payment for dining at Airedale Hospital", "Expenses:Other Expenses:Dining"),
        "the rosse": ("Payment for dining at The Rosse", "Expenses:Other Expenses:Dining"),
        "myrtle grove": ("Payment for dining at The Myrtle Grove", "Expenses:Other Expenses:Dining"),
        "linton kitchen|cenu ltd": ("Payment for dining at Linton Kitchen", "Expenses:Other Expenses:Dining"),
        "rontec hinckley": ("Payment for coffee at Rontec Hinckley", "Expenses:Other Expenses:Dining"),
        "cuthbert brodrick": ("Payment for coffee at Cuthbert brodrick", "Expenses:Other Expenses:Dining"),
        "stick or twist": ("Payment for coffee at Stick or Twist", "Expenses:Other Expenses:Dining"),
        "the hockney": ("Payment for dining at The Hockney", "Expenses:Other Expenses:Dining"),
        "on 03 sep clp": ("Payment for coffee at Lord Rodney", "Expenses:Other Expenses:Dining"),
        "camden food|skyrack|bowery|yorkshire catering|ppoint_\*wisla": ("Payment for dining at Camden Food", "Expenses:Other Expenses:Dining"),
        "sumup \*takeaway ge": ("Payment for dining at Bistro Polish Food", "Expenses:Other Expenses:Dining"),
        "livery rooms": ("Payment for dining at Livery Rooms at Keighley", "Expenses:Other Expenses:Dining"),
        "the hut halifax": ("Payment for coffee at The Hut Halifax", "Expenses:Other Expenses:Dining"),
        "merrie england cof": ("Payment for coffee at Merrie England Coffee", "Expenses:Other Expenses:Dining"),
        "barum top inn": ("Payment for coffee at Barum top inn", "Expenses:Other Expenses:Dining"),
        "flowbird smart cit": ("Payment for coffee at Flowbird Smart", "Expenses:Other Expenses:Dining"),
        "drakes fish and ch": ("Payment for dining at Drakes Fish and Chips", "Expenses:Other Expenses:Dining"),
        "the bingley arms": ("Payment for dining at The Bingley Arms", "Expenses:Other Expenses:Dining"),
        "george & dragon": ("Payment for dining at George & Dragon", "Expenses:Other Expenses:Dining"),
        "cookhouse n pub": ("Payment for dining at Cookhouse n pub", "Expenses:Other Expenses:Dining"),
        "stump cross ca": ("Payment for dining at Stump Cross Cavern", "Expenses:Other Expenses:Dining"),
        "webster": ("Payment for dining at Webster", "Expenses:Other Expenses:Dining"),
        "shimla spice": ("Payment for dining at Shimla Spice", "Expenses:Other Expenses:Dining"),
        "starseeds": ("Payment for dining at Star Seeds", "Expenses:Other Expenses:Dining"),
        "tim hortons": ("Payment for dining at Tim Hortons", "Expenses:Other Expenses:Dining"),
        "the lion at settle": ("Payment for dining at The Lion at Settle", "Expenses:Other Expenses:Dining"),
        "talbot arms": ("Payment for dining at Talbot Arms at Settle", "Expenses:Other Expenses:Dining"),
        "bell.*on 05 may clp": ("Payment for dining at Bell", "Expenses:Other Expenses:Dining"),
        "iw group services": ("Payment for dining at IW Group Services", "Expenses:Other Expenses:Dining"),
        "the hop": ("Payment for dining at The Hop", "Expenses:Other Expenses:Dining"),
        "airedale heifer": ("Payment for dining at Airdale Heifer", "Expenses:Other Expenses:Dining"),
        "the duck & drake": ("Payment for dining at The Duck & Drake", "Expenses:Other Expenses:Dining"),
        "devonshire inn": ("Payment for dining at Devonshire Inn", "Expenses:Other Expenses:Dining"),
        "the quays": ("Payment for coffee at The Quays", "Expenses:Other Expenses:Dining"),
        "the old unicorn": ("Payment for dining at The Old Unicorn", "Expenses:Other Expenses:Dining"),
        "the racehorses hot": ("Payment for dining at The Racehorses hot", "Expenses:Other Expenses:Dining"),
        "multi cook": ("Payment for dining at the Multi Cook", "Expenses:Other Expenses:Dining"),
        "denbrook service": ("Payment for dining at the Danebrook service", "Expenses:Other Expenses:Dining"),
        "bold privateer": ("Payment for dining at the Bold Privateer pub", "Expenses:Other Expenses:Dining"),
        "uber \*one": ("Payment for delivery at Uber One", "Expenses:Other Expenses:Dining"),
        "q park the light": ("Payment for delivery at Q Park The Light", "Expenses:Other Expenses:Dining"),
        "wakefield football": ("Payment for delivery at Wakefield Football Center", "Expenses:Other Expenses:Dining"),
        "six poor folk": ("Payment for delivery at Six Poor Folk", "Expenses:Other Expenses:Dining"),

        # transfer on my bank accounts
        "204112 43041824": ("From Current Account to Savings Account", "Current Money:English Accounts:Barclays Accounts:Barclays Savings Account"),
        "203009 33477010": ("From Car Savings account to Savings Account", "Current Money:English Accounts:Barclays Accounts:House & Car Savings"),
        "204529 53155420": ("From Current account to ISA Account", "Current Money:English Accounts:Barclays Accounts:Barclays ISA"),
        "to monzo": ("to monzo", "Current Money:English Accounts:Monzo Accounts:Monzo Current Account"),
        "204112 63557790": ("From Savings Account to Current Account", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "204112 23955761": ("From Madzia current account", "Imbalance:MyWifeCurrentAccountImbalance"),
        "203009 00897604": ("From Madzia's MInvestment", "Current Money:English Accounts:Barclays Accounts:M Investment"),
        "203009 33312712": ("From Madzia's Madzia Savings", "Current Money:English Accounts:Barclays Accounts:Madzia Savings"),
        "203009 00450529": ("to Lily Savings", "Current Money:English Accounts:Barclays Accounts:Lily Savings"),
        "203009 83154998": ("to Roxy Savings", "Current Money:English Accounts:Barclays Accounts:Roxy Account"),
        "www.hl.co.uk": ("into heargraves langsdown account", "Current Money:English Accounts:HL:HL Fund & Share Account"),

        # internet subscriptions
        "netflix": ("Netflix payment", "Expenses:Other Expenses:TVandInternet"),
        "disney plus": ("Disney+ payment", "Expenses:Other Expenses:TVandInternet"),
        "amazon prime|prime video": ("Amazon Prime payment", "Expenses:Other Expenses:TVandInternet"),
        "amazon music": ("Amazon Music payment", "Expenses:Other Expenses:Entertainment"),
        "the athletic": ("internet portal subscription - The Athletic", "Expenses:Other Expenses:Entertainment"),
        "telegraph subscrip": ("internet portal subscription - The Telegraph", "Expenses:Other Expenses:Entertainment"),
        "surfshark": ("internet subscription - Surfshark", "Expenses:Other Expenses:Entertainment"),
        "now.*ents|now.*boost|now 783fb|now.*on 28 dec": ("internet subscription - NOW TV", "Expenses:Other Expenses:Entertainment"),
        "times newspapers": ("internet subscription - The Times", "Expenses:Other Expenses:Entertainment"),
        "leeds playhouse": ("Payment for delivery at Leeds Playhouse", "Expenses:Other Expenses:Entertainment"),

        # gifts and charity
        "gofundme": ("Charity GoFundMe", "Expenses:Other Expenses:GiftsAndCharity"),
        "nspcc": ("Charity NSPCC", "Expenses:Other Expenses:GiftsAndCharity"),
        "darowizna|zrzutka.pl": ("Darowizna na cele charytatywne", "Expenses:Other Expenses:GiftsAndCharity"),

        # apps
        "google pla": ("Payment for app/movie at Google Play", "Expenses:Other Expenses:Travel and Entertainment"),

        # kids expenses
        "smyths": ("Toys at Smyths for Roksanka", "Expenses:Other Expenses:KidsExpenses"),
        "tumble town": ("Toys at Smyths for soft play", "Expenses:Other Expenses:KidsExpenses"),
        "monster kidz": ("Monster Kidz for soft play", "Expenses:Other Expenses:KidsExpenses"),
        "kidzplay": ("Kidzplay for soft play", "Expenses:Other Expenses:KidsExpenses"),

        # other expenses
        "jacek baranowski": ("Return of loan to Jacek", "Income:Gifts Received"),
        "bernas|moscicki|szczypczyk|matusiewicz|lubiarz": ("Return of payment to PowerPlay", "Income:Gifts Received"),

        "blood and medical|expresstest": ("Payment for Covid Tests", "Expenses:Other Expenses:CovidTests"),

        "land registry": ("Payment for getting house title from HM Land Registry", "Expenses:Other Expenses:Fees"),
        "post office": ("Payment for letter at post office", "Expenses:Other Expenses:Fees"),
        "currys": ("Payment for electronic device at Currys", "Expenses:Other Expenses:Electronics"),

        "aws emea": ("Payment for AWS Services", "Expenses:Other Expenses:Miscellaneous"),
        "amznmktplace|amazon.co.uk|amazon\* 204-": ("Payment at amazon", "Expenses:Other Expenses:Miscellaneous"),
        "ebay": ("Payment for something at Ebay", "Expenses:Other Expenses:Miscellaneous"),
        "registry-trust": ("Payment for something at Registry Trust", "Expenses:Other Expenses:Miscellaneous"),
        "britishredcros": ("Payment to British Red Cross", "Expenses:Other Expenses:Miscellaneous"),
        "ikea": ("Payment at IKEA", "Expenses:Other Expenses:Miscellaneous"),
        "salts mill": ("Payment at Salts Mill", "Expenses:Other Expenses:Miscellaneous"),
        "hayloftplants": ("Payment at hayloftplants", "Expenses:Other Expenses:Miscellaneous"),
        "zettle_\*bradford d": ("Payment at hayloftplants", "Expenses:Other Expenses:Miscellaneous"),
        "sumup \*stump": ("Payment at something", "Expenses:Other Expenses:Miscellaneous"),
        "phoenix trophies": ("Payment for Maja throphy at phoenix throphies", "Expenses:Other Expenses:Miscellaneous"),
        "wyp.org.uk": ("unknown payment", "Expenses:Other Expenses:Miscellaneous"),

        "sopra steria": ("Payment for biometrics appointment", "Expenses:Other Expenses:Citizenship"),
        "2naa031107562": ("Payment for biometrics appointment", "Expenses:Other Expenses:Citizenship"),
        "ncs vue-pte exam": ("Payment for English Exam", "Expenses:Other Expenses:Citizenship"),
        "psi services int": ("Payment for Live in the UK exam", "Expenses:Other Expenses:Citizenship"),
        "hm passport": ("Payment for British passport", "Expenses:Other Expenses:Citizenship"),

        # Sundries
        "rushpay.pl|gift round lim|bowling green|savills|crossed shuttle|marks&spencer|midpoint|teachhospi|crowd of favours|tarquins|westcliffe pharma|de verde|quaytickets|lukasz czajka|mfs and c|sanandaj|royd ices|sainsburys.*mkts|saltaire mini mark|north yorkshire co|owlerton stadium|loaded gourmet|zettle|eagle events|m tomas|fine confection|vms salts|spar |manchester airport|moto birch east": ("Payment for miscellaneous", "Expenses:Other Expenses:Miscellaneous"),

        # ============= BUSINESS ACCOUNT ======================
        "hiscox": ("Hiscox - Payment for Business insurance to Hiscox", "Expenses:Bussiness Expenses:Business Insurance"),
        "zodeq|langham bgc": ("Payment from WellcomeSanger invoice", "Income:UK Income:WellcomeSanger"),
        "the bridge.*720763": ("Payment from AstraZeneca invoice", "Income:UK Income:AstraZeneca"),
        "djma it solutions": ("Payment from DJMA IT Solutions invoice", "Income:UK Income:DJMA IT Solutions"),
        "commission for": ("Bank account fees", "Expenses:Bussiness Expenses:Fees"),
        "current account.*(sto|bbp)": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "hmrc gov\.uk\.paye|hmrc etmp": ("HMRC - PAYE - Payment for NIC contributions", "Expenses:Other Expenses:Taxes:NIC contributions"),
        "hmrc (gov\.uk\ )?cotax": ("Corportation Tax Payment for XMementoIT for 2019/2020", "Expenses:Other Expenses:Taxes:Corporation Tax"),
        "hmrc (gov\.uk\ )?vat": ("VAT payment + surcharge", "Expenses:Other Expenses:Taxes:VAT Payment"),
        "companies house": ("Confirmation statement in Companies House", "Expenses:Bussiness Expenses:Fees"),
        "nicola toothill": ("Payment for accountancy ", "Expenses:Bussiness Expenses:Accountancy"),
        "helen kaye": ("Payment for accountancy (Corporation Tax)", "Expenses:Bussiness Expenses:Accountancy"),
        "ppwdl4ux222242jz3c": ("Transfer from XMementoIT's PayPal", "Current Money:English Accounts:Paypal accounts:Paypal XMementoIT GBP"),
        "companieshouse web": ("Confirmation statement payment to Companies House", "Expenses:Bussiness Expenses:Fees"),
        "hmrc shipley.*28266": ("Corportation Tax Payment for XMementoIT for 2020/2021", "Expenses:Other Expenses:Taxes:Corporation Tax"),
        "hmrc shipley.*475pz": ("HMRC - PAYE - Payment for NIC contributions", "Expenses:Other Expenses:Taxes:NIC contributions"),
        "dick hudsons|salute at the whit|halfway house": ("Company Annual Event - Christmas Party", "Expenses:Bussiness Expenses:CompanyAnnualEvents"),
        "packt birmingham|udemy": ("professional courses and ebooks subscription", "Expenses:Bussiness Expenses:Trainings and courses"),
        "chatgpt subscripti|openai.*usa": ("ChatGPT subscription", "Expenses:Bussiness Expenses:Trainings and courses"),
        "a medium corporati": ("Medium subscription", "Expenses:Bussiness Expenses:Trainings and courses"),
        "woodfield farm|travelodge": ("accomodation during business trip", "Expenses:Bussiness Expenses:Bussiness travels"),
        "the red mug|stgcoach/ctylink|az\ rdc\ catering|eb\ \*az\ cambridge|burger king brampt|wendy's brampton|trainline|the piccadilly|the pen and pencil": ("expenses during business trip", "Expenses:Bussiness Expenses:Bussiness travels"),

        # salary and dividends
        "uram-ziobro.*dividend": ("Dividends payment for shareholder - Magdalena Uram-Ziobro", "Imbalance:MyWifeCurrentAccountImbalance:MadziaDividends"),
        "uram-ziobro.*salary": ("Salry payment for  Magdalena Uram-Ziobro", "Imbalance:MyWifeCurrentAccountImbalance:MadziaSalary"),
        "204112.*dividend": ("Dividends payment for shareholder - Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "204112.*salary": ("Salary payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),
        "204112.*mileage": ("Mileage payment for Damian Ziobro", "Current Money:English Accounts:Barclays Accounts:Barclays Current Account"),

        "uram-ziobro": ("From Madzia for bills payment", "Imbalance:MyWifeCurrentAccountImbalance"),
        "enrgy2003570711": ("Council Tax Rebate", "Imbalance:MyWifeCurrentAccountImbalance"),

        # interest
        "interest paid gross": ("Interest income", "Income:Interest Income:Savings Interest"),

        # ============= NEST BANK ACCOUNT ======================
        "podatek.*naliczanie odsetek": ("interest tax", "Expenses:Other Expenses:Fees PL"),
        "naliczanie odsetek": ("interest", "Income:Interest Income:Savings Interest PL"),

        "onet\.pl": ("subskrypcja onet.pl", "Expenses:Other Expenses:Fees PL:Onet"),
        "codesmarkt": ("subskrypcja polską tv", "Expenses:Other Expenses:Fees PL:TV"),
        "youtubepremium": ("subskrypcja youtube premium", "Expenses:Other Expenses:Fees PL:Youtube"),
        "warszawa canal": ("subskrypcja canal+ online", "Expenses:Other Expenses:Fees PL:CanalPlus"),
        "opłata za|137997|pilot wp vod|wp pilot|powiadomienia sms|cyberfolks|ovh\.pl|hosting\.linux|oczytanie|automaty pro|player\.pl|poznan new hope|viaplay": ("opłata", "Expenses:Other Expenses:Fees PL"),
        "stacja paliw|bp-jaslo|bp-babica|orlen": ("Platnosc za paliwo", "Expenses:Other Expenses:DaciaSandero expenses:DaciaSandero - Fuel"),


        "002/05/23": ("PRZELEW 1/2 za fakturę VAT numerPF0 002/05/23 - Sprzedaż budynkumieszka lnego położonego Klęczany nadziałce  o numerze ewidencyjnym1845/8", "Current Money:Assets:HouseKleczanyPL:Kupno"),
        "pf0004\/05\/23": ("Przelew za fakturę PF0004/05/23 - udział w działce o numerze 544/1 w Klęczanach", "Current Money:Assets:HouseKleczanyPL:Kupno"),
        "pf0003\/05\/23": ("Przelew za fakturę PF0004/05/23 - udział w działce o numerze 1845/2 w Klęczanach", "Current Money:Assets:HouseKleczanyPL:Kupno"),
        "f0001\/01\/23": ("Przelew za fakturę F0001/01/23 - zadatek na kupno domu w Klęczanach na działce o numerze na za 1845/2 w Klęczanach", "Current Money:Assets:HouseKleczanyPL:Kupno"),

        "na dom w pl|na zadatek na dom": ("from Damian's Nest savings account to Damian's Nest current account", "Current Money:Polish Accounts:NestBank Current Account"),

        "na wykończenie domu w kleczanach|na płatność za łazienkę|wykończenie domu w klęczanach|na wykończenie domu|na główne konto|na glowne konto": ("from Damian's Nest savings account to Damian's Nest current account", "Current Money:Polish Accounts:NestBank Current Account"),

        "numer zamówienia 209674|numer zamówienia 202281": ("Kupno drzwi wewnętrznych w Leroy Merlin", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "zamówienie numer 463202": ("Płatność za wyposażenie kuchni w Leroy Merlin", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "numer zamówienia 463206": ("Płatność za montaż kuchni w Leroy Merlin", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "zamówienia numer 462515": ("Wyposażenie łazienki w Leroy Merlin", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "inwentaryzacja przyłącza gazowego": ("Inwentaryzacja przyłącza gazowego", "Current Money:Assets:HouseKleczanyPL:Dokumenty"),
        "świadectwo energetyczne": ("Klęczany 265F - Świadectwo Energetyczne", "Current Money:Assets:HouseKleczanyPL:Dokumenty"),
        "inwentaryzacja geodezyjna": ("Inwentaryzacja geodezyjna w Klęczanach na działce 1845/8", "Current Money:Assets:HouseKleczanyPL:Dokumenty"),
        "leroy merlin rzeszow 2891": ("Płatność za lampy, zarowki itp.", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "fs\/3\/12\/2023": ("Płatność dla Grześka Kurowskiego za: dokończenie paneli, malowanie, montaż drzwi, układanie płytek", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "fs\/1\/09\/2023": ("Płatność dla Grześka Kurowskiego za łazienkę", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "odwodnienia i zbiornik na": ("Zwrot to taty za odwodnienia i zbiornik na deszczówkę", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "vat 1175\/bud\/2023": ("Zwrot to taty za odwodnienia i zbiornik na deszczówkę", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "nexterio": ("Płatność za płytki do łazienki", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "0046\/09\/23\/kr": ("Płatność za zbiornik na deszczówkę", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "nr 158\/08\/23|187\/06\/23": ("Płatność dla Domus AK Wanat Jasło za elementy do malowania, kleje itp.", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "faktura nr 2\/2023": ("Płatność dla Grześka Kurowskiego za układanie paneli", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "montaż kotła kondensacyjnego": ("Płatność za piec i montaż pieca dla Gaskop", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "panele i listy przypodłogowe": ("Płatność za panele i listy przypodłogowe", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "leroy merlin rzeszow 905": ("Drobne rzezcy do wykończeń z Leroy Merlin", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "74627157067": ("Płatność za cegiełkę na ścianę", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "damian ziobro\ -\ klęczany": ("Płatność dla elektryka za dodatkowe prace", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "jaslo.*astro": ("Kleje, farby itp.", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "faktura nr 3192/js/2023": ("akcesoria do wykończenia łazienki i paneli", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "ceg.y dekoracyjnej": ("Układanie cegiełki dekoracyjnnej", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "54320837": ("Płatność za gaz", "Current Money:Assets:HouseKleczanyPL:Oplaty:Rachunki"),
        "abonamentowa za wodę": ("Płatność za wodę", "Current Money:Assets:HouseKleczanyPL:Oplaty:Rachunki"),
        "74340460729": ("Płatność za ubezpieczenie domu", "Current Money:Assets:HouseKleczanyPL:Oplaty:Rachunki"),
        "gkpge.pl": ("Płatność za prąd", "Current Money:Assets:HouseKleczanyPL:Oplaty:Rachunki"),
        "podatek od nieruch(o)?mości": ("Podatek od nieruchomości w Klęczanach", "Current Money:Assets:HouseKleczanyPL:Oplaty:Rachunki"),
        "221\/01\/08494": ("Podatek od nieruchomości w Godowej", "Current Money:Assets:HouseKleczanyPL:Oplaty:Rachunki"),
        "allaboutparen": ("Kupno kursu dla rodziców", "Expenses:Other Expenses:Miscellaneous PLN"),
        "karola brzezinska|jaslo spp|fahri cekic|otopark|ph sobniow|kaufland|marmax|biedronka|limoni|pepco|delikatesy|(strzyzow|wisniowa|sedziszow mal|jaslo|rzeszow|iwonicz-zdroj) zabka|zappka|stokrotka|lody u myszki|sklep wielobranzowy|lody stachura|jaslo lidl|cukiernia": ("Zakupy zywnosciowe w polsce", "Expenses:Other Expenses:Miscellaneous PLN"),
        "empik.com|spp rynek|kwiaciarnia|rossmann|apteka|stomatolog|9276 strzyzow|allegro|9276 gorlice|spodlady.com|roland adam|strzyzow planet|mg tkaniny|arcom mercik|qh66463h5|krosno pok\.017|2601831|balice mpl|strzyzow obwozny|fryzjer|gorlice firma|sedziszow mal me|automat spec|myjnia|459846|zaliczka na chrzciny|71471990582|71437588142": ("Inne zakupy w Polsce (ex. rossmann, apteka, dentysta, allegro, kwiaciarnia itp.)", "Expenses:Other Expenses:Miscellaneous PLN"),
        "pizzeria (al capone|faraon)|kebab|keks": ("Obiad wyjściowy w Polsce", "Expenses:Other Expenses:Dining PLN"),
        "bez tytulu": ("Od Barbi", "Expenses:Other Expenses:Miscellaneous PLN"),
        "doladowanie play": ("play phone topup", "Expenses:Bussiness Expenses:Phone PLN"),
        "1000200000000501481880|467619|467216|464418|jysk|rzeszow wito 200|leroy-merlin rzeszow 200|psb mrowka|strzyzow mrowka|leroy-merlin 1809|utwardzenie drogi|c46fc096|mal mazak|460129": ("Platność za drobne rzeczy do wykończenia domu", "Current Money:Assets:HouseKleczanyPL:Wykonczenia"),
        "wypłata gotówki": ("withdraw in cash machine", "Expenses:Other Expenses:Miscellaneous PLN"),
        "od męża": ("od męża", "Current Money:Polish Accounts:NestBank Current Account"),
        "587694869|531378322": ("Przelew przez WISE na dom w PL z konta w UK", "Imbalance-PLN"),

        "zwrot zaliczki na chrzest": ("zwrot zaliczki za chrzest", "Expenses:Other Expenses:Miscellaneous PLN"),
        "pracownia zlotnicza": ("złoty wisiorek dla Madzi", "Expenses:Other Expenses:Miscellaneous PLN"),

        "6780591194": ("inna transakcja", "Expenses:Other Expenses:Miscellaneous PLN"),

        # ============= PKO BP ACCOUNT ======================
        "podatek od odsetek kapita": ("interest tax", "Expenses:Other Expenses:Fees PL"),
        "kapitalizacja odsetek": ("interest", "Income:Interest Income:Savings Interest PL"),

        "ata miesi.*za kart": ("card usage fee", "Expenses:Other Expenses:Fees PL"),
        "real\. zlec\.": ("monthly transaction fee", "Expenses:Other Expenses:Fees PL"),
        "prowadzenie rachunku": ("account usage fee", "Expenses:Other Expenses:Fees PL"),
        "przelew zew\.dowol\.": ("external transfer fee", "Expenses:Other Expenses:Fees PL"),
        "nazwa odbiorcy : bik": ("BIK - oplata za sprawdzanie w BIK", "Expenses:Other Expenses:Fees PL"),
        "15 1240 2786 1111 0010 6797 3234": ("honorarium autorski - armoryka", "Income:Other Income"),
        "71 1560 0013 0500 1210 3047 7700": ("15 years investment", "Current Money:Assets:15 Years Investment"),
        "70 1870 1045 2078 1027 1517 0001": ("from nestbank current", "Current Money:Polish Accounts:NestBank Current Account"),
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
