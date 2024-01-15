from requests.auth import HTTPBasicAuth

AUTH = HTTPBasicAuth('admin', 'admin')
INVALID_USER_AUTH = HTTPBasicAuth('', 'admin')
INVALID_PASSWORD_AUTH = HTTPBasicAuth('admin', '')