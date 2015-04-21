from core.account.user_manager import UserManager
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(['GET'])
def pull_recommends(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # GET data
        data = {
        }

        # action
        user = UserManager.get_user_from_token(token)
        result = user.pull_recommends()
        return JSONResponse.with_200(json_result=result)

    except Exception as error:
        return JSONResponse.with_403(error_message=error.message)