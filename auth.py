from Crypto.PublicKey import RSA

# Internet-facing authentication API.
# Protects customer credentials and financial records.
# Long-term retention for authentication history.
key = RSA.generate(2048)