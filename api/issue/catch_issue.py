from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def catch_issue(request):
    return HttpResponse({"status": "success"}, status=status.HTTP_200_OK, content_type="application/json")