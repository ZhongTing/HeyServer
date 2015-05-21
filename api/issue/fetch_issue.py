from core.account.user_manager import user_manager
from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(['GET'])
def fetch_issue(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
            "last_fetch_issue_id": request.get_param("lastFetchIssueId", null=True, default=0),
        }

        # action
        user = user_manager.get_user_from_token(token)
        issues = user.fetch_issue(data["last_fetch_issue_id"])
        return JSONResponse.output({
            "issues": issues
        })

    except Error as error:
        return JSONResponse.output(error)