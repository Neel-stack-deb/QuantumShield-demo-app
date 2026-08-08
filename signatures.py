from cryptography.hazmat.primitives.asymmetric import ec

# Classical elliptic-curve signature.
# QuantumShield should detect ECDSA-P256.
signer = ec.ECDSA(ec.SECP256R1())


def sign_message(message):
    return signer