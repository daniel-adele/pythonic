from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

def auth_context(user):
    return AuthenticationContext(user)

def token(user, password):
    return auth_context().acquire_token_for_user(user, password)

def context(user):
    return ClientContext(user, auth_context())

