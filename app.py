from flask import Flask, jsonify, request
# from flask_cors import CORS
from blockchain import Blockchain
from argparse import ArgumentParser

app = Flask(__name__)
# CORS(app)


@app.route('/', methods=['GET'])
def chian():
    chain = test.chain
    dictChain = [block.__dict__.copy() for block in chain]

    return jsonify(dictChain), 200


@app.route('/mine', methods=['POST'])
def mine():
    """ mine a block """
    addBl=test.addBlcok
    if addBl != None:
        dictBlock = block.__dict__.copy()
        dictBlock['transactions'] = [tx.__dict__ for tx in dictBlock['transactions']]
        res = {
            'Block': dictBlock,
        }
        return jsonify(res), 200

    else:
        res ={
            'Message':'There is an error '
        }
        return jsonify(res), 500

@app.route('/opentxs', methods=['GET'])
def opentxs():
    """ get the unconfirmed transactions or any transaction has not been included in a block """
    txs = test.unconfirmed
    if txs != None:
        dictTx = [tx.__dict__ for tx in txs]
        res ={
            'Transactions ':dictTx
        }
        return jsonify(res), 200
    else:
        res ={
            'Message':'There is no transaction '
        }
        return jsonify(res), 500
@app.route('/sendtx', methods=['POST'])
def sendtx():
    """ send a transaction"""
    values = request.get_json()
    if not values:
        res = {
            'Message':'There is no input'
        }
        return jsonify(res), 400
    reqKeys = ['sender', 'receiver', 'amount']

    if not all (key in values for key in reqKeys):
        res = {
            'Message ':'There is a missing value'
        }
        return jsonify(res), 400
    sender =values['sender']
    receiver =values['receiver']
    amount = values['amount']
    addTx = test.addTransaction(sender,receiver,amount)
    if addTx != None:
        res ={
            'Transaction' : {
                'sender' : values['sender'],
                'receiver' : values['receiver'],
                 'amount' : values['amount']
            }
        }
        return jsonify(res), 200
    else:
        res = {
            'Message' : 'The transaction does not pass'
        }
        return jsonify(res), 500



if __name__ == '__main__':
    ser = ArgumentParser()
    ser.add_argument('-p', '--port', default=8020)
    args = ser.parse_args()
    port = args.port
    test = Blockchain()
    app.run(debug=True, port=port)
