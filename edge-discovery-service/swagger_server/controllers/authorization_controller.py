from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_oAuth2(token):
    return {'scopes': ['petstore:read'], 'uid': 'test_value'}

def validate_scope_oAuth2(required_scopes, token_scopes):
    return set(required_scopes).issubset(set(token_scopes))


