# main.py
from app.blockchain import Blockchain

def main():
    # Blockchain 생성자를 이용해 인스턴스를 생성하고, 필요한 인자를 전달합니다.
    bitcoin = Blockchain()

    # previous_block_hash = '519619156945694516'
    # current_block_data = [
    #     {
    #         'amount' : 10,
    #         'sender' : 'BAD48461AB6',
    #         'recipient' : 'ag4a6e4g9a4w5eg',
    #     },
    #     {
    #         'amount' : 30,
    #         "sender" : '15DSGA86G4AD46GAE',
    #         'recipient' : 'aega6we16ga1we65g1',
    #     },
    #     {
    #         'amount' : 100,
    #         "sender" : 'GAWEKGAWE66GA16W1E1661',
    #         'recipient' : 'a6w191a9be156b1a',
    #     },
    # ]
    # nonce = 100


    bc1 ={
        "chain": [
        {
        "hash": "3f086d9ef2ea9e855d880e3381ed6d4cc7bbc57d2dcf815dbf7b179659400460",
        "index": 1,
        "merkle_root": "926a9afa65f355220cf4c1196152a3c8e5780d520ca7bee92ab7c12d68266ffa",
        "nonce": 778,
        "previous_block_hash": "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
        "timestamp": 1685176348592,
        "transactions": [
        {
        "amount": 50,
        "recipient": "8ca1082b309f409f9c5226667ee679bf",
        "sender": "0",
        "transaction_id": "4e598b74a1804bcdb7c57c8f9ff8b7f2"
        }
        ]
        },
        {
        "hash": "00003d99ee97ae8fe67f100381b47690d248bf124ee3a651bddf68ae077901a0",
        "index": 2,
        "merkle_root": "09a55c96e640043ccebee5e51cc917a765cab9f943adc84b74240ab28c6cf2fb",
        "nonce": 40080,
        "previous_block_hash": "3f086d9ef2ea9e855d880e3381ed6d4cc7bbc57d2dcf815dbf7b179659400460",
        "timestamp": 1685177461523,
        "transactions": [
        {
        "amount": 6.25,
        "recipient": "00",
        "sender": "00",
        "transaction_id": "d40454ca3ded48bc9049d8dc568ce76b"
        },
        {
        "amount": 700,
        "recipient": "bgjvvfvvasdvasdv",
        "sender": "aasdvasdvfdsv"
        },
        {
        "amount": 700,
        "recipient": "bgjvvfvcdsdsadv",
        "sender": "aasdvfddfvd"
        }
        ]
        }
        ],
        "current_node_url": "http://localhost:8090",
        "genesis_nonce": 778,
        "merkle_tree_proecss": [],
        "network_nodes": [],
        "pending_transactions": [
        {
        "amount": 6.25,
        "recipient": "c63a0a254a434b728855b25b12551813",
        "sender": "00",
        "transaction_id": "89d3bf136c7d44a7ba7373eb2ba4da13"
        }
        ]
    }

    print('VALID:', bitcoin.chain_is_valid(bc1['chain']))
    #print(bitcoin.hash_block(previous_block_hash,current_block_data,900))

if __name__ == "__main__":
    main()
