import click
from base64 import b64decode, urlsafe_b64decode
from pprint import pprint
import json

@click.command()
@click.option("--license-blob", required=True, type=click.File())
def main(license_blob):
    blob_data = license_blob.read().strip().split('.')
    d1, header, encoded_payload, encoded_signature = blob_data

    payload = json.loads(b64decode(d2 + "===="))
    # pprint(payload)

    timestamp = payload['p']
    uuid = payload['u']
    encrypted = b64decode(b64decode(payload['s']))

    # pprint(encrypted)

    pprint(urlsafe_b64decode(d3 + "=="))

    pprint(b64decode(d4))

if __name__ == '__main__':
    main()
