from core.account.authorization import Authorization
from core.response.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def raise_issue(request):
    auth = Authorization(request)

    if auth.is_valid():
        return JSONResponse.with_200(json_result={"Hello": "test raise issue"})
    else:
        return JSONResponse.with_403(error_message=auth.error_message)