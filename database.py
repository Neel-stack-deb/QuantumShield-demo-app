from Crypto.Cipher import AES

# AES-256-GCM is considered quantum-resistant at the
# symmetric-security level used by QuantumShield.
AES_KEY_SIZE = 256

cipher = AES.new(
    b"0123456789abcdef0123456789abcdef",
    AES.MODE_GCM,
)


def encrypt_record(data):
    return cipher.encrypt(data)