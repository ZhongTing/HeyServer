from core.account.user_manager import user_manager
from core.utility.error_exceptions import Error
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
        user = user_manager.get_user_from_token(token)
        result = user.get_recommend_list()
        return JSONResponse.output(result)

    except Error as error:
        return JSONResponse.output(error)