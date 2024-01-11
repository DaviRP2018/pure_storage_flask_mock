from flask import request
from flask_restful import Resource, reqparse
from settings import (
    AUTH_SESSIONS,
    FRAGILE_SESSION,
    SESSION_LOCATION,
    UNAUTHORIZED_RESPONSE,
)
from utils import delete_session, session_exists


class ResourceApiAuthSession(Resource):
    def __init__(self, *args, **kwargs):
        self.logger = kwargs["logger"]

    parser = reqparse.RequestParser()
    parser.add_argument(
        "api_token",
        type=str,
        required=True,
        help="Missing API Token!",
        # location="form",
    )

    def post(self):
        remote_addr = request.remote_addr
        return manage_auth(remote_addr, self.logger)


def manage_auth(remote_addr, logger):
    data = ResourceApiAuthSession.parser.parse_args()
    token = data["api_token"]
    valid_token = token in AUTH_SESSIONS

    if session_exists(remote_addr, logger):
        if valid_token:
            return {"username": AUTH_SESSIONS[token]}, 200
        elif FRAGILE_SESSION:
            # This actually never run, because PP verify auth by /api/1.4/array
            # QA have to manually delete the session at /tmp
            # Or dev can put this validation at ResourceApiArray like `manage_auth(remote_addr)`
            # just to delete or keep the session
            #
            # Delete the session since token has changed to a wrong one
            # Not sure how Pure handles this case, but we are going to do this way
            # Better for testing
            delete_session(remote_addr)
            return [], 401
        else:
            return [], 200
    else:
        if valid_token:
            file_path = f"{SESSION_LOCATION}/pure_session_{remote_addr}"
            with open(file_path, "w"):
                logger.info("Created new session for %s.", remote_addr)
            return {"username": AUTH_SESSIONS[token]}, 200
        return UNAUTHORIZED_RESPONSE[0], UNAUTHORIZED_RESPONSE[1]
