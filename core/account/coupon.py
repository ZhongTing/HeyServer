from core.models import CouponModel
from core.utility.error_exceptions import CouponError


class Coupon(CouponModel):
    class Meta:
        proxy = True

    def __init__(self, *args, **kwargs):
        super(Coupon, self).__init__(*args, **kwargs)

    def use(self):
        self.used = True
        self.save()

    @staticmethod
    def get(coupon_code):
        try:
            return Coupon.objects.filter(used=False).get(coupon_code=coupon_code)
        except CouponModel.DoesNotExist:
            pass
        raise CouponError()