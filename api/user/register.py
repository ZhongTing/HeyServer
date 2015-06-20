from core.account.coupon import Coupon
from core.account.user_manager import UserManager
from core.utility.error_exceptions import Error
from core.utility.request_checker import RequestChecker
from core.utility.json_response import JSONResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def register(request):
    try:
        request = RequestChecker(request)

        # header
        token = request.get_token()

        # POST data
        data = {
            "coupon_code": request.get_data("coupon"),
            "device_identity": request.get_data("deviceIdentity"),
        }

        # action
        coupon = Coupon.get(data["coupon_code"])

        user = UserManager.register(coupon, data["device_identity"])

        return JSONResponse.output({
            "token": user.access_token
        })

    except Error as error:
        return JSONResponse.output(error)