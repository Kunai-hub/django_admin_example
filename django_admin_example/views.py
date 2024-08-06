from django.shortcuts import render
from django.views import View


class MainPageView(View):

    def get(self, request):
        return render(request,
                      'main.html')


def welcome(request):
    return render(request, 'welcome.html')
