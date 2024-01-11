from flask import request
from flask_restful import Resource
from settings import UNAUTHORIZED_RESPONSE
from utils import get_synced_response, session_exists

from server.resources.mappings import ARRAY_CONTROLLERS_API_CHOICES


class ResourceApiArrayControllers(Resource):
    def __init__(self, *args, **kwargs):
        self.logger = kwargs["logger"]

    def get(self):
        remote_addr = request.remote_addr
        if session_exists(remote_addr, self.logger):
            response = get_synced_response(ARRAY_CONTROLLERS_API_CHOICES, self.logger)
            return response[0], response[1]
        return UNAUTHORIZED_RESPONSE[0], UNAUTHORIZED_RESPONSE[1]
