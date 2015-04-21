from core.account.user_manager import UserManager
from core.utility.error_message import ErrorMessage
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def raise_issue(request):
    request = RequestChecker(request)

    # header
    token = request.get_token()

    # post data
    data = {
        "actor": request.get_data("actor"),
        "event": request.get_data("event"),
        "place": request.get_data("place", null=True),
        "latitude": request.get_data("latitude", null=True),
        "longitude": request.get_data("longitude", null=True),
    }

    #
    print request
    user = UserManager.get_user_from_token(token)

    if user is None:
        return JSONResponse.with_403(error_message=ErrorMessage.authorization_error)

    elif not request.is_valid:
        return JSONResponse.with_403(error_message=request.error_message)

    else:
        user.raise_issue(data)
        return JSONResponse.with_200(json_result={})