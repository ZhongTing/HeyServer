from app.wsgi import user_manager
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def issue_regret(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
            "issue_id": request.get_data("issueId"),
        }

        # action
        issue_id = int(data["issue_id"])
        user = user_manager.get_user_from_token(token)
        user.regret_issue(issue_id)
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)