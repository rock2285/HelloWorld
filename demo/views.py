from django.views import View
from django.shortcuts import render


class Window(View):
    def get(self, request):
        return render(request, "hello.html", {"color": "red", "data": "This is fun"})

class Away(View):
    def get(self, request):
        return render(request, "away.html")
