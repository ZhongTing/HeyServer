from app.wsgi import user_manager
from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(['GET'])
def fetch_popular_issue(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
        }

        # action
        user = user_manager.get_user_from_token(token)
        issues = user.fetch_popular_issue()
        return JSONResponse.output({
            "issues": issues
        })

    except Error as error:
        return JSONResponse.output(error)