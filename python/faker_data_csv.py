#! /usr/bin/env python

from faker import Faker
import csv

CSV_HEADER=['name','age','street','city','county','postcode','lng','lat']
NUMER_OF_FAKE_PEOPLE = 10000

with open('data.csv','w') as data_file:
    mywriter=csv.writer(data_file)
    mywriter.writerow(CSV_HEADER)

    fake=Faker(["en_GB"])
    for r in range(NUMER_OF_FAKE_PEOPLE):
        mywriter.writerow(
            [
                fake.name(),
                fake.random_int(min=18, max=80, step=1), 
                fake.street_address(), 
                fake.city(),
                fake.county(),
                fake.postcode(),
                fake.longitude(),
                fake.latitude()
            ]
        )
