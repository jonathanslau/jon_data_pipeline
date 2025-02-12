import os

def get_secret(key: str) -> str:
    """get secret from windows environment variables"""
    
    if not key:
        raise ValueError('Error: Provide name of secret key.')
    value = os.getenv(key)
    
    if value:
        return value
    else:
        raise KeyError(f"Secret {key} not found in environment variables.")