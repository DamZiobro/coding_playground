from llama_index import VectorStoreIndex, SimpleDirectoryReader
import openai  # you need to have OPENAI_API_KEY expoerted

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex(documents)
index.save_to_disk("index.json")

response = index.query("Who is Alice?")
logger.info(response)
