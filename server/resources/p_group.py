from flask import request
from flask_restful import Resource
from settings import UNAUTHORIZED_RESPONSE
from utils import get_synced_response, session_exists

from server.resources.mappings import (
    PROTECTION_GROUP_API_CHOICES,
    PROTECTION_GROUP_API_CHOICES_RETENTION,
    PROTECTION_GROUP_API_CHOICES_SCHEDULE,
    PROTECTION_GROUP_API_CHOICES_SPACE,
)


class ResourceApiPgroup(Resource):
    def __init__(self, *args, **kwargs):
        self.logger = kwargs["logger"]

    def get(self):
        remote_addr = request.remote_addr
        if not session_exists(remote_addr, self.logger):
            return UNAUTHORIZED_RESPONSE[0], UNAUTHORIZED_RESPONSE[1]

        query_string = request.args
        if "space" in query_string:
            payload = PROTECTION_GROUP_API_CHOICES_SPACE
        elif "retention" in query_string:
            payload = PROTECTION_GROUP_API_CHOICES_RETENTION
        elif "schedule" in query_string:
            payload = PROTECTION_GROUP_API_CHOICES_SCHEDULE
        else:
            payload = PROTECTION_GROUP_API_CHOICES

        response = get_synced_response(payload, self.logger)
        return response[0], response[1]
