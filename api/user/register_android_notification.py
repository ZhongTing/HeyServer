from app.wsgi import user_manager
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def register_android_notification(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
            "notification_token": request.get_data("gcmToken"),
        }

        # action
        user = user_manager.get_user_from_token(token)
        user.update_notification_token(data["notification_token"])
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)