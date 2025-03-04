from django.views import View
from django.shortcuts import render


class Window(View):
    def get(self, request):
        return render(request, "hello.html", {"data": "This is capybara", "TODD": 6})

