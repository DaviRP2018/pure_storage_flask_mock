import logging

from flask import Flask, jsonify, request
from flask_restful import Api
from resources.array import ResourceApiArray
from resources.auth_session import ResourceApiAuthSession
from resources.drive import ResourceApiDrive
from resources.h_group_scale_volume import ResourceApiHgroupScaleVolume
from resources.hardware import ResourceApiHardware
from resources.host import ResourceApiHost
from resources.host_group import ResourceApiHgroup
from resources.message import ResourceApiMessage
from resources.p_group import ResourceApiPgroup
from resources.version import ResourceApiVersion
from resources.volume import ResourceApiVolume
from resources.volume_scale_01 import ResourceApiVolumeScaleDc3Edpure01Scale01
from resources.volume_scale_02 import ResourceApiVolumeScaleDc3Edpure01Scale02
from resources.volume_scale_hgroup_01 import (
    ResourceApiVolumeScaleDc3Edpure01Scale01Hgroup,
)
from resources.volume_scale_hgroup_02 import (
    ResourceApiVolumeScaleDc3Edpure01Scale02Hgroup,
)
from settings import BASE_URL

app = Flask(__name__)


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


api = Api(app)

api.add_resource(
    ResourceApiAuthSession,
    f"{BASE_URL}/auth/session",
    resource_class_kwargs={"logger": app.logger},
)

api.add_resource(
    ResourceApiArray, f"{BASE_URL}/array", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiDrive, f"{BASE_URL}/drive", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiHardware, f"{BASE_URL}/hardware", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiHgroup, f"{BASE_URL}/hgroup", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiHgroupScaleVolume,
    f"{BASE_URL}/hgroup/Scale/volume",
    resource_class_kwargs={"logger": app.logger},
)
api.add_resource(ResourceApiHost, f"{BASE_URL}/host", resource_class_kwargs={"logger": app.logger})
api.add_resource(
    ResourceApiMessage, f"{BASE_URL}/message", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiPgroup, f"{BASE_URL}/pgroup", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiVersion, "/api/api_version", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiVolume, f"{BASE_URL}/volume", resource_class_kwargs={"logger": app.logger}
)
api.add_resource(
    ResourceApiVolumeScaleDc3Edpure01Scale01,
    f"{BASE_URL}/volume/Scale/dc3edpure01_Scale01",
    resource_class_kwargs={"logger": app.logger},
)
api.add_resource(
    ResourceApiVolumeScaleDc3Edpure01Scale01Hgroup,
    f"{BASE_URL}/volume/Scale/dc3edpure01_Scale01/hgroup",
    resource_class_kwargs={"logger": app.logger},
)
api.add_resource(
    ResourceApiVolumeScaleDc3Edpure01Scale02,
    f"{BASE_URL}/volume/Scale/dc3edpure01_Scale02",
    resource_class_kwargs={"logger": app.logger},
)
api.add_resource(
    ResourceApiVolumeScaleDc3Edpure01Scale02Hgroup,
    f"{BASE_URL}/volume/Scale/dc3edpure01_Scale02/hgroup",
    resource_class_kwargs={"logger": app.logger},
)


@app.route("/cache-me")
def cache():
    return "nginx will cache this response"


@app.route("/info")
def info():
    resp = {
        "connecting_ip": request.headers["X-Real-IP"],
        "proxy_ip": request.headers["X-Forwarded-For"],
        "host": request.headers["Host"],
        "user-agent": request.headers["User-Agent"],
    }

    return jsonify(resp)


@app.route("/flask-health-check")
def flask_health_check():
    return "success"
