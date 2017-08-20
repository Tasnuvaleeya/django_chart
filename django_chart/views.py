from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})
        # return render(request, 'charts.html', {"customers":10})


def get_date(request, *args, **kwargs):
    data ={
        'sales': 100,
        'customers': 10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, *args, **kwargs):
        # usernames = [user.username for user in User.objects.all()]
        qs_count = User.objects.all().count()
        labels = ["User", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]

        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)