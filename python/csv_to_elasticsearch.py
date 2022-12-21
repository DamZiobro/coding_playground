from elasticsearch import Elasticsearch, helpers
import csv
import json
import datetime
import sys

URL_ES = 'http://localhost:9200/'
CSV_FILE = 'data.csv'
INDEX = 'hpiuk'
TYPE = '_price_paid'
ID_FIELD = 'id'
BULK_SIZE = 5000


def rows_from_a_csv_file(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield row


def get_elasticsearch_connection():
    print('Connecting to elasticsearch...')
    es = Elasticsearch(URL_ES)
    print("Connected to: " + str(es.info()))
    print('Done!')
    return es


if __name__ == "__main__":
    csv_file = sys.argv[1]
    print(f"Start reading data from CSV file: {csv_file}")

    es_conn = get_elasticsearch_connection()
    transactions = []
    es_conn.indices.create(index=INDEX, ignore=400)

    for i, row in enumerate(rows_from_a_csv_file(sys.argv[1])):
        record = {
            "_index": INDEX,
            "_doc_type": "_doc",
            "_id": row["id"].strip('"'),
            "_source": {
                "paid_price": int(row["paid_price"]),
                "transaction_date": datetime.datetime.strptime(row["transaction_data"], '%Y-%m-%d %H:%M').date(),
                "county": row["county"].strip('"').strip("{").strip(""),
                "postcode": row["postcode"].strip('"'),
            }
        }
        transactions.append(record)

        if len(transactions) >= BULK_SIZE:
            print(f'Inserting bulk data {i+1}...')
            for success, info in helpers.parallel_bulk(es_conn, transactions):
                if not success:
                    print(f"ERROR: {info}")
            print(f'done!')
            transactions = []

    if len(transactions) > 0:
        print('Inserting final bulk data...')
        for success, info in helpers.parallel_bulk(es_conn, transactions):
            if not success:
                print(f"ERROR: {info}")

    print('Finished.')
