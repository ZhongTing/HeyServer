from core.account.user_manager import UserManager
from core.utility.error_message import ErrorMessage
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def raise_issue(request):
    request_checker = RequestChecker(request)

    # header
    token = request_checker.get_token()

    # post data
    actor = request_checker.get_data("actor")
    event = request_checker.get_data("event")
    place = request_checker.get_data("place", null=True)

    latitude = request_checker.get_data("latitude", null=True)
    longitude = request_checker.get_data("longitude", null=True)

    print request_checker

    user = UserManager.get_user_from_token(token)

    if user is None:
        return JSONResponse.with_403(error_message=ErrorMessage.authorization_error)

    elif not request_checker.is_valid:
        return JSONResponse.with_403(error_message=request_checker.error_message)

    else:
        return JSONResponse.with_200(json_result={"Hello": "test raise issue"})