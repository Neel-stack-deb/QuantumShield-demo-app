# Post-quantum algorithms already present in the application.

KEM = "ML-KEM"
SIGNATURE = "ML-DSA"

# Standardized ML-KEM-768 target.
KEM_PARAMETER_SET = "ML-KEM-768"


def pqc_status():
    return {
        "kem": KEM_PARAMETER_SET,
        "signature": SIGNATURE,
    }