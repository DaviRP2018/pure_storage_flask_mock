from flask import request
from flask_restful import Resource
from settings import UNAUTHORIZED_RESPONSE
from utils import get_synced_response, session_exists

from server.resources.mappings import (
    ARRAY_API_CHOICES,
    ARRAY_API_CHOICES_ACTION,
    ARRAY_API_CHOICES_CONTROLLERS,
    ARRAY_API_CHOICES_SPACE,
)


class ResourceApiArray(Resource):
    def __init__(self, *args, **kwargs):
        self.logger = kwargs["logger"]

    def get(self):
        remote_addr = request.remote_addr

        if not session_exists(remote_addr, self.logger):
            return UNAUTHORIZED_RESPONSE[0], UNAUTHORIZED_RESPONSE[1]

        query_string = request.args
        if "space" in query_string:
            payload = ARRAY_API_CHOICES_SPACE
        elif "controllers" in query_string:
            payload = ARRAY_API_CHOICES_CONTROLLERS
        elif query_string.get("action") == "monitor" and query_string.get("historical") == "1h":
            payload = ARRAY_API_CHOICES_ACTION
        else:
            payload = ARRAY_API_CHOICES

        response = get_synced_response(payload, self.logger)
        return response[0], response[1]
