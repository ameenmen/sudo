import requests
from dotenv import load_dotenv
load_dotenv()
import time
import os

swap_url =  "https://api-1.origins.ordinox.xyz/relay2/api/swap"

auth_token = os.getenv('first_acc_bearer')
headers = {
    "Authorization": f"Bearer {auth_token}"
}

first_txn_payload = {
  "address_a": "0x5D840528D5C677a2E3aCf3368fe11bc4f2817342",
  "address_b": "0x5D840528D5C677a2E3aCf3368fe11bc4f2817342",
  "amount": "0.2",
  "asset_a": "BASET.USDX-0X2D4B1EDA9514675A9F8CB13B3F3A7475EBB81024",
  "asset_b": "BASET.WOOF-0X4F9FA0435DBF11C4A93C4006D39918A6B672D08D",
  "for_signature": True,
  "nonce_a": 1,
  "signature_block": {
    "address": "0x5D840528D5C677a2E3aCf3368fe11bc4f2817342",
    "signature": "test",
    "signature_type": "EVM"
  }

}

second_txn_payload = {
  "address_a": "0x5D840528D5C677a2E3aCf3368fe11bc4f2817342",
  "address_b": "0x5D840528D5C677a2E3aCf3368fe11bc4f2817342",
  "amount": "0.2",
  "asset_a": "BASET.USDX-0X2D4B1EDA9514675A9F8CB13B3F3A7475EBB81024",
  "asset_b": "BASET.WOOF-0X4F9FA0435DBF11C4A93C4006D39918A6B672D08D",
  "for_signature": False,
  "nonce_a": 2,
  "signature_block": {
    "address": "0x5D840528D5C677a2E3aCf3368fe11bc4f2817342",
    "signature": "66fcfda9aa190c7c323c6c1500718eb4640d7833a5f4b1601336c06413272b7813e77b726243d8b96b782c495ca48024a9880677024f8eca01bf4f4ddaacacc81b",
    "signature_type": "EVM"
  }
}


def send_txn():
    r_1 = requests.post(swap_url, json=first_txn_payload, headers=headers)
    r_2 = requests.post(swap_url, json=second_txn_payload, headers=headers)
    if r_2.status_code == 200:
        print(f"Done Txn : {txn_counter}")
    else:
        print(f"failed {r_2.text}")
txn_counter = 1
while txn_counter < 21:
    send_txn()
    txn_counter +=1
    time.sleep(10)
   
