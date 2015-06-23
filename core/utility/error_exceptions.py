from app.settings import DEBUG
from rest_framework import status


class Error(Exception):
    def __init__(self, message="unknown error!", status_code=status.HTTP_400_BAD_REQUEST):
        self._message = str(message)
        self._status_code = status_code

    @property
    def message(self):
        return self._message

    @property
    def status_code(self):
        return self._status_code

    def __str__(self):
        return "(%d) %s" % (self._status_code, self._message)


class AuthorizationError(Error):
    def __init__(self):
        super(AuthorizationError, self).__init__("authorization fail!", status.HTTP_401_UNAUTHORIZED)


class ParameterError(Error):
    def __init__(self):
        super(ParameterError, self).__init__("parameter missing!", status.HTTP_403_FORBIDDEN)


class SerializerError(Error):
    def __init__(self, serializer_errors):
        if not DEBUG:
            serializer_errors = "serializer error!"
        super(SerializerError, self).__init__(serializer_errors, status.HTTP_417_EXPECTATION_FAILED)


class DeviceIdentityExistedError(Error):
    def __init__(self):
        super(DeviceIdentityExistedError, self).__init__("device has registered!", status.HTTP_409_CONFLICT)


class IssueNotFound(Error):
    def __init__(self):
        super(IssueNotFound, self).__init__("issue not found!", status.HTTP_404_NOT_FOUND)


class CouponError(Error):
    def __init__(self):
        super(CouponError, self).__init__("coupon is not valid!", status.HTTP_403_FORBIDDEN)


class IssueFilterDuplicate(Error):
    def __init__(self):
        super(IssueFilterDuplicate, self).__init__("issue filter is duplicate", status.HTTP_409_CONFLICT)