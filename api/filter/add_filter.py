from app.wsgi import user_manager, filter_manager
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def add_filter(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
            "subject": request.get_data("subject")
        }

        # action
        user = user_manager.get_user_from_token(token)
        filter_id = filter_manager.add_filter(user, data["subject"])
        return JSONResponse.output({
            "id": filter_id
        })

    except Error as error:
        return JSONResponse.output(error)