#!/usr/bin/env python

# Connect to service instance by running import statements.
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.document import Document
import os, json

from dotenv import load_dotenv


load_dotenv()

account_user_name = os.environ["account_name"]
apikey = os.environ["apikey"]
databaseName = "pets-database"


def main():
    client = Cloudant.iam(account_name=account_user_name, api_key=apikey, connect=True)
    myDatabaseDemo = client.create_database(databaseName)
    f = open('sample_pets.json',)
    data = json.load(f)
    for document in data["pets"]:
        kind = document["kind"]
        name = document['name']
        age = document['age']
        breed = document['breed']
        comments = document['comments']
        image_url = document['image_url']

        jsonDocument = {
                "kind": kind,
                "name": name,
                "age": age,
                "breed": breed,
                "comments": comments,
                "image_url": image_url
            }

        newDocument = myDatabaseDemo.create_document(jsonDocument)

if __name__=='__main__':
    main()

