import pytest
from unittest import mock

from yosai import (
    DefaultHashService,
    HashRequest,
)

from passlib.context import CryptContext

@pytest.fixture(scope="function")
def authc_config():
    return {
        "hash_algorithms": {
            "bcrypt_sha256": {
                "default_rounds": 200000,
            },
            "sha256_crypt": {
                "default_rounds": 110000,
                "max_rounds": 1000000,
                "min_rounds": 1000,
                "salt_size": 16}},
        "private_salt": "privatesalt"
    }

@pytest.fixture(scope='function')
def default_context():
    return {'schemes': ['sha256_crypt'],
            'sha256_crypt__default_rounds': 180000}

@pytest.fixture(scope='function')
def crypt_context():
    return CryptContext(schemes=['sha256_crypt'])

@pytest.fixture(scope='function')
def hash_request():
    algorithm_name = "bcrypt_sha256"
    iterations = None 
    source = "secret"

    return HashRequest(source, iterations, algorithm_name)

@pytest.fixture(scope='function')
def default_hash_service():
    return DefaultHashService()

@pytest.fixture(scope='function')
def private_salt():
    return 'privatesaltysnack'

@pytest.fixture(scope='function')
def patched_default_hash_service(default_context, monkeypatch,
                                 default_hash_service, private_salt):

    # changes from ['bcrypt_sha256', 'sha256_crypt'] to [sha256_crypt]
    monkeypatch.setattr(default_hash_service, 'default_context', 
                        default_context) 
    monkeypatch.setattr(default_hash_service, 'private_salt', private_salt)

    return default_hash_service 