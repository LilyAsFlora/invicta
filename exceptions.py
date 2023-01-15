"""Exception classes for Invicta."""

class CannotCaesarEncryptException(Exception):
    """Raised when attempting to decrypt ciphertext that could not have
    been encrypted with Caesar cipher."""
    pass
