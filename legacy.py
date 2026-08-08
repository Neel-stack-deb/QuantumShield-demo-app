import hashlib


def legacy_digest(data):
    # Legacy hash algorithms.
    md5_digest = hashlib.md5(data).hexdigest()
    sha1_digest = hashlib.sha1(data).hexdigest()

    return md5_digest, sha1_digest


def modern_digest(data):
    return hashlib.sha256(data).hexdigest()