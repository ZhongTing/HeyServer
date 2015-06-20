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
            "subject": request.get_data("subject"),
            "description": request.get_data("description"),
            "privacy_mode": request.get_bool_data("privacy", null=True, default=False),
            "place": request.get_data("place", null=True),
            "photo": request.get_file("photo", null=True),
            "latitude": request.get_data("latitude", null=True),
            "longitude": request.get_data("longitude", null=True),
        }

        # action
        user = user_manager.get_user_from_token(token)
        user.raise_issue(data)
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)