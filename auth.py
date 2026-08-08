from Crypto.PublicKey import RSA

# Legacy authentication key.
# QuantumShield should detect RSA-2048.
key = RSA.generate(2048)


def authenticate(message):
    return key.public_key().export_key()