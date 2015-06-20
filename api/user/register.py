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

        # POST data
        data = {
            "coupon_code": request.get_data("coupon"),
            "device_identity": request.get_data("deviceIdentity"),
        }

        # action

        # test code
        if data["coupon_code"] == "test":
            coupon = Coupon.objects.get(coupon_code="test")
            coupon.used = False
            coupon.save()

        coupon = Coupon.get(data["coupon_code"])

        user = UserManager.register(coupon, data["device_identity"])
        return JSONResponse.output(user.token)

    except Error as error:
        return JSONResponse.output(error)