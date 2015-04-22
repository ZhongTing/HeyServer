from core.account.user_manager import UserManager
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def raise_issue(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
            "actor": request.get_data("actor"),
            "event": request.get_data("event"),
            "place": request.get_data("place", null=True),
            "latitude": request.get_data("latitude", null=True),
            "longitude": request.get_data("longitude", null=True),
        }

        # action
        user = UserManager.get_user_from_token(token)
        user.raise_issue(data)
        return JSONResponse.with_200()

    except Error as error:
        return JSONResponse.with_403(error_message=error.message)