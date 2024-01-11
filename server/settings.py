DEBUG = True
BASE_URL = "/api/1.4"
HOST = "0.0.0.0"
PORT = 8000  # gunicorn controls it at docker-compose. Will only work on manual run

AUTH_SESSIONS = {
    # token | owner
    "<token>": "purepack-temp",
}
# Delete session if an already authenticated request hits with a different and wrong token
# Won't work, see comment in auth_session.py
FRAGILE_SESSION = True

SESSION_LOCATION = "/tmp"

UNAUTHORIZED_RESPONSE = ({"error": "Unauthorized"}, 401)
