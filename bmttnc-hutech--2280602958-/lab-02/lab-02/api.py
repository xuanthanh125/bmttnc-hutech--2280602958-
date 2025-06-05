from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.Transposition import TranspositionCipher
app = Flask(__name__) 
#Caesar
caesar_cipher = CaesarCipher();
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    return jsonify({'encrypted_text': caesar_cipher.encrypt_text(text, key)})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    return jsonify({'decrypted_text': caesar_cipher.decrypt_text(text, key)})



#Vigenere
vigenere_cipher = VigenereCipher()
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    return jsonify({'encrypted_text': vigenere_cipher.encrypt_text(text, key)})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    return jsonify({'decrypted_text': vigenere_cipher.decrypt_text(text, key)})



#Railfence
railfence_cipher = RailFenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = int(data['key'])
    return jsonify({'encrypted_text': railfence_cipher.rail_fence_encrypt(text, key)})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = int(data['key'])
    return jsonify({'decrypted_text': railfence_cipher.rail_fence_decrypt(text, key)})



#Playfair
playfair_cipher = PlayFairCipher()
@app.route('/api/playfair/creatematrix',methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix":playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'encrypted_text': playfair_cipher.playfair_encrypt(text, playfair_matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'decrypted_text': playfair_cipher.playfair_decrypt(text, playfair_matrix)})


#Transposition
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)