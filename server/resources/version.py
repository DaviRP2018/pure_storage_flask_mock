from flask_restful import Resource
from utils import get_synced_response

from server.resources.mappings import VERSION_API_CHOICES


class ResourceApiVersion(Resource):
    def __init__(self, *args, **kwargs):
        self.logger = kwargs["logger"]

    def get(self):
        """
        It seems, if I understood correctly, in our PP original code flow,
        the version endpoint doesn't need an auth.
        """
        # remote_addr = request.remote_addr
        # if session_exists(remote_addr, self.logger):
        response = get_synced_response(VERSION_API_CHOICES, self.logger)
        return response[0], response[1]
        # return UNAUTHORIZED_RESPONSE[0], UNAUTHORIZED_RESPONSE[1]
