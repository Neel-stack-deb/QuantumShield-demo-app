# Internet-facing authentication API protecting customer credentials
# and long-term financial records.
#
# Data retention: long_term
# Exposure: public API
# Sensitivity: customer credentials / financial data

from Crypto.PublicKey import RSA

key = RSA.generate(2048)