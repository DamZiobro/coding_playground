#! /usr/bin/env python

from faker import Faker
import json

NUMER_OF_FAKE_PEOPLE = 10000

with open('data.json','w') as data_file:
    fake=Faker(["en_GB"])
    data_records = []
    for _ in range(NUMER_OF_FAKE_PEOPLE):
        record = {
            "name": fake.name(),
            "age": fake.random_int(min=18, max=80, step=1), 
            "street": fake.street_address(), 
            "city": fake.city(),
            "county": fake.county(),
            "postcode": fake.postcode(),
            "lng": float(fake.longitude()),
            "lat": float(fake.latitude())
        }
        data_records.append(record)
    json.dump(data_records, data_file)
