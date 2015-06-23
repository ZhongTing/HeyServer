from app.wsgi import user_manager, filter_manager
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_filter(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
        }

        # action
        user = user_manager.get_user_from_token(token)
        filters = filter_manager.list_filter(user)
        return JSONResponse.output({
            "filters": filters
        })

    except Error as error:
        return JSONResponse.output(error)