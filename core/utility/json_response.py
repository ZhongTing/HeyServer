from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer


class JSONResponse():
    def __init__(self):
        pass

    @classmethod
    def with_200(cls, json_result=None):
        return cls._response(True, json_result, status.HTTP_200_OK)

    @classmethod
    def with_403(cls, error_message):
        return cls._response(False, error_message, status.HTTP_403_FORBIDDEN)

    @classmethod
    def with_406(cls, error_message):
        return cls._response(False, error_message, status.HTTP_406_NOT_ACCEPTABLE)

    @staticmethod
    def _response(success, result, response_code):
        json_object = {
            "status": "success" if success else "fail"
        }

        if result is not None:
            json_object["result"] = result

        return HttpResponse(JSONRenderer().render(json_object), status=response_code, content_type="application/json")
