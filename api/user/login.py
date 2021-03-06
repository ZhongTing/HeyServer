from app.wsgi import user_manager
from core.account.user import User
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def login(request):
    try:
        request = RequestChecker(request)

        # header

        # POST data
        data = {
            "device_identity": request.get_data("deviceIdentity"),
        }

        # action
        if data["device_identity"] == "test":
            user = User.objects.get(device_identity="test")
            return JSONResponse.output(user.token)

        user = user_manager.get_user_from_device_identity(data["device_identity"])
        return JSONResponse.output(user.token)

    except Error as error:
        return JSONResponse.output(error)