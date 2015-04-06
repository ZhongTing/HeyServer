from core.response.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def catch_issue(request):
    return JSONResponse.with_200(json_result={"Hello": "test catch issue"})