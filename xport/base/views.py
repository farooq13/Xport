from django.shortcuts import render
from django.views import View



class Index(View):
  def get(self, request, *args, **kwargs):
    context = {

    }
    return render(request, 'base/index.html', context)