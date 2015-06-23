from app.wsgi import user_manager, filter_manager
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def remove_filter(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
            "filter_id": int(request.get_data("filterId"))
        }

        # action
        user = user_manager.get_user_from_token(token)
        filter_manager.remove_filter(user, data["filter_id"])
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)